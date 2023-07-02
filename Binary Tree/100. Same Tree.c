/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    bool dfs(struct TreeNode* _p, struct TreeNode* _q){
        if (!_p && !_q){
            return true;
        }
        else if (_p && _q && _p->val == _q->val){
            return dfs(_p->left, _q->left) && dfs(_p->right, _q->right);
        }
        else {
            return false;
        }        
    }
    return dfs(p, q);
}
