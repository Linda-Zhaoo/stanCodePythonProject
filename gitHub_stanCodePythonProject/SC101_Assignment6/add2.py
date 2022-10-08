"""
File: add2.py
Name: Linda Zhao
------------------------
There are two not None linked lists, represent 2 int.
However, the value is saved in reverse way in linked list.
The program would read 2 linked lists and calculate the sum then return the sum as new linked list.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    cur_l1 = l1
    cur_l2 = l2
    num_l1 = 0
    num_l2 = 0
    length_l1 = 0
    length_l2 = 0
    while cur_l1 is not None:
        num_l1 += cur_l1.val * (10**length_l1)
        cur_l1 = cur_l1.next
        length_l1 += 1
    while cur_l2 is not None:
        num_l2 += cur_l2.val * (10**length_l2)
        cur_l2 = cur_l2.next
        length_l2 += 1
    num_ans = num_l1 + num_l2

    add_num = num_ans % 10
    ans = ListNode(add_num, None)
    cur = ans
    num_ans = num_ans // 10
    while num_ans >= 1:
        add_num = num_ans % 10
        cur.next = ListNode(add_num, None)
        cur = cur.next
        num_ans = num_ans // 10
    #######################
    return ans


####### DO NOT EDIT CODE BELOW THIS LINE ########
def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
