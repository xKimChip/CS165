# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

import sys
import random
from math import log
from collections import namedtuple
from decimal import *

from typing import TypeVar
from dataclasses import dataclass

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
Rank = namedtuple("Rank", ["geometric_rank", "uniform_rank"])
tup = namedtuple('val', ['index', 'maxval'])

# @dataclass
# class Rank:
# 	geometric_rank: int
# 	uniform_rank: int

class TreeNode:
    def __init__(self, key, value, rank=None):
        self.key = key
        self.value = value
        self.rank = rank
        self.left = None
        self.right = None
        pass

class ZipZipTree:
    def __init__(self, capacity: int):
        # self.head = TreeNode(None, None, -1)
        self.head = None
        self.capacity = capacity
        self.size = 0
        pass

    def get_random_rank(self) -> Rank:
        geometric_rank = 0
        while random.random() < 0.5:
            geometric_rank += 1

        uniform_rank = random.randint(0, int(log(self.capacity, 2)**3) - 1)
        
        return Rank(geometric_rank, uniform_rank)
        pass

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        if rank is None:
            rank = self.get_random_rank()
        # increase size for new node inserted
        self.size += 1
        x = TreeNode(key, val, rank)  # Create the new node
        cur = self.head
        prev = None
        fix = None

        # Find the insertion point based on rank and key
        while cur and (rank < cur.rank or (rank == cur.rank and key > cur.key)):
            prev = cur
            cur = cur.left if key < cur.key else cur.right

        # If the head has no rank, set the head as the node
        if cur == self.head:
            self.head = x
        # if the key of inserted node is less than the previous node, then put it on the left
        # else put it on the right
        elif key < prev.key:
            prev.left = x
        else:
            prev.right = x
        

        
        # Establish horizontal links
        if cur is None:
            x.left, x.right = None, None
            return x

        if key < cur.key:
            x.right = cur
        else:
            x.left = cur

        # Fix vertical links from bottom up
        prev = x

        while cur:
            fix = prev
            if cur.key < key: 
                while cur and cur.key <= key:  # Check for prev
                    prev, cur = cur, cur.right
            else:  
                while cur and cur.key >= key:  # Check for prev
                    prev, cur = cur, cur.left

            if fix.key > key or (fix == x and prev.key > key):
                fix.left = cur
            else:
                fix.right = cur
     
        
        return x

    # removes item with parameter key from tree.
    # you can assume that the item exists in the tree.


    def remove(self, key: KeyType):
        cur = self.head
        prev = None

        while key != cur.key:
            prev = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        left = cur.left
        right = cur.right
        
        if left is None:
            cur = right
        elif right is None:
            cur = left
        elif left.rank >= right.rank:
            cur = left
        else:
            cur = right

        parent = cur
        if self.head.key == key:
            self.head = cur
        elif key < prev.key:
            prev.left = cur
        else:
            prev.right = cur

        while left and right:
            if left.rank >= right.rank:
                while left and left.rank >= right.rank:
                    prev = left
                    left = left.right
                prev.right = right
            else:
                while right and left.rank < right.rank:
                    prev = right
                    right = right.left
                prev.left = left
        return parent


    # returns the value of item with parameter key.
    # you can assume that the item exists in the tree.
    def find(self, key: KeyType) -> ValType:
        if self.size == 0:
            return None
        return self.__find(self.head, key)
        # pass
    # recursive approach will traversal based on a balanced BST until the key is find
    # if it isn't it returns null.
    def __find(self, node: TreeNode,key: KeyType) -> ValType:
        if node is None:
            return None
        # Return up the recursion calls if we found the node
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.__find(node.left, key)
        else:
            return self.__find(node.right, key)
    pass
    
    # returns the number of nodes in the tree.
    def get_size(self) -> int:
        return self.size
        # pass

    # return the height of the tree using recursion
    def get_height(self) -> int:
        return self.__get_height(self.head)
        # pass
    
    # Private recursion function
    def __get_height(self, node: TreeNode) -> int:
        if node is None:
            return -1
        # call the recursively to the bottom of each tree.
        left_height = self.__get_height(node.left)
        right_height = self.__get_height(node.right)
        
        # the path that took the longest will give the largest height, then that is returned to get_height
        return 1 + max(left_height, right_height)
        # pass
    
    # returns the depth of the item with parameter key.
    # you can assume that the item exists in the tree.
    def get_depth(self, key: KeyType):
        return self.__get_depth(self.head, key)
        # pass
    # Same idea as find recursively, but instead returning an int + 1 for each level down
    def __get_depth(self, node: TreeNode, key: KeyType):
        if node is None:
            return -1
        
        if key == node.key:
            return 0
        elif key < node.key:
            return 1 + self.__get_depth(node.left, key)
        else:
            return 1 + self.__get_depth(node.right, key)
        
        # pass

    def rebalanceTree(self, key: KeyType):
        nodelist = list()
        self.__findPath(key, list = nodelist)
        print (len(nodelist))
        if (self.head.left): 
            print (self.head.left.value)
        if (self.head.right):
            print (self.head.right.value)
        
        for x in range(len(nodelist)):
            maxvalue = Decimal(str(nodelist[x].value))
            # check which children the node has
            if nodelist[x].left and nodelist[x].right:
                maxvalue = max(Decimal(str(nodelist[x].value)), Decimal(str(nodelist[x].left.value)), Decimal(str(nodelist[x].right.value)))
            elif nodelist[x].left:
                maxvalue = max(Decimal(str(nodelist[x].value)),  Decimal(str(nodelist[x].left.value)))
            elif nodelist[x].right:
                maxvalue = max(Decimal(str(nodelist[x].value)), Decimal(str(nodelist[x].right.value)))
            
            print(maxvalue)
                
            # if the max between parent and two children is parents value, then no need to update the rest

            # if not, then update parent and keep going through list
            nodelist[x].value = Decimal(str(maxvalue))

        pass

    # this can assume a node is in the tree because we have already found it
    def __findPath(self, key: KeyType, list: list[TreeNode]):
        cur = self.head
        list.insert(0, cur)
        while key != cur.key:
            cur = cur.left if key < cur.key else cur.right
            list.insert(0, cur)
        pass

    def inorderbal(self, key: KeyType, free_space: list):
        self.__inorderbal(self.head, key, free_space=free_space)

    def __inorderbal(self, node: TreeNode, key: KeyType, free_space: list):

        if key < node.key:
            self.__inorderbal(node.left, key, free_space=free_space)
        elif key > node.key:
            self.__inorderbal(node.right, key, free_space=free_space)  

        leftval = -1
        rightval = -1

        if node.left:
            leftval = Decimal(str(node.left.value))
        if node.right:
            rightval = Decimal(str(node.right.value))
        node.value = Decimal(str(max(Decimal(str(leftval)), Decimal(str(rightval)), Decimal(str(free_space[node.key])))))

        return

    # def bal(self, key: KeyType):
    #     self.__bal(self.head, key)

    # def __bal(self, node: TreeNode, key: KeyType):

    #     if node and key < node.key:
    #         self.__bal(node.left, key)
    #     elif node and key > node.key and node.right:
    #         self.__bal(node.right, key)  

    #     if node is None:
    #         return
    #     leftval = -1
    #     rightval = -1

    #     if node.left:
    #         leftval = Decimal(str(node.left.value[1]))
    #     if node.right:
    #         rightval = Decimal(str(node.right.value[1]))
    # #     node.value = (node.value[0], Decimal(str(max(leftval, rightval, node.key))))

    #     return
        
    # def find_best_fit(self, item_size):
    #     current = self.head
    #     best_fit_node = None
        
    #     while current:
    #         if current.left and current.left.value[1] >= item_size:
    #             current = current.left
    #         elif current.key >= item_size:
    #             best_fit_node = current
    #             break
    #         elif current.right and current.right.value[1] >= item_size:
    #             current = current.right
    #         else:
    #             break

    #     return best_fit_node

    def min(self, key: KeyType):
        return self.__min(self.head, key)
    
    def __min(self, node: TreeNode, key: KeyType):
        if node is None:
            return None
        
        diff = node.key - key
        minNode = None
        cur = node
        while cur:
            curDiff = cur.key - key
            if curDiff < diff:
                diff = curDiff
                minNode = cur
                
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                break
        return minNode
            
        
                
            

        

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
    # def remove(self, key: KeyType):
    #     cur = self.head     
    #     prev = None

    #     while key != cur.key:       # find the node that holds the key to remove
    #         prev = cur
    #         if key < cur.key:
    #             cur = cur.left
    #         else:
    #             cur = cur.right

    #     left = cur.left             # cur is node with given key
    #     right = cur.right
        
    #     #Deletion of the key node
    #     if left is None:            # if left is null, cur is now cur.right, key is now gone
    #         cur = right
    #     elif right is None:         # if right is null, cur is now cur.left, key is now gone
    #         cur = left
    #     elif left.rank >= right.rank:   # if there is both children, cur is left if it out ranks right
    #         cur = left
    #     else:                           # else cur is now right 
    #         cur = right

    #     # parent = cur
    #     if self.head.key == key:    # sets head if they are the same
    #         self.head = cur
    #     elif key < prev.key:        # put the child of old cur as the parents left or right
    #         prev.left = cur
    #     else:
    #         prev.right = cur 

    #     while left and right:       # if there is a left and a right we need to readjust the tree
    #         if left.rank >= right.rank:
    #             while left and left.rank >= right.rank:
    #                 prev = left
    #                 left = left.right
    #             prev.right = right                    
    #         else:
    #             while right and left.rank < right.rank:
    #                 prev = right
    #                 right = right.left
    #             prev.left = left
    #     if right:
    #         self.bal(right.key)
    #     if left:
    #         self.bal(left.key)
    #     # return parent
