/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, 0, 0, inorder.length-1);
    }
    public TreeNode helper(int[] preorder, int[] inorder, int preStart, int inStart, int inEnd){
        int rootindex = 0;
        if (inStart > inEnd || preStart > preorder.length){
            return null;
        }
        if (inStart == inEnd){
            return new TreeNode(preorder[preStart]);
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        for (int i = inStart; i <= inEnd; i++){
            if (inorder[i] == preorder[preStart]){
                rootindex = i;
            }
        }
        int leftsub = rootindex - inStart + 1;
        root.left = helper(preorder, inorder, preStart+1, inStart, rootindex-1);
        root.right = helper(preorder, inorder, preStart + leftsub, rootindex+1, inEnd);
        
        
        return root;
        
        
        
        
    }
}