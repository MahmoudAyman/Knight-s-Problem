
import itertools
from copy import deepcopy

class Board(object):
	"""
	Board is an nxm matrix
	forward_links is a list for tuples connecting start to middle sub-boards
	backward_links is a list of tuples connecting middle sub-boards to the end
	start is a tuple indicating the start location of the tour
	end is a tuple indicating the ending location of the tour
	"""
	index_itr = itertools.count()
	def __init__(self, n, m, start,end, matrix):
		super(Board, self).__init__()
		self.rows = n
		self.cols = m
		self.startPos = start
		self.endPos = end
		self.dataMatrix = deepcopy(matrix)
		self.forward_links = []
		self.backward_links = []
		self.index=next(Board.index_itr)
		self.colorMatrix=[[self.index]*self.cols]*self.rows

	def two_link(self, B):
		'''
		B is the adjacent board to be jointed
		'''
		#print("two_link")
		#print(str(self.index), str(B.index))
		if (self.rows != B.rows):
			print("two link is invalid")
			return None

		self.forward_links+=B.forward_links
		self.backward_links=(B.backward_links)+self.backward_links

		self.forward_links.append(((0,self.cols-2),(B.endPos[0], B.endPos[1]+self.cols)))
		self.backward_links.append(((B.startPos[0],B.startPos[1]+self.cols),(2,self.cols-1)))
		
		for i in range(self.rows):
			self.dataMatrix[i]=self.dataMatrix[i]+B.dataMatrix[i]
			self.colorMatrix[i]=self.colorMatrix[i]+B.colorMatrix[i]
		self.rows+=B.rows
			

	def quad_link(self, B, C, D):
		if (self.cols != C.cols):
			print("quad_link is invalid")
			return None
		self.two_link(B)
		#print(self.dataMatrix)
		#print(self.dataMatrix)
		C.two_link(D)
		# print("b1")
		# print(self)
		# print("b3")
		# print(C)
		self.forward_links+=C.forward_links
		self.backward_links=(C.backward_links)+self.backward_links
		self.forward_links.append(((self.rows-2,0),(C.endPos[0]+self.rows,C.endPos[1])))
		self.backward_links.append(((C.endPos[0]+self.rows,C.endPos[1]),(self.rows -1,2)))
		self.cols+=C.cols
		
		for i in C.dataMatrix:
			#print (i)
			self.dataMatrix.append(i)
		print(self)
		print(self.forward_links)
		print(self.backward_links)

		# print("b1")
		# print(self)
		# print("b3")
		# print(C)



	def __str__(self):
		out=""
		for i in range(self.rows):
			out+=str(self.dataMatrix[i])
			out+=("\n")
		return out


three_by_five = [[1,4,7,10],
				 [12,9,2,5],
				 [3,6,11,8]]

three_by_five2 = [[0,0,0,0],
				 [12,9,2,5],
				 [3,6,11,8]]

b1 = Board(3,4,(0,0),(1,0),three_by_five)
b2 = Board(3,4,(0,0),(1,0),three_by_five)
b3 = Board(3,4,(1,1),(1,0),three_by_five2)
b4 = Board(3,4,(0,0),(1,0),three_by_five2)
#print(b1==b3)
# b1.quad_link(b2,b3,b4)

#b1.quad_link(b2,b3,b4)
#print(b1)
# print(b3)
# print(b1.forward_links)
# print(b1.backward_links)
#print(b1.colorMatrix)
# print(b1.index)
# print(b2.index)
# print(b3.index)
# print(b4.index)
