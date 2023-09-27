from matrix import *
import sys
import matplotlib.pyplot as plt

# skapar en matris a från textfilen
a = loadtxt(sys.argv[1])
at = transpose(a) # at är transponat av a

x = at[0] # x är första kolumnen i a / första raden i at 
y = at[1] # y är andra  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

xp  = powers(x,0,1)
yp  = powers(y,1,1)
xpt = transpose(xp)

# predicted number of chirps = b + m * temperature
[[b],[m]] = matmul(invert(matmul(xpt,xp)),matmul(xpt,yp))
y2 = []
for temp in x:
    y2.append(b + m * temp)

# ritar plots
plt.plot(x,y,'ro')
plt.plot(x,y2)
plt.show()

