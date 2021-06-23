# CSC447 Assignment 2
# Instructor: Dr.Plaku
# Author : Lan Nguyen
# StudentID: 5152815
# Readme instruction

-Programming language : Python 3.7.0
-Install python 3
-Create a folder on your computer such as "C:\code\hw02"
-Copy all the files from LanNguyen_CSC447_Project2.Zip to hw02 folder
-Run the script:
	Suppose the main script are in "C:\code\hw02\GridSearch.py" or ~/code/hw02/GridSearch.py on Unix-like systems.
	In Windows:
		+Open command line: Start menu -> Run and type "cmd"
		+Change directory to \hw02 folder
		+type : C:\code\hw02\GridSearch.py method grid.txt rstart cstart rend cend path.txt
	Mac OS X:
		+Open command line: Finder -> Go menu -> Applications -> terminal
		+Change directory to hw02 folder
		+type : python ~/code/hw02/GridSearch.py method grid.txt rstart cstart rend cend path.txt
	Linux:
		+Open a command prompt
		+Change directory to hw02 folder
		+type : python ~/code/hw02/GridSearch.py method grid.txt rstart cstart rend cend path.txt
	where: 
		method is the name of the search method 
		grid.txt is the name of the file with the grid
		rstart is the row index of the start position 
		cstart is the column index of the start position
		rend is the row index of the end position
		cend is the column index of the end position
		path.txt is the name of path file consist of row and collumn index.
-Then visualize the grid and the solution via support code.
-I have created 2 grid files named : grid.txt and grid2.txt for testing purpose.
-See the SampleSolution file for "sample solution"