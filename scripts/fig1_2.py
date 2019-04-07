from pylab import *
from matplotlib import rc
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

# rec = path.abspath('..'+'\\rec\\rec.xlsx')

# df=read(rec, sheet_name='1')

# figure('Задание 1')
# z=df['Цена деления, В']
# x=array(df['f'])
# y=array(df['U'])/max(df['U'])
# g = interpolate.interp1d(x,y, 'quadratic' )
# x=linspace(x[0],x[-1],1000)
# y=g(x)
# plot(x,y,label='интерполяция')
# plot(df['f'],df['U']/max(df['U']),'ro',label='эксперимент')
# xlabel(r'$f$, \text{кГц}',fontsize=16)
# ylabel(r'$K(f)=\frac{U_{\text{вых}}}{U^{m}_{\text{вых}}}$, ',fontsize=16)
# grid(which='major', linestyle='-')
# grid(which='minor', linestyle=':')
# minorticks_on()
# legend()
# savefig(path.abspath('..'+'\\fig\\task1.pdf'))


global a,M1,M2,beta
a=0.5
M1=1
M2=4
beta=1
def omega0():
	
	omega0=sqrt(2*beta)*(M1+M2)/(M1+M2)
	return omega0

def gamma():
	gamma=sqrt(4*(M1*M2)/(M1+M2)**2)
	print(gamma)
	return gamma

def optic_branch(q):
	omega=omega0()
	omega1=sqrt(omega**2/2)*sqrt(1+sqrt(1-gamma()**2*sin(a*q/2)**2))
	return omega1

def acoustic_branch(q):
	omega=omega0()
	omega2=sqrt(omega**2/2)*sqrt(1-sqrt(1-gamma()**2*sin(a*q/2)**2))
	return omega2
q=linspace(-pi/a,pi/a,10000)
plot(q,optic_branch(q),label='оптическая ветвь',color='red')
plot(q,acoustic_branch(q),label='акустическая ветвь',color='darkblue')

ylabel(r'$\omega$ ',fontsize=22)
axvline(pi/a,color='black',linestyle=':')
axvline(-pi/a,color='black',linestyle=':')
legend(fontsize=14)
yticks([])
xticks([-pi/a,0,pi/a],
	[r'$-\pi/a$','0',r'$\pi/a$'],
	fontsize='22')
savefig(path.abspath('..'+'\\fig\\fig1_2.pdf'))
# show()