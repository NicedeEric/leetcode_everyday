# 目标是设计一个cache结构，和Redis类似。同时要求实现TTL(Time To Live)功能，以及LRU（Least Recently Used) 功能。

# TTL意味着，在get的时候，我们不允许get超过TTL的对象。
# LRU意味着，当set一个新的值的时候，假如超出了缓存的长度，那么就直接放弃最长时间没有被用的LRU的对象，添加新的对象

'''
实现思路：
我们结合三种数据结构：

功能	数据结构	说明
快速查找key	dict	存储 key -> Node 映射
LRU淘汰	双向链表	维护访问顺序，最近使用的在头部
TTL检查	dict + time 模块	每个键记录 过期时间，在访问时进行判断
'''

import time

class Node:
    def __init__(self, key, value, ttl):
        self.key = key
        self.value = value
        # 这里注意一定要判断 is not None 而不是 if ttl，因为ttl = 0的时候会返回false
        self.expire_time = time.time() + ttl if ttl is not None else None
        self.ttl = ttl
        self.pre = None
        self.next = None

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        # 定义 哈希表
        self.map = {}
        # 定义双向链表
        # 使用dummy head 和 dummy tail 因为涉及到很多头部和尾部的删除和添加操作，用dummy node会更好操作
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        # 连接双向链表
        self.head.next = self.tail
        self.tail.pre = self.head

    # 定义辅助函数

    # 把某个节点从双向链表中移除
    def _remove_node(self, node):
        node_pre = node.pre
        node_next = node.next
        node_pre.next = node_next
        node_next.pre = node_pre

    # 把某个新的节点添加到双向链表的头部
    def _add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    # 把某个已经在双向链表中的节点移到头部
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)
    
    # 执行LRU操作
    def _evict(self):
        node = self.tail.pre
        if node and node != self.head:
            self._remove_node(node)
            del self.map[node.key]

    # 判断某个节点是否已经过期
    def _is_expired(self, node):
        # 这里允许一些节点不会过期，假如expire time没有被设置的话，默认不会过期
        if node.expire_time is not None and node.expire_time < time.time():
            return True
        return False
    
    def get(self, key):
        if key not in self.map:
            return None
        
        node = self.map[key]
        if self._is_expired(node):
            self._remove_node(node)
            del self.map[node.key]
            return None
        else:
            # 这里的设计是get了之后，expire time 会重置。假如不需要的话，就不需要更新只需要把node移到最前面
            self._move_to_head(node)
            if node.ttl:
                node.expire_time = time.time() + node.ttl
            return node.value
    
    def set(self, key, value, ttl):
        current_time = time.time()
        if key in self.map:
            node = self.map[key]
            node.value = value
            if ttl is not None:
                node.ttl = ttl
                node.expire_time = current_time + ttl
            else:
                node.ttl = None
                node.expire_time = None
            self._move_to_head(node)
        
        else:
            if len(self.map) >= self.capacity:
                self._evict()
            
            node = Node(key, value, ttl)
            self.map[key] = node
            # 新node，使用add to head
            self._add_to_head(node)
