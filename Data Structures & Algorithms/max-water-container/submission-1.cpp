class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size(), lo = 0, hi = n-1;
        int res = 0;

        while(lo<hi){
            int ht = min(heights[lo], heights[hi]), len = hi-lo;
            res = max(res, ht * len);

            if(heights[lo] < heights[hi])
                lo++;
            else
                hi--;
        }

        return res;
    }
};
