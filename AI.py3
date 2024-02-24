import random,sys

field = []   

inputFile = sys.argv[1]  
outputFile = sys.argv[2]

class Cow(object):


# reading input file
    with open(inputFile) as f:
        lines = f.readlines()
       
        for i in lines:
            a = list(i.rstrip())
            field.append(a)
   

#counting number of @'s
    z = "@"
    counter = 0
    for i in range(len(field)):
        counter += field[i].count(z)
    i = 1

    size_of_farm = int(field[0][0])

#replacing "." with "C"

    while(i<=counter):
        ind_1 = random.randint(1,size_of_farm)
        ind_2 = random.randint(0,size_of_farm-1)
        if field[ind_1][ind_2] == "." :
            field[ind_1][ind_2] = "C"
            i +=1

   

#to find index of Character in this case for "C"

def find(char):
    for i, istr in enumerate(field):
        
        for j,jstr in enumerate(istr):
            try:
                if jstr == char:
                    yield i, j
            except ValueError:
                continue

# to check if the index is outofbounds     
       
def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

# to calculate score

def CountScore(arr, i, j):
    offsets = [[-1,-1],[-1,0],[-1,1],
               [0,-1],        [0, 1],
               [ 1,-1],[1, 0],[1,1]]

    
 # Size of given 2d array
    n = len(arr)
    m = len(arr[0])

    CowScore = 0
    another_cow = False
    pond = False
    haystack = False
    for off in range(0,8):
        
        row = i + offsets[off][0] # 1 + [-1]
        col = j + offsets[off][1]
        
        
        
        total = sum(offsets[off])
        
        if total == -1 or total == 1:
            orthogonal = True
        else:
            orthogonal = False
        
        
        if (isValidPos(row,col,n,m)):
            if arr[row][col] == 'C':
                another_cow = True
            elif orthogonal:
                if arr[row][col] == '@':
                    haystack = True
                if arr[row][col] == '#':
                    pond = True
   
    if another_cow:
        CowScore -= 3
    if haystack:
        CowScore += 1
        if pond:
           CowScore += 2
    
    return CowScore

# to generate output file

def output_data(lines, filename):
    with open(filename, 'w') as file:
        for item in field:
            for i in range(len(item)):
                file.write("%s" % item[i])
            file.write("\n")
        file.close()


#Find the index for all the Cows placed in the farm
farmSize = field.pop(0)
matches = [match for match in find('C')]



#Calculate Score of all the cows
Total_Cow_Score = 0
for i,j in matches:
    Total_Cow_Score += CountScore(field, i, j)

field.append([str(Total_Cow_Score)])

field.insert(0, farmSize)
output_data(field,outputFile)


