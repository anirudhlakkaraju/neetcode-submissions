class Solution {
public:

    bool dfs(vector<vector<int>> &adj, int x, vector<int> &visited, vector<int> &cycle){

        if(visited[x])
            return false;

        if(cycle[x])
            return true;
        
        cycle[x] = 1;
        
        for(int i=0; i<adj[x].size(); i++){
            if(dfs(adj, adj[x][i], visited, cycle))
                return true;
        }
        cycle[x] = 0;
        visited[x] = 1;

        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        int n = numCourses;

        vector<vector<int>> adj(n);
        for(int i=0; i<prerequisites.size(); i++){
            adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        vector<int> visited(n, 0), cycle(n, 0);

        for(int i=0; i<n; i++){
            if(!visited[i] && dfs(adj, i, visited, cycle))
                return false;
        }

        return true;
    }
};
