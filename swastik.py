def swastik(row,col):
    """Prints Swastik patterm
    Make sure to give ODD rows and column to print perfect Swastik pattern

    Args:
        row ([type]): Value must be a ODD number
        col ([type]): Value must be a ODD number
    """    
	for i in range(row):
		for j in range(col):
			if(i < row // 2):
				if (j < col // 2):
					if (j == 0):
						print("*", end = "")
					else:
						print(" ", end = " ")
				elif (j == col // 2):
					print(" *", end = "")
				else:
					if (i == 0):
						print(" *", end = "")		
			elif (i == row // 2):
				print("* ", end = "")
			else:
				if (j == col // 2 or j == col - 1):
					print("* ", end = "")
				elif (i == row - 1):
					if (j <= col // 2 or j == col - 1):
						print("* ", end = "")
					else:
						print(" ", end = " ")
				else:
					print(" ", end = " ")
		print()	
#Make sure to provide odd number to print perfect swastika
row = int(input('Enter row number for swastik : '))
col = int(input('Enter column for swastika : '))
swastik(row, col)