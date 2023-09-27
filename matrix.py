# transpose tar en matris M
def transpose(M):
    result = []
    m = len(M) # rader i M
    # om M är tom returnas []
    if m == 0: return result 
    n = len(M[0]) # kolumner i M
    for j in range(0, n):
        row = []
        for i in range(0,m):
            row.append(M[i][j])
        result.append(row)
    return result

# powers tar en lista l och två tal x och y
def powers(l, x, y):
    result = []
    rows = len(l)
    for r in range(0, rows):
        row = []
        for i in range(x, y + 1):
            row.append(l[r]**i)
        result.append(row)
    return result

def matmul(A, B):  
    result = []
    # om A eller B är tomma eller om kolumner i A inte är lika med rader i B så returnas []
    if len(A) == 0 or len(B) == 0 or len(A[0]) != len(B): return result
    m = len(A)      # rader i A
    n = len(A[0])   # kolumner i A / rader i B
    r = len(B[0])   # kolumner i B
    # i är nuvarande rad och j är nuvarande kolumn i AB, k är var i summaberäkningen man är
    for i in range(0, m):
        row = []
        for j in range(0, r):
            sum = 0
            for k in range(0, n):
                sum += A[i][k]*B[k][j]
            row.append(sum)
        result.append(row)
    return result

# invert tar en matris A
def invert(A):
    # A ska vara en 2x2 matris, om det inte är det returnas []
    if len(A) != 2 or len(A[0]) != 2: return []
    det = A[0][0]*A[1][1]-A[0][1]*A[1][0] # determinanten, a*d-b*c
    result = [[A[1][1]/det, -A[0][1]/det],
              [-A[1][0]/det, A[0][0]/det]]
    return result

# loadtxt tar en string dir som leder till en textfil
def loadtxt(dir):
    # öppnar filen och kopierar linjerna till lines
    file = open(dir)
    lines = file.readlines()
    file.close()

    result = []
    for line in lines:
        items = line.split() # delar upp föremålen i raden
        row = []
        for item in items:
            row.append(float(item)) 
        result.append(row)
    return result