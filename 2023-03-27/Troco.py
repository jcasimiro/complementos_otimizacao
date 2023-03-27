import numpy as np

def troco(seq,N):
    v =[]
    i=0
    while N>0:
        if seq[i]<=N:
            v.append(seq[i])
            N=N-seq[i]
        else:
            i+=1
    return v

def write_output(filename, results):
    file = open(filename, "w")
    for result in results:
        file.write(str(result) + "\n")
    file.close()

seq = [200,100,50,20,10,5,2,1]
N=42
t=troco(seq,N)
write_output("2023-03-27/output_troco.txt", t)