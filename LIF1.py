#利用sympy包进行微分方程的运算
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

#声明常量
R = 2.6*10**6
tau = 20*10**-3
I = 5*10**-9
Urest = -70*10**-3
Uth = -57*10**-3

#声明符号变量
t = symbols('t')
# Um = symbols('Um',cls=Function)
Um=Function('Um')

#常微分方程
eq = Eq(tau*Um(t).diff(t),Urest-Um(t)+R*I)
result = dsolve(eq,Um(t),ics={Um(0):Urest})
result=result.rhs

t0=0
y=[]
def LIF(ts):
    global t0
    temp=lambdify(t,result.subs(t,ts-t0),"math")
    U=temp(ts)
    if U >= (Uth - 0.00001):
        U=Urest
        t0=ts
    y.append(U)

times=np.linspace(0,1,1000)
for i in times:
    LIF(i)

plt.plot(times,y)
plt.xlabel("time")
plt.ylabel("voltage")
plt.show()



