"""
Knight's Problem divide and conquer algorithm
"""
from classDef import *
from baseCases import *
import math
		

def lookUp(n,m, mode):
	'''
	takes a dimensions (n,m) and returns a solveBoardd matrix of the same size
	returns nxm matrix
	'''
	if not((n,m) in base_cases.keys()):
		print("Solution not found")
		return None
	else:
		if (mode=='c'):
			data = base_cases[(n,m)][0]
		elif (mode=='s'):
			data = base_cases[(n,m)][1]
		elif (mode=='d'):
			data = base_cases[(n,m)][2]
		else:
			print("mode is undefined")
			return None
		#print(data)
		start=(0,0)
		end=(0,0)
		for i in range(0,n-1):
			for j in range(0,m-1):
				if (data[i][j] == 1):
					start=(i,j)
					pass
				elif (data[i][j]==(n*m)):
					end=(i,j)
					pass

		return (Board(n,m,start,end,data))


def solveBoard(n,m):
	'''
	takes dimensions (n, m) and returns a knight's tour on a board of size n*m
	returns: matrix
	'''
	if ((n<=10) and (m<=10)):
		temp = lookUp(n,m,'s')
		if (temp==None):
			print("Solution not found.")
			return None
		else:
			return temp
	
	elif ((n==3) and (m>10)):
		k = ((m-7)%4) + 7
		#print(k)
		aux_matrix=lookUp(3,4,'s')
		if (aux_matrix==None):
			print("Solution not found")
			return None
		else:
			for i in range(1,(m-k)/4):
				aux_matrix.two_link(lookUp(3,4,'s'))
			temp = solveBoard(3,k)
			if (temp==None):
				print("solution not found")
				return None
			else:
				return ((temp.two_link(aux_matrix)))

	elif ((n==4) and (m>10)):
		k = ((m-6)%5) + 6
		aux_matrix=lookUp(4,5,'s')
		for i in range(1,(m-k)/5):
			aux_matrix = combine(aux_matrix, lookUp(4,5,'s'))
		return (combine(solveBoard(4,k),aux_matrix))

	elif ((5<=n<=10) and (m>10)):
		m1 = (math.floor(m/4)*2)+(m%2)
		m2 = m-m1
		return (combine(solveBoard(n,m1), solveBoard(n,m2)))
	elif ((5>10) and (m>10)):
		n1 = (math.floor(n/4)*2)+(n%2)
		n2 = n-n1
		m1 = (math.floor(m/4)*2)+(m%2)
		m2 = m-m1
		return (combine(combine(solveBoard(n1,m1), solveBoard(n1,m2)), combine(solveBoard(n2,m1),solveBoard(n2,m2))))


sol = solveBoard(3,8)
print(sol)
# temp = lookUp(4,5,'s')
# print(temp)
# print(temp.endPos)
# if __name__ == "__main__":

# 	n = int(input("Enter value of n: "))
# 	m = int(input("Enter value of m: "))

# 	solution  = solveBoard(n,m)
# 	print (solution)