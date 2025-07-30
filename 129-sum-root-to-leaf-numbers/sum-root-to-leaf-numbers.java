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
    int ans = 0;
    public int sumNumbers(TreeNode root) {
        if (root == null){
            return 0;
        }

        recurse(root, 0);
        return ans;
    }

    public void recurse(TreeNode root, int path){
        if (root == null){
            return;
        }
        path *= 10;
        path += root.val;

        if (root.left == null && root.right == null){
            ans += path;
        }

        recurse(root.left, path);
        recurse(root.right, path);
    }
}