import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
		                               AutoMinorLocator)


def func(a,b,c,d,t):
	ff=a/t*np.log(t/b)+c/t+0.0558118059*np.sin(d*np.pi/180.0)
	return ff



plt.rc('font', family='serif')
#plt.rc('xtick', labelsize='x-small')
#plt.rc('ytick', labelsize='x-small')
plt.rcParams.update({'font.size': 15})
plt.rc('xtick', labelsize=17)
plt.rc('ytick', labelsize=17)
fig = plt.figure(figsize=(7.2, 7.2))
ax=fig.add_subplot(111)
(ax1,ax2,ax3) = fig.subplots(3)
#ax2 = fig.subplots(2,sharex=True)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(direction='in',labelcolor='w', top='off', bottom='off', left='off', right='off')



#plt.grid(True)
#ax.xaxis.grid(True, which='minor')
#ax.grid(alpha=0.5,color='k',linestyle='dashed',linewidth=0.5)
plt.tight_layout(True)
#yticks = np.arange(-50, 30, 10)
#xticks = np.arange(-500, 550, 200)
#x = np.linspace(1., 8., 30)
#fp=open("d110p111.txt","r")
#line=fp.readlines()
#x=[]
#y=[]
#for i in range(len(line)):
#	x.append(np.float(line[i].split()[0]))
#	y.append(np.float(line[i].split()[1]))


fp=open("dft0001Re.txt","r")
line=fp.readlines()
x1=[]
y1=[]
for i in range(len(line)):
	x1.append(np.float(line[i].split()[0]))
	y1.append(np.float(line[i].split()[1]))


fp1=open("pres0001Re.txt","r")
line1=fp1.readlines()
x2=[]
y2=[]
for i in range(len(line1)):
	x2.append(np.float(line1[i].split()[0]))
	y2.append(np.float(line1[i].split()[1]))

fp2=open("eam0001Re.txt","r")
line2=fp2.readlines()
x3=[]
y3=[]
for i in range(len(line2)):
	x3.append(np.float(line2[i].split()[0]))
	y3.append(np.float(line2[i].split()[1]))

fpp=open("dft1010Re.txt","r")
linep=fpp.readlines()
xx1=[]
yy1=[]
for i in range(len(linep)):
	xx1.append(np.float(linep[i].split()[0]))
	yy1.append(np.float(linep[i].split()[1]))

fpp1=open("pres1010Re.txt","r")
linep1=fpp1.readlines()
xx2=[]
yy2=[]

for i in range(len(linep1)):
	xx2.append(np.float(linep1[i].split()[0]))
	yy2.append(np.float(linep1[i].split()[1]))

fpp2=open("eam1010Re.txt","r")
linep2=fpp2.readlines()
xx3=[]
yy3=[]
for i in range(len(linep2)):
	xx3.append(np.float(linep2[i].split()[0]))
	yy3.append(np.float(linep2[i].split()[1]))


fpp3=open("dft1210Re.txt","r")
linep3=fpp3.readlines()
xx4=[]
yy4=[]

for i in range(len(linep3)):
	xx4.append(np.float(linep3[i].split()[0]))
	yy4.append(np.float(linep3[i].split()[1]))
fpp4=open("pres1210Re.txt","r")
linep4=fpp4.readlines()
xx5=[]
yy5=[]
for i in range(len(linep4)):
	xx5.append(np.float(linep4[i].split()[0]))
	yy5.append(np.float(linep4[i].split()[1]))
fpp5=open("eam1210Re.txt","r")
linep5=fpp5.readlines()
xx6=[]
yy6=[]
for i in range(len(linep5)):
	xx6.append(np.float(linep5[i].split()[0]))
	yy6.append(np.float(linep5[i].split()[1]))

ax1.plot(x1, y1,color='black',linewidth=2.0,markersize=8,label='DFT')
ax1.plot(x2, y2,color='red',linewidth=2.0,markersize=8,label='P-MEAM')
ax1.plot(x3, y3,color='blue',linewidth=2.0,markersize=8,label='EAM')
ax2.plot(xx1, yy1,color='black',linewidth=2.0,markersize=8,label='DFT')
ax2.plot(xx2, yy2,color='red',linewidth=2.0,markersize=8,label='P-MEAM')
ax2.plot(xx3, yy3,color='blue',linewidth=2.0,markersize=8,label='EAM')
ax3.plot(xx4, yy4,color='black',linewidth=2.0,markersize=8,label='DFT')
ax3.plot(xx5, yy5,color='red',linewidth=2.0,markersize=8,label='P-MEAM')
ax3.plot(xx6, yy6,color='blue',linewidth=2.0,markersize=8,label='EAM')
ax1.text(3, 40, '(0001)', {'color': 'black', 'fontsize': 13})
ax2.text(3, 40, '(1010)', {'color': 'black', 'fontsize': 13})
ax3.text(3, 40, '(1210)', {'color': 'black', 'fontsize': 13})


#ax1.plot(x, x ** 1.5, color='k', ls='solid',linewidth=2.0,markersize=6)
#ax1.plot(x, 20/x, color='0.50', ls='dashed',linewidth=2.0,markersize=6)
#ax2.plot(x, x ** 1.5, color='k', ls='solid',linewidth=2.0,markersize=6)
#ax2.plot(x, 20/x, color='0.50', ls='dashed',linewidth=2.0,markersize=6)
#ax1.set_xlabel('Displacement (u/b)',size=17)
#ax1.set_ylabel('Energy/Area (meV/$\AA^2$)',size=17)
#plt.savefig('test.png')
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())

ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())

ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())

#ax.xaxis.set_major_locator()
#ax.yaxis.set_major_locator()
#plt.legend(fontsize=13,loc=0)
#ax.tick_params(direction='in', length=6, width=2, colors='r',grid_color='r', grid_alpha=0.5)

ax1.set_xlim(0, 6, 1)
ax2.set_xlim(0, 6, 1)
ax3.set_xlim(0, 6, 1)

ax1.legend(fontsize=13,loc=0)
ax2.legend(fontsize=13,loc=0)
ax3.legend(fontsize=13,loc=0)

ax1.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax1.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax1.tick_params(axis='x',which='minor', length=3)
ax1.tick_params(axis='y',which='minor', length=3)
#ax1.set_xticklabels([])

ax2.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax2.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax2.tick_params(axis='x',which='minor', length=3)
ax2.tick_params(axis='y',which='minor', length=3)

ax3.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax3.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax3.tick_params(axis='x',which='minor', length=3)
ax3.tick_params(axis='y',which='minor', length=3)

#ax.set_title(plot_title,fontsize=17, loc="left", pad=30)
#ax.set_xlabel('Displacement (u/b)',size=17)
ax.yaxis.set_label_coords(-0.12, 0.5)
ax.set_xlabel('Displacement [$\AA$]',size=17,style='italic')
ax.set_ylabel('Tensile stress [GPa]',size=17,style='italic')
plt.savefig('trachcp.eps')
plt.show()
