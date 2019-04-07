from pylab import *
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read

sheet_name='5.2'
rec = path.abspath('.\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
y=array(df['I'])
x=array(df['U'])
g = polyfit(x,y,1)
y=poly1d(g)
resistance=1/g[0]
sheet_name='5.3'
rec = path.abspath('.\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
x=array(df['I']) # В Амперах
y=array(df['U'])
g = polyfit(x,y,9)
error=poly1d(g)
l,b,d= 22e-3, 0.38e-3 , 3.5e-3

rho=resistance*l/(d*b)
sigma=(1/rho)%10
R1=2.18*10**(-11)
R2=2.12*10**(-11)
R4=2.03*10**(-11)
R7=2.89*10**(-11)
R200= 1.88*10**(-11)
R400= 2.18*10**(-11)
R600= 1.93*10**(-11)
R900= 1.93*10**(-11)

R=array([R1,R2,R4,R7,R200,R400,R600,R900])
mu=mean(sigma*R)

A=3*pi/8
e=1.60217662e-19
n=A/mean(R)/e