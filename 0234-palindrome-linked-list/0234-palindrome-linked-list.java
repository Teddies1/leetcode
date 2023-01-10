/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        /*
        ListNode cur = head;
        Stack<Integer> s = new Stack<>();
        while(cur != null){
            s.push(cur.val);
            cur = cur.next;
        }
        while(head != null){
            if (s.pop() != head.val){
                return false;
            }
            head = head.next;
        }
        return true;
        */
        Stack<Integer> s = new Stack<>();
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            s.push(slow.val);
            fast = fast.next.next;
            slow = slow.next;
        }
        if(fast != null){
            slow = slow.next;
        }
        while(slow != null){
            if (s.pop() != slow.val){
                return false;
            }
            slow = slow.next;
        }
        return true;
    }
    
}