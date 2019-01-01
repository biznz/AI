from structures import *
from collections import deque
'''
	General Search for use with distinct
	data structures such as LIFOs QUEUEs and HEAPs
	implementing depth first search, breadth first search
	!!! finish comments
'''

queue_type=None


def successor(state,move):
	'''
	from state to problem,
	to transformed problem
	to new state
	'''
	pass

def start():

	queue_type='lifo'
	initial = [[1,2,3,4],[5,6,8,12],[13,9,0,7],[14,11,10,15]]
	goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	operators=('up','down','right','left')
	p = Problem(initial,operators,goal)
	

def run_General_search(problem,q):
	queue_type=q
	return General_Search(problem)

def General_Search(problem):
	'''
		General Search Algorithm
	'''
	nodes = make_queue(make_node(initial_state(problem)))
	while(True):
		if(empty(nodes)):
			return None
		node=remove_nodes(nodes)
		if(node.getState())==goal_test(problem):
			return node
		new_nodes = expand(node,operators(problem))
		nodes = Queue_fn(nodes,new_nodes)


def expand(node,operators):
	'''
		expands new nodes on the search path
	'''
	nodes = []
	for move in operators:
		node = Node(successor(node.state,move))
		nodes.append(node)
	return nodes

def operators(problem):
	'''
		returns the operators 
		on a type of problem
	'''
	return problem.getOperators()

def Queue_fn(enqueue,queue):
	'''
		appends new elements to a queue
	'''
	queue[0].append(enqueue)
	return queue

def remove_nodes(queue):
	'''
		removes nodes from a list according 
		to the list type
		lifo - removes last inserted nodes ( stack )
		fifo - removes first inserted nodes ( queue )
	'''
	node=None
	if(queue[1]=='lifo'):
		node = queue.pop()
	if(queue[1]='fifo'):
		node = queue.popleft()
	return node


def goal_test(problem):
	'''
	returns the end goal on a problem
	'''
	return self.getGoalStateValue()

def initial_state(problem):
	'''
	builds an inital state on the search problem 
	'''
	state = State(problem)
	return state


def make_queue(node):
	'''
		builds a queue
	'''
	queue=None
	if(queue_type=='fifo'):
		queue = deque([node])
		return (queue,queue_type)
	return ([node],queue_type)

def make_node(state):
	'''
		builds a node from a state of a problem
	'''
	return Node(state,depth=0,path=0)

def empty(nodes):
	'''
		returns true if nodes list is empty
	'''
	return (len(nodes)==0)

