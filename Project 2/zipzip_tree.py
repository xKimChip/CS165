# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file
import math
import random


from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass
class Rank:
	geometric_rank: int
	uniform_rank: int

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
        self.head = TreeNode(None, None, -1)
        self.capacity = capacity
        pass

    def get_random_rank(self) -> Rank:
        geometric_rank = random.geometric(1)
        
        uniform_rank = random.randint(0, int(math.log(self.capacity)**3) - 1)

        if random.rand() < 0.5:
            return geometric_rank
        else:
            return uniform_rank
        pass

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        if rank is None:
            rank = get_random_rank 

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

        # Establish horizontal links
        if cur:
            if key < cur.key:
                x.right = cur
            else:
                x.left = cur
        else:  # Reached the end of the list
            x.left, x.right = None, None
            return

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
        pass

    def remove(self, key: KeyType):
        key = self.key
        cur = self.head
        prev = None

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




        pass

    def find(self, key: KeyType) -> ValType:
        pass

    def get_size(self) -> int:
        pass

    def get_height(self) -> int:
        pass

    def get_depth(self, key: KeyType):
        pass

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
