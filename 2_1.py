from pyparsing import *
import math

num = ZeroOrMore(Word(nums + ".-"))
temp = []
a = []
b = []
c = []

const = [1, 2, 1, 1.5]
tau = [0.001, 0.01, 0.1, 0.3, 0.5, 0.7]
K = []
K_cash = []
y1 = [1]
y2 = [0.05]
t = [0]

def set_data(file_name):
	global S, eps
	file = open(file_name, 'r')

	for line in file:
		temp.append((num.parseString(line)).asList())
	S = int(temp[0].pop())
	
	for i in range(1, S+1):
		a.append(temp[i].pop(0))

	for i in range(S):
		b.append(list())
	for i in range(0, S):
		for j in range(0, S):
			b[i].append(temp[i+1][j])

	for i in range(0, S):
		c.append(temp[S][i])

	try:
		eps = (temp[S+2][0])
	except Exception:
		eps = 0
		
	for i in range(0, S):
		K.append(list())

	for i in range(0, S):
		for j in range(0, 3):
			K[i].append(0.0)
	file.close()

def set_t(k, g): #t step
	global t
	t.clear()
	for i in range(0, g*int(math.pow(tau[k], -1)), 1):
		t.append(i/int(math.pow(tau[k], -1)))
	return 0

def get_range(k, g):
	return g*int(math.pow(tau[k], -1))


def print_data(n): #in file
	global t
	file = open(str(tau[n])+'.txt', 'w')
	file.write('t = ' + str(tau[n-1])+'\n')
	for i in range(len(t)):
		file.write(str(t[i])+'\t'+str(y1[i])+'\t'+str(y2[i])+'\n')
	file.close()


#sum1-4 - summs for k
def sum1(st, en):
	res = 0.0
	for i in range(st, en):
		res = res + float(b[i][en-1])*(const[0] - const[1]*K[i][2])*K[i][1]
	return res

def sum1_im(st):
	res = 0.0
	for i in range(st, S):
		if math.fabs(math.sqrt(K_cash[i][0]**2 + K_cash[i][1]**2 + K_cash[i][2]**2) - math.sqrt(K[i][0]**2 + K[i][1]**2 + K[i][2]**2)) > eps:
			res = res + float(b[i][en-1])*(const[0] - const[1]*K_cash[i][2])*K_cash[i][1]
		else:
			res = 0.0
	return res
	
def sum2(st, en):
	res = 0.0
	for i in range(st, en):
		res = res + float(b[i][en-1])*(-const[2] + const[3]*K[i][1])*K[i][2]
	return res

def sum2_im(st):
	res = 0.0
	for i in range(st, S):
		if math.fabs(math.sqrt(K_cash[i][0]**2 + K_cash[i][1]**2 + K_cash[i][2]**2) - math.sqrt(K[i][0]**2 + K[i][1]**2 + K[i][2]**2)) > eps:
			res = res + float(b[i][en-1])*(-const[2] + const[3]*K[i][1])*K[i][2]
		else:
			res = 0.0		
	return res

def sum3():
	res = 0.0
	for i in range(0, S):
		res = res + float(c[i])*(const[0] - const[1]*K[i][2])*K[i][1]
	return res

def sum3_im():
	res = 0.0
	for i in range(0, S):
		res = res + float(c[i])*(const[0] - const[1]*K[i][2])*K[i][1]
	return res

def sum4():
	res = 0.0
	for i in range(0, S):
		res = res + float(c[i])*(-const[2] + const[3]*K[i][1])*K[i][2]
	return res

def sum4_im():
	res = 0.0
	for i in range(0, S):
		res = res + float(c[i])*(-const[2] + const[3]*K[i][1])*K[i][2]
	return res

def step(n, k): #calculate k and next y
	K[0][0] = t[n] + float(a[0])
	K[0][1] = y1[n]
	K[0][2] = y2[n]
	for j in range(1, S):
		K[j][0] = t[n] + float(a[j])
		K[j][1] = y1[n] + tau[k]*sum1(0, j)
		K[j][2] = y2[n] + tau[k]*sum2(0, j)
	y1.append(y1[n] + tau[k]*sum3())
	y2.append(y2[n] + tau[k]*sum4())
	
def step_im(n, k): #calculate k and next y
	K[0][0] = t[n] + float(a[0])
	K[0][1] = y1[n]
	K[0][2] = y2[n]
	for j in range(1, S):
		K[j][0] = t[n] + float(a[j])
		K[j][1] = y1[n] + tau[k]*sum1_im(0)
		K[j][2] = y2[n] + tau[k]*sum2_im(0)
	K_cash = K.copy()
	y1.append(y1[n] + tau[k]*sum3())
	y2.append(y2[n] + tau[k]*sum4())



set_data('input.dat')
set_t(4, 40)
if eps == 0.0:
	for i in range(0, get_range(4, 40)):
		step(i, 4)
else:
	for i in range(0, get_range(4, 40)):
		step_im(i, 4)	
print_data(4)










