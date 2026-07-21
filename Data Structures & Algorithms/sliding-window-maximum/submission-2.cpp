class Solution {
public:
    bool in(pair<int, int> p, int lo, int hi){
        if(p.second < lo || p.second > hi)
            return false;
        return true;
    }

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        priority_queue<pair<int, int>> heap;
        vector<int> res;
        int lo = 0, hi = 0;

        while(hi<n){

            heap.push(make_pair(nums[hi], hi));

            if(hi-lo+1 < k){
                hi++;
                continue;
            }

            while(!in(heap.top(), lo, hi)){
                heap.pop();
            }

            res.push_back(heap.top().first);
            hi++;
            lo++;
        }

        return res;
    }
};
