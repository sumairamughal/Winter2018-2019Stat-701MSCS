import numpy as np
import matplotlib.pyplot as plt
CPUTime = np.array((2, 5, 7, 9, 10, 13, 20))
memory=np.array((2,4,8,16,32,64, 128))
DiskIO= np.array((14, 16, 27, 42, 39, 50, 83))
# number of observations/points
n = np.size(DiskIO)

# mean of x and y vector
m_X1, m_X2, m_Y = np.mean(CPUTime),np.mean(memory), np.mean(DiskIO)
print('Mean of X1   =  ',m_X1)
print('Mean of X2   =   ',m_X1)
print('Mean of Y    =   ',m_Y)


Sx1y= np.sum((CPUTime-m_X1)*(DiskIO-m_Y))
Sx2_sq= np.sum((memory-m_X2)**2)
Sx2y=np.sum((memory-m_X2)*(DiskIO-m_Y))
Sx1x2= np.sum((CPUTime-m_X1)* (memory-m_X2))
Sx1_sq= np.sum((CPUTime-m_X1)**2)

# calculating regression coefficients
b_1 = ((Sx1y*Sx2_sq)-(Sx2y*Sx1x2))/((Sx1_sq*Sx2_sq)- (Sx1x2**2))
b_2 = ((Sx2y*Sx1_sq)-(Sx1y*Sx1x2))/((Sx1_sq*Sx2_sq)- (Sx1x2**2))
b_0 = m_Y - b_1* m_X1 - b_2* m_X2
print('estimated coefficient\n')
print("intercept =   ", b_0)
print("beta_1  =   ", b_1)
print("beta_2  =   ", b_2)
# predicted response vector
y_pred = b_0 + b_1 * CPUTime + b_2 * memory
print('Y  =  ', b_0,' + ', b_1, ' *  X1', b_2, ' * X2')
TSS=np.sum((DiskIO- m_Y)**2)
RSS=np.sum((DiskIO- y_pred)**2)

MSS=np.sum((y_pred-m_Y)**2)
R_sq=MSS/TSS

print('Total Sum of Square       =  ', TSS)
print('Model Sum of Square       =  ', MSS)
print('Residual Sum of Square    = ', RSS)
print('Coefficient of determination = ', R_sq)

T_Df=n-1
k=3
M_Df=k-1
R_Df=n-k
MSReg=MSS/M_Df
MSErr=RSS/R_Df
F_test=MSReg/MSErr
v_b1=(MSErr*Sx2_sq)/((Sx1_sq*Sx2_sq)- (Sx1x2**2))
v_b2= (MSErr*Sx1_sq)  / ((Sx1_sq*Sx2_sq)- (Sx1x2**2))
v_b3= MSErr * ((1/n)+((m_X1 **2 )*Sx2_sq)+((m_X2**2)*Sx1_sq)-(2*m_X1* m_X2*Sx1x2))
print('Sigma__sq   =   ', MSErr)
print(' variance of b1    =   ', v_b1)
print('variance of b1    =   ', v_b2)
print('variance of b1    =   ', v_b3)


print(' F_Test  =   ', F_test)
plt.scatter(CPUTime, DiskIO, color="m", marker="o", s=30)

plt.scatter(memory, DiskIO, color="m", marker="o", s=30)
plt.plot(CPUTime, DiskIO, color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.plot(memory, DiskIO, color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
