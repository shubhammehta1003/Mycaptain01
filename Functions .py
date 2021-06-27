# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Z = input("Enter a string:\t")
d = {}
for i in range(0, len(Z)):
    if Z[i] not in d:
        d[Z[i]] = 1
    else:
        d[Z[i]] += 1

keylist = list(d.keys())
for bubbleSort_1 in range(0, len(keylist)):
    for bubbleSort_2 in range(0, bubbleSort_1+1):
        for i in range(0, len(keylist)-1, 1):
            a = d[keylist[i]]
            b = d[keylist[i+1]]
            if a < b:
                t = {keylist[i]: a}
                u = {keylist[i+1]: b}
                v = {}
                for s in range(0, i):
                    v[keylist[s]] = d[keylist[s]]
                w = {}
                for s in range(i+2, len(keylist)):
                    w[keylist[s]] = d[keylist[s]]
                d.clear()
                d.update(v)
                d.update(u)
                d.update(t)
                d.update(w)
            keylist = list(d.keys())
print(d)
            
            
            
            
            
        
        
        
        

     




















     
   

    