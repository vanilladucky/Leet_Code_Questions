/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth){
    if (depth == 1){
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = root;
        node->right = NULL;
        return node;
    }
    else if (depth == 2){
        struct TreeNode* node_1 = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node_1->val = val;
        node_1->left = root->left;
        node_1->right = NULL;
        root->left = node_1;
        
        struct TreeNode* node_2 = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node_2->val = val;
        node_2->right = root->right;
        node_2->left = NULL;
        root->right = node_2;
    }
    else{
        if (root->left != NULL){
            root->left = addOneRow((root->left), val, depth-1);
        }
        if (root->right != NULL){
            root->right = addOneRow((root->right), val, depth-1);
        }
    }
    return root;
}
