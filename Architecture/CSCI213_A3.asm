# MIPS Assembler Code!!
# CCP - Computer Science 
# CSCI213 - Fall 2023 - Assignment 3
# Written by Diana Mann.
# Last Modified: 27/09/23

# We put our data first... sorry! Habits from C++ and python are hard to break.
.data
# ASCII with NULL terminator, to be C++ string-like.
string1: .asciiz "appledonkeya" 
string2: .asciiz "appledonkeyz"


# The actual code goes in the  text section:
.text
# Let's initialize our registers to zero, it's always good practice:
# We will rely on the argument and values registers for calling our looping function:
li $a0, 0 #$a0 will pass the address of string1.
li $a1, 0 #$a1 will pass the address of string2.
li $t0, 0 # $t0 will be used to hold bytes of string1
li $t1, 0 # $t1 will be used to hold bytes of string2
li $s7, 0 #$s7 will hold the result of the computation as per requirement.
# We pass our function the pointer (memory address) to our strings; so we prepare that first with the first couple of load from memory instructions:
la $a0, string1
la $a1, string2

# Now, time to compare strings in a loop - the function will branch depending on the conditional evaluation of the characters in the strings, one char at the time:
compare_strings:
	# load the first byte to compare:
	lbu $t0, 0($a0) # NOTE!! we're loading the next byte of the address at $a0.
	lbu $t1, 0($a1) # NOTE!! we're loading the next byte of the address at $a1.
	# IF $t0 < $t1, branch to precedes:
	blt $t0, $t1, precedes
	# If $t0 > $t1, branch to succeeds:
	bgt $t0, $t1, succeeds 
	# If we're here, it is assumed we survived the first branch, then, check if we're not at a null (0) character:
	beq $t0, $0, equals # Done comparing, exit loop, if we got this far, we must assume the string is equal.
	# It isn't zero, increment the counter and run the function again.
	addi $a0, $a0, 1 # Increment Register address (next char) for string1
	addi $a1, $a1, 1 # Increment Register address (next char) for string2
	j compare_strings # Jump back to the start of this function.
	
precedes:
	li $s7, -1 #Assign value -1 to $s7
	j done
	
succeeds:
	li $s7, 1 #Assign value 1 to $s7
	j done
	
equals:
	li $s7, 0 # Assign value 0 to $s7.
	j done
	
done:
	# Finished

	