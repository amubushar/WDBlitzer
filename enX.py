import pyautogui as pxl
import os
import time
import copy

#Left_WinCorner = [420,160]
Left_WinCorner = [87,136]
X_base = 60
X_seperation = 105
Y_base = 305
Y_seperation = 105
Mspeed = 0.5
WordsX = 75

clear = lambda: os.system('cls')

arraySize = 4
m = []
wordsList = []
matrix = []

def Console():
	print('Please enter the grid in left to right matrix order:')
	grid = list(input().upper())
	start_time = time.time()
	clear()	
	global matrix
	matrix = copy.deepcopy(chunks(grid, arraySize))
	global pxl
	global wordsList
	wordsList = []
	allStarts()	
	abvList = [w for w in wordsList if len(w)>1]
	abvList.sort(key=len, reverse=True)
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
		for row in matrix]))
	print("\n")
	for xla in abvList:
		print(xla)
	print("\nWords: ", len(abvList), "\n")
	print("Time taken: ", time.time() - start_time)	
	abvList = abvList[0:WordsX]
	pxl.click(Left_WinCorner[0],Left_WinCorner[1])
	for m in abvList:
		t = m.split("_")[1]
		al = [t[i:i+2] for i in range(0, len(t), 2)]
		for steps in al:
			pxl.moveTo(X_base + Left_WinCorner[0] + (int(steps[1])-1)*X_seperation,Y_base + Left_WinCorner[1] + (int(steps[0])-1)*Y_seperation)
			pxl.mouseDown()
		pxl.mouseUp()
	Console();
	return

def wordsBy( str ):
	filteredList = [x for x in m if x.startswith(str)]   
	return filteredList
	
def chunks(l, n):
	return [l[i:i+n] for i in range(0, len(l), n)]
	
def get_digit(number, n):
	return int(number) // 10**n % 10
	
def allStarts():
	visited = [[0 for x in range(arraySize)] for y in range(arraySize)]
	for i in range(arraySize):
		for j in range(arraySize):
			file = open(matrix[i][j].lower() + "_dict.txt","r")
			z = set(file.read().split("\n"))
			global m
			m = z
			zr = 0
			path = []
			enumF("", i, j, zr, path)
 
def enumF(stre, i, j, visited, pathX):
	path = copy.deepcopy(pathX)
	if (i < 0 or j < 0 or i > (arraySize - 1) or j > (arraySize - 1) or get_digit(bin(visited)[2:],((i*4+j))) == 1 ):	
		pass
	else:
		visited += 1 << (i*4 + j)
		path.append(str(i+1) + str(j+1))
		comb = stre + matrix[i][j]
		cstr = wordsBy(comb)
		if (len(cstr) != 0):
			if comb in cstr:
				wordsList.append(comb + "_" + "".join(path))
				m.remove(comb)
			enumF(comb,i + 1,j,visited,path) #down
			enumF(comb,i - 1,j,visited,path)	#up
			enumF(comb,i,j + 1,visited,path)	#right
			enumF(comb,i,j - 1,visited,path) #left
			enumF(comb,i + 1,j + 1,visited,path) #down right
			enumF(comb,i - 1,j + 1,visited,path) #up right
			enumF(comb,i + 1,j - 1,visited,path) #down left
			enumF(comb,i - 1,j - 1,visited,path) #up left
	return
clear()
Console()