
# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and 
#   if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

file_name = input('Enter file name: ')
file_handle = open(file_name)

master_list = list()

for line in file_handle:
    line = line.rstrip()    # Remove \n
    words = line.split()
    
    for word in words:
        if word in master_list: continue
        
        master_list.append(word)    # Add only new words
        
master_list.sort()

print(master_list)        
    