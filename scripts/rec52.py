from pylab import *
from matplotlib import rc

import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}',
                        r'\usepackage{mathrsfs}'])


rc('font', family='serif')


sheet_name='5.2'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)

figure(sheet_name)
y=array(df['I'])
x=array(df['U'])
g = polyfit(x,y,1)
y=poly1d(g)
a,b,d= 22e-3, 0.38e-3 , 3.5e-3
R=1/g[0]
print('Сопротивление образца R=',R)
rho=R*b*d/a
print('Удельное Сопротивление rho=', rho)
print('Удельная проводимость sigma=',1/rho)
x=linspace(0,x[-1],1000)

plot(x,y(x),label='аппроксимация',color='darkblue')
plot(df['U'],df['I'],'r.',label='эксперимент')
xlabel(r'$U$, \text{мВ}',fontsize=16)
ylabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
savefig(path.abspath('..'+'\\fig\\52.pdf'))
print(path.abspath('..'))
show()