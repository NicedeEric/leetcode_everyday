import time
import pytest
from cache import Cache  # 替换成你实际的类名和导入路径

def test_basic_get_set():
    cache = Cache(capacity=2)
    cache.set("a", 1, ttl=5)
    assert cache.get("a") == 1

def test_expiration():
    cache = Cache(capacity=2)
    cache.set("b", 2, ttl=1)
    time.sleep(1.1)
    assert cache.get("b") is None

def test_no_ttl_permanent():
    cache = Cache(capacity=2)
    cache.set("c", 3, ttl=None)
    time.sleep(1)
    assert cache.get("c") == 3

def test_lru_eviction():
    cache = Cache(capacity=2)
    cache.set("x", 10, ttl=5)
    cache.set("y", 20, ttl=5)
    cache.set("z", 30, ttl=5)  # should evict "x"
    assert cache.get("x") is None
    assert cache.get("y") == 20
    assert cache.get("z") == 30

def test_sliding_ttl():
    cache = Cache(capacity=2)
    cache.set("d", 4, ttl=2)
    time.sleep(1)
    assert cache.get("d") == 4  # access refreshes TTL
    time.sleep(1.5)
    assert cache.get("d") == 4
    time.sleep(2.1)
    assert cache.get("d") is None