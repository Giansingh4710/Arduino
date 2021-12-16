'''
this script is to remove the sketch
'''

path="C:\\Users\\gians\\Desktop\\CS\\Arduino\\.vscode\\arduino.json"

lines=[]
with open(path, "r") as file1:
    # reading data to a file
    lines=file1.readlines()
newLines=[]
for line in lines:
    theNewLine=line
    if '"sketch":' in line:
        theNewLine='"sketch": ""\n'
    newLines.append(theNewLine)

with open(path, "w") as file1:
    # writing data to a file
    for i in newLines:
        file1.write(i)
    print("Reset Successful!!!")
