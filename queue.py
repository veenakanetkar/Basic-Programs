queue = []
def push(queue, item):
	
		queue.insert(0,item)
		return queue
def pop(queue):
	return queue.pop()
		
push(queue,1)
push(queue,2)
push(queue,3)
print(queue)
print(pop(queue))
print(pop(queue))
print(pop(queue))
print(queue)
