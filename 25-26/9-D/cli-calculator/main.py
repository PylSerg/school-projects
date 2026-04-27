row = input("\n>> ").split()
result = 0

if row[0] == "+":
    for i in enumerate(row):
        if i[0] == 0: 
            continue
        elif i[0] == 1: 
            result = float(i[1])
        else:
            result += float(i[1])
            
elif row[0] == "-":
    for i in enumerate(row):
        if i[0] == 0: 
            continue
        elif i[0] == 1: 
            result = float(i[1])
        else:
            result -= float(i[1])
            
elif row[0] == "*":
    for i in enumerate(row):
        if i[0] == 0: 
            continue
        elif i[0] == 1: 
            result = float(i[1])
        else:
            result *= float(i[1])
            
elif row[0] == "/":
    for i in enumerate(row):
        if i[0] == 0: 
            continue
        elif i[0] == 1: 
            result = float(i[1])
        else:
            result /= float(i[1])
            
else:
    print("\n\033[01;31mERROR: Unsupported action!")
    exit()
            
            
print(f"\n\nResult: {result} \n\n")