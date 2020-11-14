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


fp=open("massen43.txt","r")
line=fp.readlines()
x1=[]
y1=[]
for i in range(len(line)):
	x1.append(np.float(line[i].split()[0]))
	y1.append(np.float(line[i].split()[1]))


fp1=open("massen60.txt","r")
line1=fp1.readlines()
x2=[]
y2=[]
for i in range(len(line1)):
	x2.append(np.float(line1[i].split()[0]))
	y2.append(np.float(line1[i].split()[1]))

fp2=open("massen70.txt","r")
line2=fp2.readlines()
x3=[]
y3=[]
for i in range(len(line2)):
	x3.append(np.float(line2[i].split()[0]))
	y3.append(np.float(line2[i].split()[1]))

fpi=open("infi43.txt","r")
linei=fpi.readlines()
x1i=[]
y1i=[]
for i in range(len(linei)):
	x1i.append(np.float(linei[i].split()[0]))
	y1i.append(np.float(linei[i].split()[1]))

fp1i=open("infi60.txt","r")
line1i=fp1i.readlines()
x2i=[]
y2i=[]
for i in range(len(line1i)):
	x2i.append(np.float(line1i[i].split()[0]))
	y2i.append(np.float(line1i[i].split()[1]))

fp2i=open("infi70.txt","r")
line2i=fp2i.readlines()
x3i=[]
y3i=[]
for i in range(len(line2i)):
	x3i.append(np.float(line2i[i].split()[0]))
	y3i.append(np.float(line2i[i].split()[1]))











fpp=open("fac43.txt","r")
linep=fpp.readlines()
xx1=[]
yy1=[]
for i in range(len(linep)):
	xx1.append(np.float(linep[i].split()[0]))
	yy1.append(np.float(linep[i].split()[1]))

fpp1=open("fac60.txt","r")
linep1=fpp1.readlines()
xx2=[]
yy2=[]

for i in range(len(linep1)):
	xx2.append(np.float(linep1[i].split()[0]))
	yy2.append(np.float(linep1[i].split()[1]))

fpp2=open("fac70.txt","r")
linep2=fpp2.readlines()
xx3=[]
yy3=[]
for i in range(len(linep2)):
	xx3.append(np.float(linep2[i].split()[0]))
	yy3.append(np.float(linep2[i].split()[1]))



ax1.plot(x1, y1, 'o--',color='green',linewidth=2.0,markersize=8,label='symmetric')
ax2.plot(x2, y2, 'o--',color='green',linewidth=2.0,markersize=8,label='symmetric')
ax3.plot(x3, y3, 'o--',color='green',linewidth=2.0,markersize=8,label='symmetric')
ax1.plot(x1i, y1i, '--',color='blue',linewidth=2.0,markersize=8,label='Asym')
ax2.plot(x2i, y2i, '--',color='blue',linewidth=2.0,markersize=8,label='Asym')
ax3.plot(x3i, y3i, '--',color='blue',linewidth=2.0,markersize=8,label='Asym')
ax1.plot(xx1, yy1, 'o',color='r',linewidth=2.0,markersize=8,label='Non-symmetric')
ax2.plot(xx2, yy2, 'o',color='r',linewidth=2.0,markersize=8,label='Non-symmetric')
ax3.plot(xx3, yy3, 'o',color='r',linewidth=2.0,markersize=8,label='Non-symmetric')
t1 = np.arange(10.0, 160.0, 0.1)
a=0.2503409745
b=1.3590137
c=0.0136930811
d=43.3138013697
ax1.plot(t1, func(a,b,c,d,t1),color='k',linewidth=2.0,markersize=4,label='(a)')

t2 = np.arange(30.0, 320.0, 0.1)

a=0.2503409745
b=1.1272955657
c=0.0136930811
d=62.0616013583
ax2.plot(t2, func(a,b,c,d,t2),color='k',linewidth=2.0,markersize=4,label='(b)')


a=0.2503409745
b=1.4414967097
c=0.0136930811
d=70.5287445063

ax3.plot(t2, func(a,b,c,d,t2),color='k',linewidth=2.0,markersize=4,label='(c)')





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

ax1.set_xlim(10, 160, 1)
ax2.set_xlim(30, 310, 1)
ax3.set_xlim(30, 310, 1)



ax1.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax1.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax1.tick_params(axis='x',which='minor', length=3)
ax1.tick_params(axis='y',which='minor', length=3)
#ax1.set_xticklabels([])
#plt.text(30, 0.08,"(a)")

ax2.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax2.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax2.tick_params(axis='x',which='minor', length=3)
ax2.tick_params(axis='y',which='minor', length=3)

ax3.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax3.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax3.tick_params(axis='x',which='minor', length=3)
ax3.tick_params(axis='y',which='minor', length=3)
plt.text(100, 0.07,"(c)")
plt.text(100, 0.105,"(b)")
plt.text(100, 0.14,"(a)")
#ax.set_title(plot_title,fontsize=17, loc="left", pad=30)
#ax.set_xlabel('Displacement (u/b)',size=17)
ax.yaxis.set_label_coords(-0.12, 0.5)
ax.set_xlabel('{112} Facet length ($\AA$)',size=17)
ax.set_ylabel('Energy/Area (eV/$\AA^2$)',size=17)
plt.savefig('enevsfacet.png')
plt.show()
