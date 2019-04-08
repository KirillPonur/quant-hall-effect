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
x=array(df['I']) # В Амперах
y=array(df['U'])
g = polyfit(x,y,9)
error=poly1d(g)
print(error(10))
b=3.5/1000


rec = path.abspath('..'+'\\rec\\rec.xlsx')
df=read(rec, sheet_name='5.4, I=1mA')

# figure('5.4, I=1mA')
x=array(df['I'])*773/10e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
print('Для I=1mA',g[0]*b/(1*10e-3))
y=poly1d(g)
x=linspace(0,x[-1],1000)

plot(x,y(x),label=r'$I=1\text{ мА}$')
plot(df['I']*773/10e4,df['E'],'r.',label='_nolegend_')

# legend()
# savefig(path.abspath('..'+'\\fig\\541.pdf'))




df=read(rec, sheet_name='5.4, I=4mA')
# figure('5.4, I=2mA')
x=array(df['I'])*773/10e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
print('Для I=4mA',g[0]*b/(4*10e-3))
y=poly1d(g)
x=linspace(0,x[-1],1000)

plot(x,y(x),label=r'$I=4\text{ мА}$')
plot(773*df['I']/10e4,df['E'],'r.',label='_nolegend_')

# legend()
# savefig(path.abspath('..'+'\\fig\\542.pdf'))

df=read(rec, sheet_name='5.4, I=7mA')
# figure('5.4, I=7mA')
x=array(df['I'])*773/10e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
print('Для I=7mA',g[0]*b/(7*10e-3))
y=poly1d(g)
x=linspace(0,x[-1],1000)

plot(x,y(x),label=r'$I=\text{7 мА}$')
plot(773*df['I']/10e4,df['E'],'r.',label='_nolegend_')
ylabel(r'$\mathscr{E}_H$, \text{В}',fontsize=16)
xlabel(r'$B, \text{Тл}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()


df=read(rec, sheet_name='5.4, I=2mA')
# figure('5.4, I=2mA')
x=array(df['I'])*773/10e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
print('Для I=2mA',g[0]*b/(2*10e-3))
y=poly1d(g)
x=linspace(0,x[-1],1000)

plot(x,y(x),label=r'$I=2\text{ мА}$')
plot(773*df['I']/10e4,df['E'],'r.',label='_nolegend_')


legend()
savefig(path.abspath('..'+'\\fig\\55.pdf'))


show()