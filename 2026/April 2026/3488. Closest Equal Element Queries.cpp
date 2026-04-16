#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        
        // Find the maximum value in nums to size our frequency array appropriately.
        // Constraints state nums[i] <= 10^6, so this is well within memory limits.
        int max_val = 0;
        for (int x : nums) {
            if (x > max_val) {
                max_val = x;
            }
        }
        
        // Group all indices by the value present at that index.
        vector<vector<int>> pos(max_val + 1);
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        
        // Precompute the minimum circular distance for each index.
        vector<int> ans(n, -1);
        
        for (const auto& arr : pos) {
            int m = arr.size();
            
            // If the element appears only once, it has no equal elements.
            if (m <= 1) continue; 
            
            for (int k = 0; k < m; ++k) {
                int idx = arr[k];
                
                // In a circular array, the closest equal element will always 
                // be one of the immediate neighbors in our sorted 'arr'.
                int prev_idx = arr[(k - 1 + m) % m];
                int next_idx = arr[(k + 1) % m];
                
                // Calculate the circular distances
                int d1 = min(abs(idx - prev_idx), n - abs(idx - prev_idx));
                int d2 = min(abs(idx - next_idx), n - abs(idx - next_idx));
                
                // Store the minimum of the two distances
                ans[idx] = min(d1, d2);
            }
        }
        
        // Resolve all queries in O(1) time per query using our precomputed answers.
        vector<int> result(queries.size());
        for (int i = 0; i < queries.size(); ++i) {
            result[i] = ans[queries[i]];
        }
        
        return result;
    }
};
