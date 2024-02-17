

cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    
    
    if float(line[0]) > 100:
        print("The planet is too hot.")

    elif float(line[0]) < 0:
        print("The planet is too cold.")

    if str(line[1]) == "false" and float(line[3]) < 0.6:
        print("The planet has no water.")

    if str(line[2]) == "false":
        print("The planet has no magnetic field.")

    if float(line[3]) > 0.6 and float(line[0]) > 0:
        print("The planet's orbit is not ideal.")

    
    print("The planet is habitable.")
