class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> v;
        for(int i=0; i<n; i++){
            v.push_back(make_pair(position[i], speed[i]));
        }

        sort(v.rbegin(), v.rend());

        // vector<int> jumps;
        // for(int i=0; i<n; i++){
        //     int dist = target - v[i].first, speed = v[i].second;
        //     int jump = (dist+speed-1)/speed;
        //     jumps.push_back(jump);
        //     cout << jump << endl;
        // }

        stack<double> st;

        for(int i=0; i<n; i++){
            double t = (double)(target - v[i].first)/v[i].second;
            if(st.empty() || t > st.top())
                st.push(t);
        }

        return st.size();
    }
        
//     car 1   2           2           1
//                     4.  4.  4.  4.  4.  4
//         0   1   2   3   4   5   6   7   8   9   10
//     car     1       2           2       1
//         0   1   2   3   4   5   6   7   8   9   10
//     car         1           2           2   1
//         0   1   2   3   4   5   6   7   8   9   10
//     car             1               2           2-1 -> 1 2 3
//         0   1   2   3   4   5   6   7   8   9   10
//     }
//     4 1 0 7
//     2 2 1 1
//     3 5 10 3

//     0 1 4 7
//     1 2 2 1
//    10 5 3 3

//     1 4
//     3 2
//     3 3

};
