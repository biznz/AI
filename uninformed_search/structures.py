
class State(object):
	'''
		provides a description of a problem state
	'''
	def __init__(self,problem=None):
		self.value = problem.getStateValue()

	def __str__(self):
		return self.value

	def getNewState(self,move):
		pass

class Problem(object):

	def __init__(self,description,operators,goal):
		self.description=description
		self.operators=operators
		self.goal=goal

	def __str__(self):
		return description

	def getStateValue():
		return self.description

	def getGoalStateValue():
		return self.goal

	def getOperators():
		return self.operators


class Node(object):
	'''
		provides a description of a node in search path
		belonging to a tree or graph
	'''
	def __init__(self,
			state,
			parent=None,
			move=None,depth=-1,path=-1):
		self.state=state
		self.parent_node=parent_node
		self.move=move
		self.depth=depth
		self.path_cost=path_cost

	def __str__(self):
		return self.state

	def setState(self,STATE):
		self.state = state

	def getState(self):
		return self.state

	def setParent(self,PARENT):
		self.parent_node=parent_node

	def getParent(self):
		return self.parent

	def setMove(self,MOVE):
		self.move = move

	def getMove(self):
		return self.move

	def setDepth(self,depth):
		self.depth = depth

	def getDepth(self):
		return self.depth

	def setPathCost(self,path_cost):
		self.path_cost=path_cost

	def getPathCost(self):
		return self.path_cost



class 15PuzzleState(State):

	def __init__(self,problem=None):
		super.__init__()

	def __str__(self):
		return self.value

	def getNewStates(self,move):
		if(move=='up'):

		if(move=='down'):

		if(move=='right'):

		if(move=='left'):

	def getNullYPosition(self):
		pass

	def getNullXPosition(self):
		pass