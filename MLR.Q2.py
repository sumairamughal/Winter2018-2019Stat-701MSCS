import numpy as np
import matplotlib.pyplot as plt
X1 = np.array((0, 0, 10, 10, 20, 20))
X2=np.array((0,0,100,100,400,400))
Y = np.array((5, 7, 15, 17, 9, 11))
# number of observations/points
n = np.size(X1)

# mean of x and y vector
m_X1, m_X2, m_Y = np.mean(X1),np.mean(X2), np.mean(Y)
print('Mean of X1   =  ',m_X1)
print('Mean of X2   =   ',m_X1)
print('Mean of Y    =   ',m_Y)


Sx1y= np.sum((X1-m_X1)*(Y-m_Y))
Sx2_sq= np.sum((X2-m_X2)**2)
Sx2y=np.sum((X2-m_X2)*(Y-m_Y))
Sx1x2= np.sum((X1-m_X1)* (X2-m_X2))
Sx1_sq= np.sum((X1-m_X1)**2)

# calculating regression coefficients
b_1 = ((Sx1y*Sx2_sq)-(Sx2y*Sx1x2))/((Sx1_sq*Sx2_sq)- (Sx1x2**2))
b_2 = ((Sx2y*Sx1_sq)-(Sx1y*Sx1x2))/((Sx1_sq*Sx2_sq)- (Sx1x2**2))
b_0 = m_Y - b_1* m_X1 - b_2* m_X2
print('estimated coefficient\n')
print("intercept =   ", b_0)
print("beta_1  =   ", b_1)
print("beta_2  =   ", b_2)
# predicted response vector
y_pred = b_0 + b_1 * X1 + b_2 * X2
print('Y  =  ', b_0,' + ', b_1, ' *  X1', b_2, ' * X2')
TSS=np.sum((Y- m_Y)**2)
RSS=np.sum((Y- y_pred)**2)

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
plt.scatter(X1, Y, color="m", marker="o", s=30)

plt.scatter(X2, Y, color="m", marker="o", s=30)
plt.plot(X1, Y, color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.plot(X2, Y, color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
