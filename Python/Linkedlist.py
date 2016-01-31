class Node(object):

	def __init__(self,value = None,next_node = None):
		self.value = value
		self.next_node = next_node


	def get_data(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, next_new):
		self.next_node = next_new	

	

class LinkList(object):
	def __init__(self,head =None):
		self.head = head

	def insert(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def length(self):
		count = 0
		nextnode = self.head
		while (nextnode != None):
			count += 1
			nextnode = nextnode.get_next()

		return count

	def search(self,data):
		nextnode = self.head
		while (nextnode != None):
			if (nextnode.get_data() == data):
				return True
			else:
				nextnode = nextnode.get_next()
		return False

	def delete(self,data):
		firstNode = self.head
		nextNode = self.head.get_next()
		if (firstNode.get_data() == data):
			self.head = firstNode.get_next()
		else:
			while (nextNode != None):
				if (nextNode.get_data() == data):
					firstNode.next_node = nextNode.get_next()	
					break
				else:
					firstNode = nextNode
					nextNode = nextNode.get_next()	 



					
					

Link = LinkList()
Link.insert(3)
Link.insert(4)
Link.insert(5)
Link.insert(6)

Link.delete(0)

print Link.search(0)
print Link.length()



