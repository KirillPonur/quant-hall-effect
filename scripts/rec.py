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

rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name='5.4, I=1mA')

figure('5.4, I=1mA')
x=array(df['I'])
y=array(df['E'])*1000
g = polyfit(x,y,1)
y=poly1d(g)
x=linspace(x[0],x[-1],1000)

plot(x,y(x),label='аппроксимация',color='darkblue')
plot(df['I'],df['E']*1000,'r.',label='эксперимент')
ylabel(r'$\mathscr{E}_H$, \text{мВ}',fontsize=16)
xlabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
savefig(path.abspath('..'+'\\fig\\541.pdf'))

df=read(rec, sheet_name='5.4, I=2mA')
figure('5.4, I=2mA')
x=array(df['I'])
y=array(df['E'])*1000
g = polyfit(x,y,1)
y=poly1d(g)
x=linspace(x[0],x[-1],1000)

plot(x,y(x),label='аппроксимация',color='darkblue')
plot(df['I'],df['E']*1000,'r.',label='эксперимент')
ylabel(r'$\mathscr{E}_H$, \text{мВ}',fontsize=16)
xlabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
savefig(path.abspath('..'+'\\fig\\542.pdf'))

df=read(rec, sheet_name='5.4, I=7mA')
figure('5.4, I=7mA')
x=array(df['I'])
y=array(df['E'])*1000
g = polyfit(x,y,1)
y=poly1d(g)
x=linspace(x[0],x[-1],1000)

plot(x,y(x),label='аппроксимация',color='darkblue')
plot(df['I'],df['E']*1000,'r.',label='эксперимент')
ylabel(r'$\mathscr{E}_H$, \text{мВ}',fontsize=16)
xlabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
savefig(path.abspath('..'+'\\fig\\547.pdf'))

show()