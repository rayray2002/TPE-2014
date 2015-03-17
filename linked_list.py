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
			
	def output(self):
		pass
			
linkedList = LinkedList()
linkedList.insert(node(2))
linkedList.insert(node(3))
	
print linkedList.head