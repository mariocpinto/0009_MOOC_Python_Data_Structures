# 7.2 Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

file_name = input("Enter Filename: ")

try:
    file_handle = open(file_name,'r')
except:
    print("Unable to open file")

count = 0
sum   = 0
    
for line in file_handle:
    
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    line = line.rstrip() # Remove trailing \n
    
    c_pos = line.find(':')  # Find ':'
    num = line[c_pos+1:]
    
    count = count + 1
    sum = sum + float(num)

if count != 0 :
    print("Average spam confidence:",(sum/count))
else:
    print("No spam confidence entries found")