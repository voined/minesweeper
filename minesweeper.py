import pygame
import random


pygame.init()
pygame.font.init()
pygame.display.set_caption('Minesweeper')

clock = pygame.time.Clock()

size = 10

screen = 700


win = pygame.display.set_mode((screen, screen))

surroundingX = 0
board = []


def build_board(rows, cols):
	global board
	global surroundingX
	for i in range(rows):
		board.append([])
		for j in range(cols):

			board[i].append(['O', False])

	for i in range(11):
		random_numi = random.randint(0, 9)
		random_numj = random.randint(0, 9)

		board[random_numi][random_numj] = ['X', False]

			






	for i in range(rows):
		for j in range(cols):
			surroundingX = 0


			if i*(screen/size) == 0 and j*(screen/size) != 0 and j*(screen/size) != len(board)*(screen/size)-(screen/size):
				type_ = 'top'
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1
				if board[i + 1][j + 1][0] == 'X': #BOTTOM-RIGHT
					surroundingX += 1
				if board[i + 1][j - 1][0] == 'X': #BOTTOM-LEFT
					surroundingX += 1
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1



			elif i*(screen/size) == len(board)*(screen/size)-(screen/size) and j*(screen/size) != 0 and j*(screen/size) != len(board)*(screen/size)-(screen/size):
				type_ = 'bottom'
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j + 1][0] == 'X': #TOP-RIGHT
					surroundingX += 1
				if board[i - 1][j - 1][0] == 'X': #TOP-LEFT
					surroundingX += 1


			elif j*(screen/size) == len(board)*(screen/size)-(screen/size) and i*(screen/size) != 0 and i*(screen/size) != len(board)*(screen/size)-(screen/size):
				type_ = 'right'
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1			
				if board[i + 1][j - 1][0] == 'X': #BOTTOM-LEFT
					surroundingX += 1
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j - 1][0] == 'X': #TOP-LEFT
					surroundingX += 1

			elif j*(screen/size) == 0 and i*(screen/size) != 0 and i*(screen/size) != len(board)*(screen/size)-(screen/size):	
				type_ = 'left'		
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j + 1][0] == 'X': #TOP-RIGHT
					surroundingX += 1
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1
				if board[i + 1][j + 1][0] == 'X': #BOTTOM-RIGHT
					surroundingX += 1


			elif j*(screen/size) == 0 and i*(screen/size) == len(board)*(screen/size)-(screen/size):
				type_ = 'bottomleft'
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j + 1][0] == 'X': #TOP-RIGHT
					surroundingX += 1
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1


			elif j*(screen/size) == len(board[0])*(screen/size)-(screen/size) and i*(screen/size) == 0:
				type_ = 'topright'
				if board[i + 1][j - 1][0] == 'X': #BOTTOM-LEFT
					surroundingX += 1
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1


			elif j*(screen/size) == len(board[0])*(screen/size)-(screen/size) and i*(screen/size) == len(board)*(screen/size)-(screen/size):
				type_ = 'bottomright'
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j - 1][0] == 'X': #TOP-LEFT
					surroundingX += 1
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1


			elif j * (screen/size) == 0 and i * (screen/size) == 0:
				type_ = 'topleft'
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1
				if board[i + 1][j + 1][0] == 'X': #BOTTOM-RIGHT
					surroundingX += 1




			else:
				type_ = 'normal'
				if board[i][j + 1][0] == 'X': #RIGHT
					surroundingX += 1
				if board[i][j - 1][0] == 'X': #LEFT
					surroundingX += 1
				if board[i + 1][j + 1][0] == 'X': #BOTTOM-RIGHT
					surroundingX += 1
				if board[i + 1][j - 1][0] == 'X': #BOTTOM-LEFT
					surroundingX += 1
				if board[i + 1][j][0] == 'X': #BOTTOM
					surroundingX += 1
				if board[i - 1][j][0] == 'X': #TOP
					surroundingX += 1
				if board[i - 1][j+ 1][0] == 'X': #TOP-RIGHT
					surroundingX += 1
				if board[i - 1][j - 1][0] == 'X': #TOP-LEFT
					surroundingX += 1

			if board[i][j][0] == 'O':
				board[i][j].append(surroundingX)
			else:
				board[i][j].append(-1)

			if board[i][j][2] == 0:
				board[i][j][2] = ''



			board[i][j].append(type_)






build_board(size, size)


block_font = pygame.font.SysFont('8-Bit-Madness', 30)
gameover_font = pygame.font.SysFont('8-Bit-Madness', 60)

gameover = False


def block_check(x, y):
	global surroundingX
	global board
	global gameover

	x = round(x)
	y = round(y)

	surroundingX = 0
	mouse_presses = pygame.mouse.get_pressed()

	if mouse_presses[0]: #LEFT CLICK
		print(round((screen/size)))
		if board[y//round((screen/size))][x//round((screen/size))][0] == 'X':
			pygame.draw.rect(win, (255, 0, 0), ((x//(screen/size))*(screen/size), (y//(screen/size))*(screen/size), (screen/size), (screen/size)))
			board[y//round((screen/size))][x//round((screen/size))][1] = True
			surroundingX = -1

			gameover = True


		elif board[y//round((screen/size))][x//round((screen/size))][0] == 'O':
			pygame.draw.rect(win, (255, 255, 255), ((x//(screen/size))*(screen/size), (y//(screen/size))*(screen/size), (screen/size), (screen/size)))
			board[y//round((screen/size))][x//round((screen/size))][1] = True



	
			block_text = block_font.render(str(board[y//round((screen/size))][x//round((screen/size))][2]), False, (0, 0, 0))
			win.blit(block_text, ((x//(screen/size))*(screen/size) + 25, (y//(screen/size))*(screen/size) + 25))






	elif mouse_presses[2] and board[y//round((screen/size))][x//round((screen/size))][1] == False: #RIGHT CLICK
		pygame.draw.rect(win, (0, 255, 0), ((x//(screen/size))*(screen/size) + 15, (y//(screen/size))*(screen/size) + 15, 40, 40))




def refreshwindow():

	block_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j][1] == True and board[i][j][2] == '':
				
				if board[i][j][3] == 'normal':
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size) + (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-RIGHT
					block_check(j * (screen/size) + (screen/size), i * (screen/size) - (screen/size)) #TOP-RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size) - (screen/size)) #TOP-LEFT
					block_check(j * (screen/size) - (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-LEFT

				elif board[i][j][3] == 'top':
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM
					block_check(j * (screen/size) + (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-LEFT

				elif board[i][j][3] == 'bottom':
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size) + (screen/size), i * (screen/size) - (screen/size)) #TOP-RIGHT
					block_check(j * (screen/size) - (screen/size), i * (screen/size) - (screen/size)) #TOP-LEFT

				elif board[i][j][3] == 'left':
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size) + (screen/size), i * (screen/size) - (screen/size)) #TOP-RIGHT
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM
					block_check(j * (screen/size) + (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-RIGHT

				elif board[i][j][3] == 'right':
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM
					block_check(j * (screen/size) - (screen/size), i * (screen/size) - (screen/size)) #TOP-LEFT
					block_check(j * (screen/size) - (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-LEFT

				elif board[i][j][3] == 'bottomleft':
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size) + (screen/size), i * (screen/size) - (screen/size)) #TOP-RIGHT
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT

				elif board[i][j][3] == 'bottomright':
					block_check(j * (screen/size), i * (screen/size) - (screen/size)) #TOP
					block_check(j * (screen/size) - (screen/size), i * (screen/size) - (screen/size)) #TOP-LEFT
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT

				elif board[i][j][3] == 'topright':
					block_check(j * (screen/size) - (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-LEFT
					block_check(j * (screen/size) - (screen/size), i * (screen/size)) #LEFT
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM

				elif board[i][j][3] == 'topleft':
					block_check(j * (screen/size) + (screen/size), i * (screen/size)) #RIGHT
					block_check(j * (screen/size), i * (screen/size) + (screen/size)) #BOTTOM
					block_check(j * (screen/size) + (screen/size), i * (screen/size) + (screen/size)) #BOTTOM-RIGHT


	for i in range(len(board)):
		pygame.draw.line(win, (150,150,150), (0, i * (screen/size)-2), (screen, i * (screen/size)-2), width = 2)
		for j in range(len(board[0])):
			pygame.draw.line(win, (150,150,150), (j * (screen/size)-2, 0), (j * (screen/size)-2, screen), width = 2)



	if gameover:
		pygame.draw.rect(win, (100, 110, 120), (80, 172, 550, 90))
		gameover_text = gameover_font.render('               You lost', False, (255, 0, 0))
		win.blit(gameover_text, (100, 200))	



	pygame.display.update()



run = True
while run:
	clock.tick(300)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	refreshwindow()



pygame.quit()