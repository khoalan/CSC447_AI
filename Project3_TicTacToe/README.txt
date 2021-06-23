# CSC447 Assignment 3
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# Readme instruction

-Programming language : Python 3.7.0
-Install python 3
-Create a folder on your computer such as "C:\code\hw03"
-Copy all the files from LanNguyen_CSC447_Project3.Zip to hw03 folder
-Run the script:

	Suppose the main script are in "C:\code\hw03\TTT.py" or ~/code/hw03/TTT.py on Unix-like systems.
	In Windows:
		+Open command line: Start menu -> Run and type "cmd"
		+Change directory to \hw03 folder
		+type : C:\code\hw03\TTT.py nrRows nrCols nrToWin player1Type player2Type depth
	Mac OS X:
		+Open command line: Finder -> Go menu -> Applications -> terminal
		+Change directory to hw03 folder
		+type : python ~/code/hw03/TTT.py nrRows nrCols nrToWin player1Type player2Type depth
	Linux:
		+Open a command prompt
		+Change directory to hw03 folder
		+type : python ~/code/hw03/TTT.py nrRows nrCols nrToWin player1Type player2Type depth

	where
	• player1Type is a string corresponding to ‘human’, ‘random’, or ‘AI’
	• player2Type is a string corresponding to ‘human’, ‘random’, or ‘AI’
	• depth is a positive integer representing the evaluation depth for the alpha-beta search.

-Take move: there will be a index right next to every position, input the index to choose your position.
-For better result, depth should be >=5 in board 3x3. 
-Other notes: the program can be only worked with square board (n x n)