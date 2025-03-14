import pandas as pd
import numpy as np


# File_object = open(r"Myfile1.txt", "Access_Mode")

# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
file1 = open("MyFile1.txt", "a")

# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt", "w+")

# Opening and Closing a file "MyFile.txt"
# for object name file1.
#file1 = open("MyFile.txt", "a")
file1.close()

# File_object.write(str1)

# File_object.writeline(L) for L = [str1, str2, str3]

# File_object.read([n])

# File_object.readline([n])

# File_object.realines()

# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
file1 = open("myfile.txt", "r+")
print("Output of Read function is ")
print(file1.read())
print()
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()
file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()
# Append-adds at last
#file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()
file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()
# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()
file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()

index = pd.date_range("1/1/2013", periods=6)
df = pd.DataFrame(np.random.randn(6, 3), index=index, columns=["A", "B", "C"])
df.to_csv('data.csv')

df = pd.read_csv('data.csv', index_col=0)

#pip install xlwt openpyxl xlsxwriter xlrd

#df.to_excel('data.xlsx')

#df = pd.read_excel('data.xlsx', index_col=0)

#df = pd.DataFrame(data=data).T
#df.to_json('data-columns.json')

#df.to_json('data-index.json', orient='index')
