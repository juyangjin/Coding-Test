class Solution {
    public int[] solution(String[] wallpaper) {
        int lux = Integer.MAX_VALUE;  // 가장 위 (min row)
        int luy = Integer.MAX_VALUE;  // 가장 왼쪽 (min col)
        int rdx = Integer.MIN_VALUE;  // 가장 아래 (max row)
        int rdy = Integer.MIN_VALUE;  // 가장 오른쪽 (max col)
        
        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    rdx = Math.max(rdx, i);
                    rdy = Math.max(rdy, j);
                }
            }
        }
        
        return new int[]{lux, luy, rdx + 1, rdy + 1};
    }
}
