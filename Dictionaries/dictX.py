
#Splits dict.txt into words by letters

file = open("dict.txt","r")
zx = set(file.read().split("\n"))

for x in "abcdefghijklmnopqrstuvwxyz".upper():
	filteredList = [y for y in zx if y.startswith(x)]   
	#print(zx)
	f1=open(x + "_dict.txt","w+")
	for ma in filteredList:
		f1.write(ma + "\n")