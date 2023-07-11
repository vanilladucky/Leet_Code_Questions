/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isSame(struct TreeNode* root1, struct TreeNode* root2) {
    if (root1 == NULL && root2 == NULL){
        return true;
    }
    if (root1 && root2 && root1->val == root2->val){
        return isSame(root1->left, root2->left) && isSame(root1->right, root2->right);
    }
    return false; 
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot){
    if (root==NULL) {
        return false;
    }
    if (subRoot == NULL) {
        return true;
    }

    if (isSame(root, subRoot)){
        return true;
    }
    else {
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
}
