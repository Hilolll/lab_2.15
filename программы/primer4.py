# open the file2.txt in read mode. causes error if no such file exists
with open("file2.txt", "r") as fileptr:
    #stores all the data of the file into the variable content
    content = fileptr.readlines()
    # prints the content of the file
    print(content)