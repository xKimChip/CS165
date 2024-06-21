from my_float import Float
from hybrid_sort import hybrid
from zipzip_tree import ZipZipTree, TreeNode


def best_fit(items: list[float], assignment: list[int], free_space: list[float]) -> None:
	zipzip = ZipZipTree(len(items))

	def find(cur: TreeNode, item: Float) -> TreeNode:
		if cur == None: return None
		if cur.key == item: return cur # perfect fit
		res = find((cur.right if cur.key < item else cur.left), item)
		if res == None and cur.key - item >= 0: return cur
		else: return res

	for i, item in enumerate(items):
		item = Float(item)
		node = find(zipzip.head, item)
		if node == None or node.key < item:
			zipzip.insert(1 - item , len(free_space))
			assignment[i] = len(free_space)
			free_space.append(1 - item)
		else:
			new_cap = node.key - item
			bin_num = node.value
			zipzip.remove(node.key)
			if not (Float(new_cap) == 0): zipzip.insert(new_cap, bin_num)
			assignment[i] = bin_num
			free_space[bin_num] -= item

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]) -> None:
	hybrid(items)
	best_fit(items, assignment, free_space)
