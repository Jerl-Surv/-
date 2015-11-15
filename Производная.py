#dx
 
n = int(input("Количество точек функции: "))

X = []
Y = []
k = 1

for i in range(n):
    x = int(input("x: "))
    X.append (x)
    y = int(input("y: "))
    Y.append (y)

while k < n:
    for i in range(n-k):
        if X[i] > X[i+1]:
            X[i],X[i+1] = X[i+1],X[i]
            Y[i],Y[i+1] = Y[i+1],Y[i]
    k += 1    
    
a = int(input("Точка для производной: "))

for i in range(n):
    if X[i] == a:
        j = i

g = Y[j]
f = Y[j+1]
h = X[j+1] - X[j]

def dx(g, f, h):
    return (f - g)/h

print (dx(g, f, h))
