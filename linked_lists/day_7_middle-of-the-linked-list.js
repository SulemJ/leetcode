/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let current = head;
    let size = 0;
    while(current.next){
        current = current.next;
        size++;
    }
    var half = Math.round(size/2);
    let index = 0;
    let hode = head;
    while(hode.next && index !== half  ){
        hode = hode.next;
        index++;                                                           
    }
    return hode;
};