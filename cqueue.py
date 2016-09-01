class Queue:
	
	def __init__(self):
		self.queue = []
		
	def push(self,item):
		 self.queue.insert(0,item)
		
	def pop(self):
		return self.queue.pop()
	
	def __str__(self):
		return str(self.queue)
queue = Queue()		
queue.push(1)
queue.push(2)
queue.push(3)
print(queue)
queue.pop()
queue.pop()
queue.pop()
print(queue)      

	
 

		

		
	
	
		
				