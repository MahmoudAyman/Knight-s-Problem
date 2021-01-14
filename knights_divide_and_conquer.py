"""
Knight's Problem divide and conquer algorithm
"""
import math
0
def lookUp(n,m):
	'''
	takes a dimensions (n,m) and returns a solved matrix of the same size
	returns nxm matrix
	'''
	pass

def combine(m1, m2):
	'''
	takes two matrices (m1 and m2)
	returns a matrix (m_combined) which is a combined and index-adjusted matrix
	of m1 and m2 combined
	'''
	def rotate(m):
		'''
		takes a matrix and returns a rotated version m_rotated
		returns: matrix 
		'''
		pass
	pass


def solveBoard(n,m):
	'''
	takes dimensions (n, m) and returns a knight's tour on a board of size n*m
	returns: matrix
	'''
	if ((n<=1) and (m<=10)):
		return (lookUp(n,m))
	
	elif ((n==3) and (m>10)):
		k = ((m-7)%4) + 7
		aux_matrix=lookUp(3,4)
		for i in xrange(1,(m-k)/4):
			aux_matrix = combine(aux_matrix, lookUp(3,4))
		return (combine(solve(3,k),aux_matrix))

	elif ((n==4) and (m>10)):
		k = ((m-6)%5) + 6
		aux_matrix=lookUp(4,5)
		for i in xrange(1,(m-k)/5):
			aux_matrix = combine(aux_matrix, lookUp(4,5))
		return (combine(solve(3,k),aux_matrix))

	elif ((5<=n<=10) and (m>10)):
		m1 = (math.floor(m/4)*2)+(m%2)
		m2 = m-m1
		return (combine(solve(n,m1), solve(n,m2)))
	elif ((5>10) and (m>10)):
		n1 = (math.floor(m/4)*2)+(n%2)
		n2 = n-n1
		m1 = (math.floor(m/4)*2)+(m%2)
		m2 = m-m1




