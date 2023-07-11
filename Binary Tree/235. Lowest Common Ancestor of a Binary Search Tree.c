/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {

    if (MAX(p->val, q->val) < root->val){
        return lowestCommonAncestor(root->left, p, q);
    }
    else if(MIN(p->val, q->val) > root->val){
        return lowestCommonAncestor(root->right, p, q);
    }
    else {
        return root;
    }
}
