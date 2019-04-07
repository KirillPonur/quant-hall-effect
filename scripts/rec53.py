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


sheet_name='5.3'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)

figure(sheet_name)
x=array(df['I'])
y=array(df['U'])
g = polyfit(x,y,9)
y=poly1d(g)
x=linspace(x[0],x[-1],100)

plot(x,y(x),label='аппроксимация',color='darkblue')
plot(df['I'],df['U'],'r.',label='эксперимент')
ylabel(r'$\mathscr{E}_H$, \text{мВ}',fontsize=16)
xlabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
savefig(path.abspath('..'+'\\fig\\53.pdf'))

show()