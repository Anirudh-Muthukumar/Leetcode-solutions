/*
Idea: Peak and valley approach

Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int n = prices.size();
        for(int i = 1; i < n; ++i){
            if(prices[i] > prices[i-1]){
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
    }
};