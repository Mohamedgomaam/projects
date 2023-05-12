#code of question 11 using MSE
ylabel=[1,-1,1,-1]
x1=[0.2,0.1,0.4,0.6]
x2=[0.5,0.3,0.8,0.4]
x3=[0.7,0.6,0.2,0.9]
w1=-0.5
w2=0.1
w3=0.4
b=0.2
alpha=0.01
j=0
error=0
error1=0
error2=0
error3=0
k=3
number_of_iteration=564
print("value of w1 : ", w1, "\n value of w2 : ", w2, "\n value of w3 : ", w3, "\n value of b : ", b)
for i in range(number_of_iteration):
    def update_wight(j, w1, w2, w3,b,error,error1,error2,error3):
        w1 = w1 + (alpha * error1)
        w2 = w2 + (alpha * error2)
        w3 = w3 + (alpha * error3)
        b = b + (alpha * error)
        return w1, w2, w3,b
    def sign(z):
        if z > 0:
            return 1
        elif z < 0:
            return -1
        else:
            return 0
    zj = (x1[j] * w1) + (x2[j] * w2) + (x3[j] * w3) + b
    print("predicted value : ",zj)
    y_hat = sign(zj)
    error=error+(ylabel[j]-y_hat)
    error1 = error1+((ylabel[j]-y_hat)*x1[j])
    error2 = error2+((ylabel[j]-y_hat)*x2[j])
    error3 = error3+((ylabel[j]-y_hat)*x3[j])
    if i==k:
        if error!=0 or error1!= 0 or error2!=0 or error3!=0:
            error=error/ (len(x1))
            error1= error1 / (len(x1))
            error2= error2 / (len(x1))
            error3= error3 / (len(x1))
            w1, w2, w3, b = update_wight(j, w1, w2, w3, b,error,error1,error2,error3)
            print("\n value of w1 : ",w1,"\n value of w2 : ", w2,"\n value of w3 : ", w3,"\n value of b : ", b)
            error=0
            error1=0
            error2=0
            error3=0
    if i==k :
        j=0
        k=k+4
    else:
        j=j+1
    print()
#if we put number of iteration=4000 we will reach the solution
'''
#this code of question 11 but without the MSE it work buy the basic error calculation 
ylabel=[1,-1,1,-1]
x1=[0.2,0.1,0.4,0.6]
x2=[0.5,0.3,0.8,0.4]
x3=[0.7,0.6,0.2,0.9]
w1=-0.5
w2=0.1
w3=0.4
b=0.2
alpha=0.01
j=0
error=0
error1=0
error2=0
error3=0
k=3
number_of_iteration=8
print("value of w1 : ", w1, "\n value of w2 : ", w2, "\n value of w3 : ", w3, "\n value of b : ", b)
for i in range(number_of_iteration):
    def update_wight(j, w1, w2, w3,b,error):
        w1 = w1 + (alpha * error*x1[j])
        w2 = w2 + (alpha * error*x2[j])
        w3 = w3 + (alpha * error*x3[j])
        b = b + (alpha * error)
        return w1, w2, w3,b
    def sign(z):
        if z > 0:
            return 1
        elif z < 0:
            return -1
        else:
            return 0
    zj = (x1[j] * w1) + (x2[j] * w2) + (x3[j] * w3) + b
    print("predicted value : ",zj)
    y_hat = sign(zj)
    error=(ylabel[j]-y_hat)
    if error!=0 :
            w1, w2, w3, b = update_wight(j, w1, w2, w3, b,error)
            print("value of w1 : ",w1,"\n value of w2 : ", w2,"\n value of w3 : ", w3,"\n value of b : ", b)
            error=0
    if i==k :
        j=0
        k=k+4
    else:
        j=j+1
    print()
'''