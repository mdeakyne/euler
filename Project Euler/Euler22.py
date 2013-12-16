#open the file names.txt
f = open("names.txt","r")
#all names are on one line, comma delimited
s_names = f.readline() 
f.close()
#takes the string and splits it into a list
l_names = s_names.split(",")

#create a dictionary to give values to each letter, A=1, B=2....Z=26
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 1
d = {}
#each name is surrounded by ". Instead of slicing, just give them
#a value of zero.
d['"'] = 0
for letter in s:
	d[letter]=count
	count += 1 

#names must be sorted
l_names.sort()

'''
#trial with the first name to make sure counting works
total = 0
for char in l_names[0]:
	print char,d[char]
	total += d[char]
'''

#line number is a multiplier, start at one and increase each iteration
line_num = 1
#total is the absolute total
total = 0
#name total is per name, so we can then use the multiplier
name_total = 0
for name in l_names:
	for char in name:
		name_total+=d[char]
	total += line_num * name_total
	line_num += 1
	name_total = 0

#Ans: 871198282
print total


