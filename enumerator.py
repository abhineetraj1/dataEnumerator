class matrix:
	def add(matrix1, matrix2):
		l_y, l_x,g= len(matrix1), len(matrix1[0]),[]
		if (l_y == l_x):
			nx,ny=0,0
			while(ny < l_y):
				h=[]
				nx=0
				while (nx < l_x):
					h.append(matrix1[ny][nx]+matrix2[ny][nx])
					nx=nx+1
				g.append(h)
				ny=ny+1
			return g
		else:
			return "Matrix type should be square matrix"
	def substract(matrix1, matrix2):
		l_y, l_x,g= len(matrix1), len(matrix1[0]),[]
		if (l_y == l_x):
			nx,ny=0,0
			while(ny < l_y):
				h=[]
				nx=0
				while (nx < l_x):
					h.append(matrix1[ny][nx]-matrix2[ny][nx])
					nx=nx+1
				g.append(h)
				ny=ny+1
			return g
		else:
			return "Matrix type should be square matrix"
	def multiply(matrix1,matrix2):
		if (len(matrix1) == len(matrix1[0])):
			h,g=[],[]
			for i in range(0,len(matrix2[0])):
				h.append(0)
			for i in range(0,len(matrix2[0])):
				g.append(h)
			for i in range(len(matrix1)):
				for j in range(len(matrix2[0])):
					for k in range(len(matrix2)):
						g[i][j] += (matrix1[i][k] * matrix2[k][j])
			return g
		else:
			return "Matrix type should be square matrix"
	def transpose(matrix1):
		N=len(matrix1)
		if (N == len(matrix1[0])):
			matrix2=matrix1
			for i in range(N):
				for j in range(N):
					matrix2[i][j] = matrix1[j][i]
		else:
			return "Matrix type should be square matrix"

class determinant:
	def multiplyNum(deteminant,n):
		for i in deteminant:
			for j in deteminant[i]:
				deteminant[i][j] = deteminant[i][j]*n
		return deteminant
	def addNum(deteminant,n):
		for i in deteminant:
			for j in deteminant[i]:
				deteminant[i][j] = deteminant[i][j]+n
		return deteminant
	def divideNum(deteminant,n):
		for i in deteminant:
			for j in deteminant[i]:
				deteminant[i][j] = deteminant[i][j]/n
		return deteminant
	def substractNum(deteminant,n):
		for i in deteminant:
			for j in deteminant[i]:
				deteminant[i][j] = deteminant[i][j]*n
		return deteminant

class info:
	def lincense():
		print("""Copyright (c) 2022 Abhineet Raj and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
		def credits():
			print("library is created by Abhineet Raj\nGithub= @abhineetraj1")