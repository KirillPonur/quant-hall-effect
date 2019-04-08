from pylab import *
from matplotlib import rc

import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
from math import *
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}',
                        r'\usepackage{mathrsfs}'])


rc('font', family='serif')

sheet_name='5.3'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
x=array(df['I'])/1000 # В Амперах
y=array(df['U'])
g = polyfit(x,y,9)
error=poly1d(g)
b=3.5/1000

sheet_name='5.6, B=200'
df=read(rec, sheet_name=sheet_name)

x=array(df['I'])/1000 # В Амперах 
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
print('Для B=200 Гс',(g[0]*b/200/10**4))
x=linspace(0,x[-1],100)

plot(x,y(x),label=r'$B=\text{200 Гс}$' )
plot(df['I']/1000,df['E'],'r.',label='_nolegend_')
ylabel(r'$\mathscr{E}_H$, \text{В}',fontsize=16)
xlabel(r'$I, \text{А}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
# savefig(path.abspath('..'+'\\fig\\56200.pdf'))

sheet_name='5.6, B=400'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)

# figure(sheet_name)
x=array(df['I1']) /1000
y=array(df['E1'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
print('Для B=400 Гс',g[0]*b/400/10**4)
x=linspace(0,x[-1],100)

plot(x,y(x),label=r'$B=\text{400 Гс}$' )
plot(df['I1']/1000,df['E1'],'r.',label='_nolegend_')
ylabel(r'$\mathscr{E}_H$, \text{В}',fontsize=16)
xlabel(r'$I, \text{А}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
# savefig(path.abspath('..'+'\\fig\\56400.pdf'))

sheet_name='5.6, B=600'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)

# figure(sheet_name)
x=array(df['I'])/1000 # В Амперах
y=array(df['E'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
print('Для B=600 Гс',g[0]*b/600/10**4)
x=linspace(0,x[-1],100)

plot(x,y(x),label=r'$B=\text{600 Гс}$' )
plot(df['I']/1000,df['E'],'r.',label='_nolegend_')
ylabel(r'$\mathscr{E}_H$, \text{В}',fontsize=16)
xlabel(r'$I, \text{А}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
# legend()
# savefig(path.abspath('..'+'\\fig\\56600.pdf'))


sheet_name='5.6, B=900'
rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)

# figure(sheet_name)
x=array(df['I'])/1000 # В Амперах
y=array(df['E'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
print('Для B=900 Гс',g[0]*b/900/10**4)
x=linspace(0,x[-1],100)

plot(x,y(x),label=r'$B=\text{900 Гс}$' )
plot(df['I']/1000,df['E'],'r.',label='_nolegend_')
ylabel(r'$\mathscr{E}_H$, \text{В}',fontsize=16)
xlabel(r'$I, \text{А}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
legend()
# savefig(path.abspath('..'+'\\fig\\56.pdf'))

show()