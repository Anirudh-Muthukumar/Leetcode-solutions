/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<queue>
#include<algorithm>
using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> res;
        vector<int> level;
        int flag = 0;
        if(!root)
            return res;
        
        q.push(root);
        
        while(!q.empty()){
            int size = q.size();
            level.clear();
            while(size--){
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
            }
            if(flag)
                reverse(begin(level), end(level));
            
            flag  ^= 1;
            res.push_back(level);
        }
        
        return res;
    }
};