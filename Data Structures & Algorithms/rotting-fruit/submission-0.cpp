class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
        int n = grid.size(), m = grid[0].size();

        queue<pair<int, int>> q;

        int fresh = 0, res = 0;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j]==1)
                    fresh++;
                else if(grid[i][j]==2){
                    q.push({i, j});
                }
            }
        }

        // Multisource BFS

        int nbh[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        while(fresh && !q.empty()){
            
            int rotten = q.size();
            
            for(int j=0; j<rotten; j++){

                int x = q.front().first, y = q.front().second;

                q.pop();

                for(int i=0; i<4; i++){
                    int xx = x + nbh[i][0], yy = y + nbh[i][1];

                    if(xx>=0 && xx<n && yy>=0 && yy<m && grid[xx][yy]==1){
                        q.push({xx, yy});
                        grid[xx][yy] = 2;
                        fresh--;
                    }
                }
            }

            res++;
        }

        return fresh ? -1 : res;

    }
};
