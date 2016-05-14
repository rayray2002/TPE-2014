def createBTree():
	BTree = [-1,5,4,6,2,-1,-1,8,1,3,-1,-1,-1,-1,7,9]
	return BTree
def search_BST(tree, data):
	pos = 1
	while(pos<len(tree)):
		if tree[pos] > data:
			pos = pos*2
		elif tree[pos] < data:
			pos = pos*2+1
		elif tree[pos] == data:
			return pos
	return 0
def search_DSF(tree, data):
	pos = 1
	while(pos != len(tree)):
		print "pos=", pos
		#pos_old = pos
		if tree[pos] == data:
			return pos
		elif pos*2 < len(tree):
			if tree[pos*2] != -1:
				pos = pos*2
			elif tree[pos*2] == -1:
				pos = pos*2+1
		else:
			pos = pos_old
		pos_old = pos
	return 0
tree = createBTree()
print search_BST(tree, 6)
print search_DSF(tree, 6)