import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []

def noeud_verif(a_droite,y,x,width,height):
    axe = x if a_droite else y
    length = width if a_droite else height
    i = 1
    while(axe+i < length):
        noeu = lines [y][x+i] if a_droite else lines [y+i][x]

        if noeu == "0" and a_droite :
            return str(x+i)+" "+ str(y)+" "
        elif noeu == "0" and not a_droite :
            return str(x)+" "+ str(y+i)+" "
        i += 1

    return str(-1)+" "+ str(-1)+" "
        



for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(list(line))
for y in range(height):
    for x in range(width):
        info_noeud = ""
        if lines[y][x]=="0":
            info_noeud += str(x) + " " +str(y)+ " "
            info_noeud += noeud_verif(True,y,x,width,height)
            info_noeud += noeud_verif(False,y,x,width,height)
            
            print (info_noeud)
