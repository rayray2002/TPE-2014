class node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
	def __str__(self):
		return str(self.data)
		
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		
	def insert(self, node):
		if not self.head:
			self.head = node
		else:
			# set new nodes pointer to old head
			node.nextNode = self.head
			# reset head to new node
			self.head = node
			
	def search(self, lList, Node):
		if self.head == Node:
			return self.head
		else:
			if lList.head.nextNode:
				self.search(linkedList(lList.head.nextNode), Node)
			else:
				raise ValueError("Node not in Linked List")
				
	def size(self):
		current = self.head
		size = 0
		while current is not None:
			size += 1
			current = current.nextNode
			return size
		
	def output(self):
		while self.head is not None:
			print self.head
			self.head = self.head.nextNode
			
linkedList = LinkedList()
linkedList.insert(node(2))
linkedList.insert(node(3))
linkedList.insert(node(1))
linkedList.output()