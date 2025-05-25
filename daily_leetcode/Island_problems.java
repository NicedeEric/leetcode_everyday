package daily_leetcode;

public class Island_problems {
    public static void main (String[] args) {
        int[][] islands = { {0,1,1,1,0},
                            {0,0,0,1,0},
                            {0,1,0,0,0},
                            {0,0,0,0,0},
                            {1,0,1,0,1}};
        int count = 0;
        for (int i=0;i<islands.length;i++) {
            for (int j=0;j<islands[0].length;j++) {
                if (islands[i][j] == 1) {
                    backTrack(islands, i, j);
                    count += 1;
                }
            }
        }
        System.out.println(count);   
    }

    public static void backTrack (int[][] islands, int i, int j) {
        if ((i >= 0) && (i<islands.length) && (j>=0) && (j<islands[0].length)) {
            if (islands[i][j] != 1) {
                return;
            } else {
                islands[i][j] = 0;
                for (int a=-1; a <= 1; a++) {
                    for (int b=-1; b <= 1; b++) {
                        if (a==0 && b==0) {
                            continue;
                        } else {
                            backTrack(islands, i+a, j+b);
                        }
                    }
                }
            }
        }
    }
}