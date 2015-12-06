n = int(input("Количество уравнений: "))

system = []
solution = []
t = 0

for i in range(n):
    X = []
    for j in range(n):
        x = int(input(" "))
        X.append (x)        
    system.append (X)
    
print (system)

for i in range(n):
    x = int(input(" "))
    solution.append (x)
    
#if system[1[1]] != 0:
for i in range(n-1):
    j == i+1
    b = system[i]
    for j in range(n-1):
        t == j
        a = system[j]
        for t in range(n):
            a[t] = a[t] - b[t]

#else:
#    system[1] == system[2]

print (system)