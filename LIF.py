#方法一：把微分方程中的dt直接定义出来
import numpy as np
import matplotlib.pyplot as plt

#定义常数,单位要统一
R = 2.6*10**6
Urest = -70*10**-3
Uth = -57*10**-3
I = 5*10**-9
tau = 20*10**-3
dt = 1*10**-3


#定义微分方程
def Efunction(U):
    '''
    :param U:前一时刻的膜电压值
    :return:微分方程
    '''
    return (-(U-Urest)+R*I)/tau

ts = np.arange(0,1+dt,dt)
Um = np.zeros(len(ts))
Um[0] = Urest

def LIF():
    for i in range(1,len(ts)):
        Um[i] = Um[i-1]+dt*Efunction(Um[i-1])
        if Um[i]>=(Uth- 0.00001):
            Um[i] = Urest

LIF()
flag=np.full([1,len(ts)],Uth)
plt.plot(ts,Um)
plt.plot(ts,flag[0])
plt.xlabel("time")
plt.ylabel("voltage")
plt.show()

