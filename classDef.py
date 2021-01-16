
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
		#print(self.index,B.index)

		if (self.rows != B.rows):
			print("two link is invalid")
			# print(self.rows, B.rows)
			# print(B.dataMatrix)
			# print(self)
			# print(B)
			return None

		if(B.rows==4):
			if ((self.cols%5)==0):
				self.forward_links.append([1,self.cols-1,B.endPos[0],B.endPos[1]+self.cols])
				self.forward_links.append([2,self.cols-1,B.endPos[0]+3,B.endPos[1]+self.cols])

				self.backward_links.append([B.startPos[0]+1,B.startPos[1]+self.cols,self.rows-1,self.cols-2])
				self.backward_links.append([B.startPos[0],B.startPos[1]+self.cols,0,self.cols-2])
			else:
				# print("innn")
				# print(self.startPos)
				self.forward_links.append([self.startPos[0],self.startPos[1],B.startPos[0]+1,B.startPos[1]+self.cols])
				self.backward_links.append([B.startPos[0],B.startPos[1]+self.cols,self.endPos[0],self.endPos[1]])

		else :
			#self.forward_links.append(((0,self.cols-2),(B.endPos[0], B.endPos[1]+self.cols)))
			self.forward_links.append([0,self.cols-2,B.endPos[0], B.endPos[1]+self.cols])
			#self.backward_links.append(((B.startPos[0],B.startPos[1]+self.cols),(2,self.cols-1)))
			self.backward_links.append([B.startPos[0],B.startPos[1]+self.cols,2,self.cols-1])

		for i in B.forward_links:
			i[1]+=self.cols
			i[3]+=self.cols
		for i in B.backward_links:
			i[1]+=self.cols
			i[3]+=self.cols

		self.forward_links+=B.forward_links
		self.backward_links=(B.backward_links)+self.backward_links
		
		for i in range(self.rows):
			self.dataMatrix[i]=self.dataMatrix[i]+B.dataMatrix[i]
			self.colorMatrix[i]=self.colorMatrix[i]+B.colorMatrix[i]
		self.cols+=B.cols

		if (self.rows == 4) and (self.cols!=5):
			self.startPos=(self.startPos[0]+2,self.startPos[1]+1)
			self.endPos=(self.endPos[0]+1,self.endPos[1]+2)



			

	def quad_link(self, B, C, D):
		if (self.cols != C.cols):
			print("quad_link is invalid")
			return None
		self.two_link(B)
		C.transpose()
		C.two_link(D)
		
		self.forward_links.append([self.rows-2,0,C.endPos[0]+self.rows,C.endPos[1]])
		self.backward_links.append([C.startPos[0]+self.rows,C.startPos[1],self.rows -1,2])

		for i in C.forward_links:
			i[0]+=self.rows
			i[2]+=self.rows
		for i in C.backward_links:
			i[0]+=self.rows
			i[2]+=self.rows

		self.forward_links+=C.forward_links
		self.backward_links=(C.backward_links)+self.backward_links
		
		for i in C.dataMatrix:
			#print (i)
			self.dataMatrix.append(i)
		self.rows+=C.rows

	def transpose(self):
		data = self.dataMatrix
		data_transposed = list(map(list, zip(*data)))
		self.dataMatrix = deepcopy(data_transposed)
		cols = self.cols
		self.cols = self.rows
		self.rows = cols
		st = self.startPos
		self.startPos = (st[1],st[0])
		en = self.endPos
		self.endPos = (en[1],en[0])



	def __str__(self):
		out=""
		# out+=str([i for i in range(0,self.cols)])
		# out+=("\n")
		# out+=str(["=" for i in range(0,self.cols)])
		# out+=("\n")
		for i in range(self.rows):
			#out+=str(i)+": "
			out+=str(self.dataMatrix[i])
			out+=("\n")
		return out



