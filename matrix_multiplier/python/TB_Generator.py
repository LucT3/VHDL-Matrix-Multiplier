"""
----------------------------TB_Generator.py SPECIFICATIONS--------------------------
////////////////////////////////////////////////////////////////////////////////////
/// the program automatically find the matrices size and let the user create    ////
/// 2 default cases, when the multiplication return the maximum positive and    ////
/// the maximum negative number as product result.                              ////
/// Moreover, the program let create a totally random matrices or let the user  ////
/// choice all the values.                                                      ////
///                                                                             ////
/// At the end the program will calculate the real matrix multiplication        ////
/// values printing it on a file (Results.txt)                                  ////
/// and produce the testbench file (MatrixMultiplier_tb.vhd),                   ////
/// so the user can compare the values returned in the simulation.              ////
////////////////////////////////////////////////////////////////////////////////////
"""

from random import randint, seed
from random import random
import numpy as np
import sys


#-------------FUNCTIONS-------------#


#FUNCTION TO CONVERT A SIGNED DECIMAL NUMBER IN A 4 BITS 2'S COMPLEMENT NUMBER

def dec_to_twos(num):
    #converting the numbers in 2's complement
    if (num < 0 ):
        negative = True
    else:
        negative = False
    binary_number = int("{0:08b}".format(abs(num)))
    binary_number = str(binary_number)
    while (len(binary_number) < 4):
        binary_number = '0' + binary_number

    if (negative):
        ones_complement = ""
        for bit in binary_number:
            if(bit == '1'):
                bit = '0'
            elif(bit == '0'):
                bit = '1'
            ones_complement += bit
        twos_complement = int(ones_complement,2)
        twos_complement = twos_complement + 1
        twos_complement = bin(twos_complement).replace("0b","")
        converted_number = twos_complement

    else:
        converted_number = binary_number

    converted_number = '"'+converted_number+'"'
    return converted_number




#-------------MAIN-------------#

#find the size of matrix A and matrix B reading the Base.txt file
size_matrixA = []
size_matrixB = []

for line in open("./Base.txt"):
    #find the size of the matrix A
    if ("matrixA" in line):
        tmp = line.split(" ")
        if( len(tmp) > 2 and tmp[2].isnumeric()):
            size_matrixA.append(int(tmp[2]))

    #find the size of the matrix B 
    if ("matrixB" in line):
        tmp = line.split(" ")
        if( len(tmp) > 2 and tmp[2].isnumeric()):
                size_matrixB.append(int(tmp[2]))

print("\nMatrix A\nRow number:",size_matrixA[0], "\nColumn number:", size_matrixA[1])
print("\nMatrix B\nRow number:",size_matrixB[0], "\nColumn number:", size_matrixB[1])


#Create the matrices for the testbench and to calculate the real matrix multiplication (4 possbile cases)
decimal_values_matrixA = []
decimal_values_matrixB = []

values_matrixA = []
values_matrixB = []

mode = 0
print("\n**TESTBENCH GENERATOR, Choose the mode")
print("MODE 1: Assign values to matrices A and B in order to produce the largest positive number")
print("MODE 2: Assign values to matrices A and B in order to produce the largest negative number")
print("MODE 3: Generate randomly the values for the matrices A and B")
print("MODE 4: Create your own matrices A and B")

while(mode not in range(1,5)):
    mode = int(input("\nSelect the mode (1,2,3 or 4): "))

#MODE 1
if ( mode == 1):
    #create the max positive multiplication case (-8 * -8)
    print("\nMODE 1: Positive limit case")

    #number to put into the matrix
    number = dec_to_twos(-8)
    default_number = dec_to_twos(0)

    #assign the values for matrix A
    for row in range(size_matrixA[0]):
        tmp = []
        for col in range(size_matrixA[1]):
            if (row == 0):
                tmp.append(-8)
                values_matrixA.append(number)
            else:
                tmp.append(0)
                values_matrixA.append(default_number)
        decimal_values_matrixA.append(tmp)

    #assign the values for matrix B
    for row in range(size_matrixB[0]):
        tmp = []
        for col in range(size_matrixB[1]):
            if (col == 0):
                tmp.append(-8)
                values_matrixB.append(number)
            else:
                tmp.append(0)
                values_matrixB.append(default_number)
        decimal_values_matrixB.append(tmp)

#MODE 2
elif(mode == 2):
    #create the max negative multiplication case (-8 * 7)
    print("\nMODE 2: Negative limit case")

    #number to put into the matrix
    number_matrixA = dec_to_twos(-8)
    number_matrixB = dec_to_twos(7)
    default_number = dec_to_twos(0)

    #assign the values for matrix A
    for row in range(size_matrixA[0]):
        tmp = []
        for col in range(size_matrixA[1]):
            if (row == 0):
                tmp.append(-8)
                values_matrixA.append(number_matrixA)
            else:
                tmp.append(0)
                values_matrixA.append(default_number)
        decimal_values_matrixA.append(tmp)

    #assign the values for matrix B
    for row in range(size_matrixB[0]):
        tmp = []
        for col in range(size_matrixB[1]):
            if (col == 0):
                tmp.append(7)
                values_matrixB.append(number_matrixB)
            else:
                tmp.append(0)
                values_matrixB.append(default_number)
        decimal_values_matrixB.append(tmp)

#MODE 3
elif(mode == 3):
    #create random values for the matrix
    print("\nMODE 3: Generate randomly the values for the matrices A and B")

    #select the seed for the random generator
    choosen_seed = int(input("Choose the seed: "))
    seed(choosen_seed)

    #assign the values for matrix A
    for row in range(size_matrixA[0]):
        tmp = []
        for col in range(size_matrixA[1]):
            random_number = randint(-8,7)
            tmp.append(random_number)

            number_matrixA = dec_to_twos(random_number)
            values_matrixA.append(number_matrixA)
        decimal_values_matrixA.append(tmp)

    #assign the values for matrix B
    for row in range(size_matrixB[0]):
        tmp = []
        for col in range(size_matrixB[1]):
            random_number = randint(-8,7)
            tmp.append(random_number)

            number_matrixB = dec_to_twos(random_number)
            values_matrixB.append(number_matrixB)
        decimal_values_matrixB.append(tmp)

#MODE 4
else:
    #choose the values for the cells
    print("\nMODE 4: Choose the values for your matrices")

    #assign the values for matrix A
    print("\nCHOOSE VALUES FOR MATRIX A\n")
    for row in range(size_matrixA[0]):
        tmp = []
        for col in range(size_matrixA[1]):
            print("Value for position (",row+1,",",col+1,"): ")
            chosen_number = 8
            while (chosen_number not in range (-8,8)):
                chosen_number = int(input())
            tmp.append(chosen_number)

            number_matrixA = dec_to_twos(chosen_number)
            values_matrixA.append(number_matrixA)
        decimal_values_matrixA.append(tmp)

    #assign the values for matrix B
    print("\nCHOOSE VALUES FOR MATRIX B")
    for row in range(size_matrixB[0]):
        tmp = []
        for col in range(size_matrixB[1]):
            chosen_number = 8
            print("Value for position (",row+1,",",col+1,"): ")
            while (chosen_number not in range(-8,8)):
                chosen_number = int(input())
            tmp.append(chosen_number)

            number_matrixB = dec_to_twos(chosen_number)
            values_matrixB.append(number_matrixB)
        decimal_values_matrixB.append(tmp)



#Creating the matrices with the binary values ( to insert in the tb file)

#creating the binary matrix A
k = 0
matrixA = "("
for i in range(size_matrixA[0]): #row number
    matrixA += "("
    for j in range(size_matrixA[1]): #col number
        matrixA += values_matrixA[k] + ","
        k += 1
    matrixA = matrixA[:-1] #delete the last comma
    matrixA += "),"

matrixA = matrixA[:-1] #delete the last comma
matrixA += ");"
print("\nBINARY MATRIX A:\n",matrixA)


#creating the binary matrix B
k = 0
matrixB = "("
for i in range(size_matrixB[0]): #row number
    matrixB += "("
    for j in range(size_matrixB[1]): #col number
        matrixB += values_matrixB[k] + ","
        k += 1
    matrixB = matrixB[:-1] #delete the last comma
    matrixB += "),"

matrixB = matrixB[:-1] #delete the last comma
matrixB += ");"
print("BINARY MATRIX B:\n",matrixB)


# generate testbench file
sys.stdout = open("./MatrixMultiplier_tb.vhd", "w")

for line in open("./Base.txt"):

    #write the values for the matrix
    if "wait for 200" in line:
        print("\t\t\twait for 50 ns;")
        #print('\t\t\tmatrixA_ext <= (("1000","1000","1000"),("0000","0000","0000"));')
        print('\t\t\tmatrixA_ext <= '+ matrixA)
        #print('\t\t\tmatrixB_ext <= (("1000","0000","0000","0000"),("1000","0000","0000","0000"),("1000","0000","0000","0000"));')
        print('\t\t\tmatrixB_ext <= '+ matrixB)
        print("\t\t\twait until rising_edge(clock);")
        
    print(line, end="")


sys.stdout = sys.__stdout__

print("\n**MatrixMultiplier_tb.vhd File correctly generated**\n")



#GENERATE THE REAL RESULTS (MATRIX MULTIPLICATION)

print("\n**MATRIX MULTIPLICATION RESULTS**\n")

#print the matrices A and B
print("MATRIX A (" ,size_matrixA[0],"x",size_matrixA[1] ,"):\n",np.array(decimal_values_matrixA))
print("\nMATRIX B (" ,size_matrixB[0],"x",size_matrixB[1] ,"):\n",np.array(decimal_values_matrixB))

#First method
#res = np.dot(mat1,mat2)

#Second method
decimal_res = np.array(decimal_values_matrixA) @ np.array(decimal_values_matrixB)
print("\nMATRIX P = AB (MATRIX MULTIPLICATION RESULT): \n",decimal_res)


#Write the result into Result.txt file
sys.stdout = open("./Results.txt", "w")

print("**MATRIX MULTIPLICATION RESULTS**\n")

print("MATRIX A (" ,size_matrixA[0],"x",size_matrixA[1] ,"):\n",np.array(decimal_values_matrixA))
print("\nMATRIX B (" ,size_matrixB[0],"x",size_matrixB[1] ,"):\n",np.array(decimal_values_matrixB))

print("\nMATRIX P = AB (MATRIX MULTIPLICATION RESULT): \n",decimal_res)

sys.stdout = sys.__stdout__


print("\n**Result.txt File correctly generated**\n")