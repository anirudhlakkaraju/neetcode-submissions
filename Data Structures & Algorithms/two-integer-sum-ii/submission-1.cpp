class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int lo = 0, hi = n-1;

        while(lo<hi){
            int sum = numbers[lo] + numbers[hi];
            if(sum > target)
                hi--;
            else if(sum < target)
                lo++;
            else
                return {lo+1, hi+1};
        }

        return {};
    }
};
