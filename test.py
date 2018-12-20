# -*- coding: utf-8 -*-

def transform():
    l = [0,1,2,3,4]
    lenSol = len(l)
    print('narmol : ', l)
    for i in range(0, lenSol):
        j = (i+2) % lenSol
        while (j != i):
            l2 = l[:]
            val = l2[i]
            del l2[i]
            l2.insert(j, val)
            print("i & j : ", (i,j))
            print(str(l2))
            j = (j+1)%lenSol


if __name__ == "__main__":
    transform()
