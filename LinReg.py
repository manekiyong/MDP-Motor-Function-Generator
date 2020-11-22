import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def predictor(fileName):
    try:
        mainDF = pd.read_excel(fileName)
    except:
        print("Canont load Spreadsheet!")
        return
    m1 = mainDF.iloc[:,0]
    m2 = mainDF.iloc[:,1]
    spd = mainDF.iloc[:,2]
    m1r= mainDF.iloc[:,4]
    m2r = mainDF.iloc[:,5]
    spdr = mainDF.iloc[:,6]
    regr_L = rpm2spd(m1,spd)
    grad_L,coeff_L = regr_L.coef_[0] , regr_L.intercept_
    regr_R = rpm2spd(m2,spd)
    grad_R, coeff_R = regr_R.coef_[0],regr_R.intercept_
    regr_rL = rpm2spd(m1r,spdr)
    grad_rL,coeff_rL = regr_rL.coef_[0] , regr_rL.intercept_
    regr_rR = rpm2spd(m2r,spdr)
    grad_rR, coeff_rR = regr_rR.coef_[0],regr_rR.intercept_
    params = {  "grad_L":grad_L,
                "coeff_L":coeff_L,
                "grad_R":grad_R,
                "coeff_R":coeff_R,
                "grad_rL":grad_rL,
                "coeff_rL":coeff_rL,
                "grad_rR":grad_rR,
                "coeff_rR":coeff_rR
                }
    funcPrinter(params)
    return
    
def rpm2spd(x,y):
    regr = linear_model.LinearRegression()
    regr.fit(np.array(x).reshape(-1,1),np.array(y))
    # The coefficients
    # print('Coefficients: \n', regr.coef_)
    # print('Intercepts: \n', regr.intercept_)
    return regr

def funcPrinter(params):
    print("\n")
    print("int leftRPMToSpeed(double rpm, bool dir){ //dir: True=Forward, False=Reverse ")
    print("\tdouble setspd;")
    print("\tif(dir)")
    print("\t\tsetspd = rpm*"+str(params['grad_L'])+"+"+str(params['coeff_L'])+";")
    print("\telse")
    print("\t\tsetspd = rpm*"+str(params['grad_rL'])+"+"+str(params['coeff_rL'])+";")
    print("\treturn int(round(setspd));")
    print("}")
    print("int rightRPMToSpeed(double rpm, bool dir){ //dir: True=Forward, False=Reverse ")
    print("\tdouble setspd;")
    print("\tif(dir)")
    print("\t\tsetspd = rpm*"+str(params['grad_R'])+"+"+str(params['coeff_R'])+";")
    print("\telse")
    print("\t\tsetspd = rpm*"+str(params['grad_rR'])+"+"+str(params['coeff_rR'])+";")
    print("\treturn int(round(setspd));")
    print("}")
    print("\n")

