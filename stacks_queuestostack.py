class Queue2Stacks(object):
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def enqueue(self, element):
		size = len(self.stack2)
		for i in range(size):
			self.stack1.append(self.stack2.pop())
		self.stack1.append(element)
	def dequeue(self):
		size = len(self.stack1)
		for i in range(size):
			self.stack2.append(self.stack1.pop())		
		return self.stack2.pop()
				
class Queue2Stacks_moreEfficient(object):
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def enqueue(self, element):
		self.stack1.append(element)
	def dequeue(self):
		size1 = len(self.stack1)
		size2 = len(self.stack2)
		if size2 == 0:
			if size1 == 0:
				return None
			for i in range(size1):
				self.stack2.append(self.stack1.pop())		
		return self.stack2.pop()