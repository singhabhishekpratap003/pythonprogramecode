file = open("data.txt" , "r")
#data = file.write("this is my first file that creating for practice the file handling methods\n")
#data = file.write("the file handling is the very ossum subject .\n ")
data = file.read()
print(data)


file.close()
