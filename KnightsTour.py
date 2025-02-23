
import pygame, sys
from pygame.locals import *
import numpy as np
from tkinter import *

def inRangeAndEmpty(posx,posy,board,N):
	return (posx < N and posx >= 0 and posy < N and posy >= 0 and board[posx][posy] == 0)

def getAccessibility(x,y,moves,board,N):
	accessibility = 0
	for i in range(8):
		if inRangeAndEmpty(x+moves[i][0],y+moves[i][1],board,N):
			accessibility += 1
	return accessibility

def getNextMoves(move,moves,board,N):
	positionx = move[0]
	positiony = move[1]
	accessibility = 8
	for i in range(8):
		newx = positionx + moves[i][0]
		newy = positiony + moves[i][1]
		newacc = getAccessibility(newx,newy,moves,board,N)
		if inRangeAndEmpty(newx,newy,board,N) and newacc < accessibility:
			move[0] = newx
			move[1] = newy
			accessibility = newacc
	return

def graphicTour(N,L_coor):
	horse = pygame.image.load("knight.png")

	# Initialize window size and title:
	pygame.init()
	window = pygame.display.set_mode((32*N,32*N))
	pygame.display.set_caption("Knight's Tour")
	background = pygame.image.load("chess.png")
	index = 0

	# Text:
	font = pygame.font.SysFont("Ubuntu",16)
	text = []
	surface = []

	while True:
		# Fill background:
		window.blit(background,(0,0))
		if index < N*N:
			window.blit(horse,(L_coor[index][0]*32,L_coor[index][1]*32))
			text.append(font.render(str(index+1),True,(255,255,255)))
			surface.append(text[index].get_rect())
			surface[index].center = (L_coor[index][0]*32+16,L_coor[index][1]*32+16)
			index += 1
		else:
			window.blit(horse,(L_coor[index-1][0]*32,L_coor[index-1][1]*32))
		for x in range(10000000):
			pass
		# Check events on window:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					pygame.quit()
					sys.exit()

		for i in range(index):
			window.blit(text[i],surface[i])

		# Update window:
		pygame.display.update()

def ifSolution(Board,N):
	for i in range(N):
		for j in range(N):
			if Board[i][j] == 0:
				return False
	return True



def createN(root):
	global N
	N = Entry(root)
	N.pack()

def createX(root):
	global X
	X = Entry(root)
	X.pack()
def createY(root):
	global Y
	Y = Entry(root)
	Y.pack()

def packN():
	global root
	global N
	String_N =N.get()
	N = int(String_N)


def packXY():
	global root
	global intx
	global inty
	String_X = X.get()
	String_Y = Y.get()
	intx = int(String_X)
	inty = int(String_Y)

	positionx = intx%N
	positiony = inty%N
	x = positionx
	y = positiony
	moveNumber = 2
	move = [positionx,positiony]
	moves = [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]
	Board = np.zeros([N,N])
	Board[positionx][positiony] = 1
	L = []

	for i in range(N*N):
		move[0] = positionx
		move[1] = positiony
		getNextMoves(move,moves,Board,N)
		positionx = move[0]
		positiony = move[1]
		Board[positionx][positiony] = moveNumber
		moveNumber += 1
	Board[positionx][positiony] -= 1


	sol = ifSolution(Board,N)
	if sol:

		k = 1
		while k <= N*N:
			for i in range(N):
				for j in range(N):
					if Board[i][j] == k:
						L.append([i,j])
						k += 1
		print(Board)
	else:
		moves = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
		Board = np.zeros([N,N])
		positionx = x
		positiony = y
		Board[positionx][positiony] = 1
		L = []
		moveNumber = 2
		move = [positionx,positiony]

		for i in range(N*N):
			move[0] = positionx
			move[1] = positiony
			getNextMoves(move,moves,Board,N)
			positionx = move[0]
			positiony = move[1]
			Board[positionx][positiony] = moveNumber
			moveNumber += 1
		Board[positionx][positiony] -= 1


		sol = ifSolution(Board,N)
		if sol:

			k = 1
			while k <= N*N:
				for i in range(N):
					for j in range(N):
						if Board[i][j] == k:
							L.append([i,j])
							k += 1
			print(Board)
	if len(L) == 0:
		print("Didn't find a solution.")
	print("Knights' positions: ", L)

	if N <= 32 and sol:
		graphicTour(N,L)


def main():
	global root
	global intx
	global inty
	root = Tk()
	root.title("KNIGHT TOUR")
	root.minsize(width = 500 , height = 200)
	Label(root,text="Salam").pack()
	Label(root, text="Please Enter the size of board, N(NxN)(N must be less than 32) : ").pack()
	createN(root)
	buttonN = Button(root,text="Submit",command=packN)
	buttonN.pack()
	Label(root, text="Please Enter the initial position of Knight(x,y) : ").pack()
	Label(root,text="X: ").pack()
	createX(root)
	Label(root,text="Y: ").pack()
	createY(root)
	buttonxy = Button(root,text="Submit",command=packXY)
	buttonxy.pack()



	# N = int(input("Enter N, size of the board (NxN): "))


	root.mainloop()
main()


	
