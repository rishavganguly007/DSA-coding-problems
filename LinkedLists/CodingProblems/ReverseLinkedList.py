# code -> https://www.codingninjas.com/codestudio/problems/799897
# resource -> https://www.youtube.com/watch?v=iRtLEoL-r-g&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=27

from math import *
from collections import *
from sys import *
from os import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.
    newHead = None
    while( head != None):
        next = head.next
        head.next = newHead
        newHead = head
        head = next
    return newHead

