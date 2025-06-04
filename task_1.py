try:
    file = open('sample.txt',"r")

    print("Reading file content:")
    count = 1

    for line in file:
        print("Line {}: {}".format(count,line.strip()))
        count += 1

    file.close()



except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
