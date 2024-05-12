import sys
from decimal import *
from zipzip_tree import ZipZipTree, Rank
from hybrid_sort import hybrid


def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    binTree = ZipZipTree(capacity = len(items))
    for i in range(len(free_space)):
        free_space[i] = Decimal(str(free_space[i]))
        
    items = [Decimal(str(i)) for i in items]

    free_space.append(Decimal(str(1)))
    binTree.insert(0, Decimal(str(1)))
    j = 0   # j should be home many bins are in the list could also use getsize()
    for i in range(len(items)):
        # if the item in the list is a value greater than the heads value, insert a new node and place the item there
        keyFind = j
        cur = binTree.head
        # if the biggest bin can not fit the item, insert the item
        if cur and cur.value < items[i]:
            j += 1
            cur = binTree.insert(j, 1 - items[i])
            keyFind = cur.key
            assignment[i] = j
            free_space.append(Decimal(str(1 - items[i])))
        else:
            # find the first bin according to freeSpace
            
            while cur:
                if cur.left and Decimal(str(cur.left.value)) >= Decimal(str(items[i])):
                    cur = cur.left
                elif Decimal(str(free_space[cur.key])) >= Decimal(str(items[i])):
                    break
                elif cur.right and Decimal(str(cur.right.value)) >= Decimal(str(items[i])):
                    cur = cur.right
                else:
                    break
                
            # cur = binTree.inorder(items[i])

            keyFind = cur.key
            free_space[keyFind] = Decimal(str(free_space[keyFind])) - Decimal(str(items[i]))
            cur.value = Decimal(str(free_space[keyFind])) - Decimal(str(items[i]))
            assignment[i] = keyFind
        
        # check cur's value an update it if needed
        maxvalue = Decimal(str(free_space[cur.key]))
        if cur.left and cur.right:
            maxvalue = max(free_space[cur.key], cur.left.value, cur.right.value)
        elif cur.left:
            maxvalue = max(free_space[cur.key], cur.left.value)
        elif cur.right:
            maxvalue = max(free_space[cur.key], cur.right.value)
        cur.value = maxvalue
        # if cur's children has most free space, then done
        # if cur has the biggest space, rebalance the values in the tree
        # rebalance the tree
        binTree.inorderbal(keyFind, free_space)
          
    for i in range(len(free_space)):
        free_space[i] = float(free_space[i])
    




def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    hybrid(items)
    # print(items)
    first_fit(items=items, assignment=assignment, free_space=free_space)
    pass

