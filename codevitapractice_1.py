# INPUT: 
# 3
# 1 Hello
# 5 Hello welcome to the CodeVita
# 8 Hello welcome to the CodeVita have a greatday

# OUTPUT:
# Hello
# Hello welcome to the CodeVita
# Hello welcome to the CodeVita have a greatday


n=int(input())
for i in range(n):
    linetobeprinted=[]
    line = input()
    words = line.split()
    for k in range(len(words)):
        if (k!=0):
            linetobeprinted.append(words[k])
    print(" ".join(linetobeprinted))