class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int res = 0;

        vector<int> left(n, height[0]), right(n, height[n-1]);

        for(int i=1; i<n; i++){
            left[i] = max(height[i-1], left[i-1]);
        }


        for(int i=n-2; i>=0; i--){
            right[i] = max(height[i+1], right[i+1]);
        }

        for(int i=1; i<n-1; i++){
            int curr = min(left[i], right[i]) - height[i];
            res += max(0, curr);
        }

        return res;
    }
};
