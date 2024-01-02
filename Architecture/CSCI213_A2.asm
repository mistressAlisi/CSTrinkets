# MIPS Assembler Code!!
# CCP - Computer Science 
# CSCI213 - Fall 2023 - Assignment 2
# Written by Diana Mann.
# Last Modified: 18/09/23

# First off, let's load our values into the registers using load immediate: This is a pseudo-op, the assembler actually turns it into addi $t0, [value], $zero. 
li $t0, 0xB5 # Use the LOAD IMMEDIATE Pseudo-op to load 0xB5 into $t0. 
li $t1, 0x7E # Use the LOAD IMMEDIATE Pseudo-op to load 0x7E into $t1
li $t2, 0xF1 # Use the LOAD IMMEDIATE Pseudo-op to load 0xF1 into $t2

# Now, using Bitmasks, Let us do some Register magick(tm):
# In order to make the computation as efficient as possible and use as little resources as possible, we'll
# achieve this with logical operations. We will use logical AND to ONLY set the bits we're interested in, and ignore the rest of the bits, literally "masking" them away.

# First of all, we want to set our destination registers, $s0, $s1, and $s2 to zero:
# A bit of a hackish way to do it, but it makes sense: 0+0 = 0:
li $s0, 0
li $s1, 0
li $s2, 0


# For exercise part 1, we're intersted in Bits 2,3,4 of $t0:
# Now, execute the bitwise AND using the immediate andi instruction to carry out the bit-wise AND between the value at $t0 and 0X1C (b00011100)
andi $s0, $t0, 0x1C
# $s0 now contains b00010100 = 0x14.

# Part 2: Same thing for $s1, which will get the bitmask applied to bits 7,6,5 and 4:0XF0 mask applied to the value at $t1:
andi $s1, $t1, 0xF0
# $s1 now contains b0111000 = 0x70.

# Part 3: Same thing for $s2, which will get the bitmask applied to bits 5-2 :0X3C mask applied to the value at $t2:
andi $s2, $t2, 0x3C
# $s2 now contains b00110000 = 0x30.
 
 

