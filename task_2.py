file = open('output.txt','w')
text = input("Enter text to write to the file: ")
file.write(text)
print("Data successfully written to output.txt")
file.close()

file = open('output.txt','a')
text = input("Enter additional text to append: ")
file.write("\n"+text)
file.close()

file = open('output.txt','r')
print("Final content of output.txt:")
for line in file:
    print(line.strip())
file.close()