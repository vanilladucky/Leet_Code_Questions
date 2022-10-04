/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool hasPathSum(struct TreeNode* root, int targetSum){
    if (root == NULL){
        return false;
    }
    if (root->val == targetSum && root->left == NULL && root->right == NULL){
        return true;
    }
    else{
        return hasPathSum(root->left, targetSum- root->val) || hasPathSum(root->right, targetSum- root->val);
    }
}
