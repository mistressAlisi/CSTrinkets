# MIPS Assembler Code!!
# CCP - Computer Science 
# CSCI213 - Fall 2023 - Assignment 4
# Written by Diana Mann.
# Last Modified: 27/09/23

# We put our data first... sorry! Habits from C++ and python are hard to break.
.data
# ASCII with NULL terminator, to be C++ string-like.
hourly: .asciiz "Please enter the employee's hourly wage: " 
worked: .asciiz "Please enteer the hours worked: "
total_pay: .asciiz "The employee's total pay is $ "

# The actual code goes in the  text section:
.text

# This function gets the hourly wages; it also validates the input
# we're going to compare the entered value to the last Floating point register, so we'll make sure $f31 is 0 by subtracting it from itself!! :D
sub.s $f31, $f31, $f31
sub.s $f0, $f0, $f0
sub.s $f1, $f1, $f1
sub.s $f12, $f12, $f12
enter_hourly:
	# Load the "Hourly pay" message into memory:
	la $a0, hourly
	# Then set v0 to 4 as a system call bit:
	li $v0, 4
	# Next; execute the system call function:
	syscall
	# Subsequently, set the v0 to read floats, that's command '6':
	li  $v0, 6
	# And run Syscall again:
	syscall
	# If $f0 <= than $f31, then we should ask the user to re-input the value:
	c.le.s $f0, $f31
	bc1t enter_hourly
# Now, let's copy (move) the value from $f0 to $f1 so we can ask for the weekly hours worked:
mov.s $f1, $f0

# step two, let's do the same, but for hours worked:
enter_worked:
	# Load the "Hourly pay" message into memory:
	la $a0, worked
	# Then set v0 to 4 as a system call bit:
	li $v0, 4
	# Next; execute the system call function:
	syscall
	# Subsequently, set the v0 to read floats, that's command '6':
	li  $v0, 6
	# And run Syscall again:
	syscall
	# If $f0 <= than $f31, then we should ask the user to re-input the value:
	c.le.s $f0, $f31
	bc1t enter_worked
	
# $f1 now contains hourly rate, and $f0 contains hours worked. We're ready to multiply.
# Multiply into $f12; the output register:
mul.s $f12, $f1, $f0
# Now, output the result:
# First of all, the string:
la $a0, total_pay
li $v0, 4
syscall
# Now to output a float, set $v0 to 2 and call syscall:
li $v0, 2
# Finally; execute the system call function:
syscall

	