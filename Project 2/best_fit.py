
from hybrid_sort import hybrid
from zipzip_tree import ZipZipTree, Rank
from decimal import *
from collections import namedtuple


tup = namedtuple('val', ['index', 'maxval'])

def best_fit2(items: list[float], assignment: list[int], free_space: list[float]):
    bin = ZipZipTree(capacity = len(items))
    items = [Decimal(str(i)) for i in items]

        
    free_space.append(Decimal(str(1)))
    bin.insert(Decimal(str(1)), tup(0, Decimal(str(1))))
    freesize = 0

    for i in range(len(items)):
        cur = bin.head

        if cur and cur.value[1] < items[i]:
            freesize += 1
            cur = bin.insert(Decimal(str(1 - items[i])), tup(freesize, Decimal(str(1)) - items[i]))
            assignment[i] = freesize
            free_space.append(Decimal(str(1 - items[i])))
        else:
        
            while True:
                if cur.left and cur.left.key >=  items[i]:
                    cur = cur.left
                elif cur.key >= items[i]:
                    break
                elif cur.right and cur.right.key >= items[i]:
                    cur = cur.right
                else:
                     break
            # newcur = bin.remove(cur.key)
            bin.remove(cur.key)
            # cur = newcur
            cur.key = cur.key - items[i]
            cur = bin.insert(Decimal(str(cur.key)), tup(cur.value[0], cur.key))
            assignment[i] = cur.value[0]
            free_space[cur.value[0]] -= items[i]
        
        leftval = -1
        rightval = -1

        if cur.left:
            leftval = Decimal(str(cur.left.value[1]))
        if cur.right:
            rightval = Decimal(str(cur.right.value[1]))
        cur.value = tup(cur.value[0],Decimal(str(max(Decimal(str(leftval)), Decimal(str(rightval)), Decimal(str(cur.key))))))

        bin.balBF(cur.key)
          
    for i in range(len(free_space)):
        free_space[i] = float(free_space[i])

    pass

def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    # Initialize the tree with a capacity based on the number of items
    tree = ZipZipTree(capacity=len(items))
    items = [Decimal(str(i)) for i in items]
    
    # Start with the first bin
    bin_index = 0
    tree.insert(Decimal(str(1)), bin_index)  # Insert the first bin with 1.0 space
    free_space.append(Decimal(str(1)))       # Initialize free space for the first bin
    
    for i, item in enumerate(items):
        # Find the best bin with the minimum space that can fit the item
        node = tree.find_best_fit(item)
        
        if node is None:
            # No bin can accommodate the item, create a new bin
            bin_index += 1
            tree.insert(1 - item, bin_index)
            free_space.append(1 - item)
            assignment[i] = bin_index
            # tree.balBF(new.key)
        else:
            # Fit the item in the found bin
            new_free_space = node.key - item
            node_val = node.value
            tree.remove(node.key)  # Remove the old node
            if new_free_space > 0:
                tree.insert(new_free_space, node_val)  # Insert the updated free space
            free_space[node_val] = new_free_space
            assignment[i] = node_val
            # if old:
                # tree.balBF(old.key)

    for i in range(len(free_space)):
        free_space[i] = float(free_space[i])
            

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    hybrid(items)
    best_fit(items=items,assignment=assignment,free_space=free_space)
    pass

