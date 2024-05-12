# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

import sys
import random
from math import log
from collections import namedtuple
from math import fabs
from decimal import *

from typing import TypeVar
from dataclasses import dataclass

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
Rank = namedtuple("Rank", ["geometric_rank", "uniform_rank"])

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

        x = TreeNode(key, val, rank)  # Create the new node
        cur = self.head
        prev = None

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
        
        # increase size for new node inserted
        self.size += 1
        
        # Establish horizontal links
        if cur:
            if key < cur.key:
                x.right = cur
            else:
                x.left = cur
        else:  # Reached the end of the list
            x.left, x.right = None, None
            return x

        # Fix vertical links from bottom up
        prev = x
        while cur:
            fix = prev
            if cur.key < key:
                while cur and cur.key < key:
                    prev, cur = cur, cur.right
            else:
                while cur and cur.key > key:
                    prev, cur = cur, cur.left

            if (fix.key > key) or (fix == x and prev.key > key):
                fix.left = cur
            else:
                fix.right = cur  
        return x

    # removes item with parameter key from tree.
    # you can assume that the item exists in the tree.
    def remove(self, key: KeyType):
        #Establish bases, cur = tree traverser, prev is the parent of cur
        # key     #May not need, key is nodes key, self.key is a key from tree but isnt real
        cur = self.head
        prev = None

        # Find the key iteratively
        while key != cur.key:
            prev = cur
            cur = cur.left if key < cur.key else cur.right
        left = cur.left
        right = cur.right

        if not left:
            cur = right
        elif not right:
            cur = left
        elif left.rank >= right.rank:
            cur = left
        else:
            cur = right

        # if the removal node is the root of the tree
        if key == self.head.key:
            self.head = cur
        # if key is less than parent, parents left is cur
        elif key < prev.key:
            prev.left = cur
        else:
            prev.right = cur

        #Fix
        while left and right:
            if left.rank >= right.rank:
                while not left or left.rank < right.rank:
                    prev = left
                    left = left.right
                prev.right = right
            else:
                while not right or left.rank >= right.rank:
                    prev = right
                    right = right.left
                prev.left = left
        self.size -= 1
        pass
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
        
        for x in range(len(nodelist)):
            maxvalue = nodelist[x].value
            # check which children the node has
            if nodelist[x].left and nodelist[x].right:
                maxvalue = max(nodelist[x].value, nodelist[x].left.value, nodelist[x].right.value)
            elif nodelist[x].left:
                maxvalue = max(nodelist[x].value,  nodelist[x].left.value)
            elif nodelist[x].right:
                maxvalue = max(nodelist[x].value, nodelist[x].right.value)
                
            # if the max between parent and two children is parents value, then no need to update the rest
            if maxvalue == nodelist[x].value:
                break
            # if not, then update parent and keep going through list
            else:
                nodelist[x].value = Decimal(str(maxvalue))
        pass

    # this can assume a node is in the tree because we have already found it
    def __findPath(self, key: KeyType, list: list[TreeNode]):
        cur = self.head
        while key != cur.key:
            list.insert(0, cur)
            cur = cur.left if key < cur.key else cur.right
        pass

        
    
	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
