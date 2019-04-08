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

rec = path.abspath('..'+'\\fig\\22.xlsx')
for sheet_name in range(1,6):
	df=read(rec, sheet_name=sheet_name)
	x=array(df['x'])
	y=array(df['y'])
	g = polyfit(x,y,2)
	f=poly1d(g)
	t=linspace(x[0],x[-1],10000)
	loglog(t,f(t),label='аппроксимация',color='darkblue')

ylabel(r'$\mathscr{E}_H$, \text{мВ}',fontsize=16)
xlabel(r'$I, \text{мА}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
legend()
# savefig(path.abspath('..'+'\\fig\\541.pdf'))


show()