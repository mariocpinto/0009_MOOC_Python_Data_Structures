# 7.1 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt

file_name = input('Enter Filename: ')

try:
    file_handle = open(file_name,'r')
except:
    print('Error opening file.')
    exit()

for line in file_handle :
    line = line.rstrip()
    print(line.upper())