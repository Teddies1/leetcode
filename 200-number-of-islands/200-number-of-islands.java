class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                if (grid[i][j] == '1'){
                    count++;
                    floodfill(grid, i , j, '0'); 
                }
            }                
        }
        return count;
    }
    public void floodfill(char[][] grid, int row, int column, char c){
        if (row < 0 || row >= grid.length || column < 0 || column >= grid[row].length || grid[row][column] == c){
            return;
        }
        grid[row][column] = c;
        floodfill(grid, row+1, column, c);
        floodfill(grid, row, column+1, c);
        floodfill(grid, row, column-1, c);
        floodfill(grid, row-1, column, c);
    }
}