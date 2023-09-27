from numpy import *
import sys
import matplotlib.pyplot as plt

txt = sys.argv[1] # txt är en textfil
n = int(sys.argv[2]) # n är graden på polynomet

# powers tar en lista l och två tal x och y
def powers(l, x, y):
    result = []
    rows = len(l)
    for r in range(0, rows):
        row = []
        for i in range(x, y + 1):
            row.append(l[r]**i)
        result.append(row)
    return array(result) # returnar en numpy array istället för en lista

# poly tar en matris a och ett nummer x
def poly(a, x):
    p = 0
    for i in range(0,len(a)):
        p += a[i]*(x**i)
    return p

# skapar en matris m från textfilen
m = loadtxt(txt)
mt = transpose(m) # mt är transponatet av m

x = mt[0] # x är första kolumnen i m / första raden i mt 
y = mt[1] # y är andra  ^^^^^^^^^^^^^^ andra  ^^^^^^^^^^

xp  = powers(x, 0, n)
yp  = powers(y, 1, 1)
xpt = transpose(xp)

a = matmul(linalg.inv(matmul(xpt, xp)),matmul(xpt, yp))
a = a[:,0]

# start är första i x, stop är sista i x, num är 
x2 = linspace(x[0], x[len(x) - 1], int((x[len(x) - 1]-x[0])/0.2)).tolist()

y2 = []
for temp in x2:
    y2.append(poly(a, temp))

# ritar plots
plt.plot(x,y,'ro')
plt.plot(x2,y2)
plt.show()