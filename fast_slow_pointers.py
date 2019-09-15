'''

Determine if there is a cycle in a linked list

                  i
Head > A > B > C > D > E
               ^       |
                --------
                
def hasCycle(Node head): # output true or false


Is this a good approach:
	keep track of visited nodes
	if we visit a node that's been visited, then there is a cycle and return true
	if we never visit a node twice then there is no cycle and we would reach the end of our linkedlist and return false

set: {A, B, C, D, E

# if Node in set, return true
# if Node == null, return false
Node.next

space: O(n)
runtime: O(n)

# constraints on space
#   must be O(logn), O(1)

# O(1)
#   manipulate the input data in place
#   a set number of pointers

          f2
              s1
Head > A > B > C > D > E
       ^               |
         ------------

// runtime: O(n)
// space: O(1)
        
// fast = null
// slow = mid
// fast, slow in the cycle
                
//
    if (head == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    
    
    while (fast != null && fast.next != null) {
        if (fast == slow) {
            return true;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    
    return false;

fast and slow pointer?

'''


'''

find the k-th to last element in a linked list

k = 2
count = 6
                   
Head > A > B > C > D > E > F > null
                               f


runtime: O(n)
space: O(1)


    if (head == null) {
        return null;
    }

    int n = k;
    ListNode fast = head;
    ListNode curr = head;
    
    // move fast pointer to k nodes ahead
    while (n-- != 0) {
        if (fast == null) {
            return null;
        }
        fast = fast.next;
    }
    
    // move both pointers until fast at the end of the linked list
    while (fast != null) {
        count++
        curr = curr.next;
        fast = fast.next;
    }
    
    return curr;


'''

def cycle_check(linked_list):
    # keep track of visited nodes
    # if we visit a node that's been visited, then there is a cycle and return true
    # if we never visit a node twice then there is no cycle and we would reach the end of our linkedlist and return false


def kth_last_element(linked_list, k):
    # have a slow pointer
    # have a fast pointer
    # move fast pointer k times if not null then move slow pointer by 1