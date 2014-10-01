Autograder
==========
Developing an auto evaluator for python assignments.
	As everything has become automated, we plan to develop an evaluator for Programming Assignments which will reduce the burden 
	of evaluation from instructors.  Right now, we restrict our project to evaluating only python programs. This auto evaluator
	evaluates the code for given inputs, to corresponding outputs in a specific amount of time. It also has the capability 
	of checking against plagiarism. 
	
Scope of our project:
	
	* Evaluation of only python programs.
	
	* We only evaluate specific assignments/programs. (We do not evaluate generic programs like sorting/searching)
	
	* Evaluation of programs against time.
	
	* Checking programs against plagiarism.
	

Example	
	The instructor has to specify what kind of input has to be taken, and the desired output format.
	He is also required to give both an input and an output file to evaluate the program.
		
	Suppose we are evaluating a program to add two numbers, the input file may contain:
	1 0
	-1 2
	100000 399999
	0.5 0.75
	1.a 3
	2 
	/*Empty string*/
			
	Output file:
	1
	1
	499999
	1.25
	Math Error
	Math Error
	Math Error

	Input Format file:
	This file contains the instructions on how the input is supposed to be handled.
	For the above example:
		The program will be invoked with two arguments separated by space
		
	Output Format file:
	This file contains the instructions on what the assignment program should output.
	For the above example:
		The program should give a single number as output. And Math Error on error.
		
	Code under execution
	$:./add 1 2
	$:3
			
			
			
