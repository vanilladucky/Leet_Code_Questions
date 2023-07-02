/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root){
    void dfs(struct TreeNode* node){
        if (node == NULL) {
            return NULL;
        }
        struct TreeNode* tmp = node->right;
        node->right = node->left;
        node->left = tmp;
        dfs(node->right);
        dfs(node->left);
    }

    struct TreeNode* tmp = root;
    dfs(tmp);
    return root;
}
