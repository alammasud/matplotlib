import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
		                               AutoMinorLocator)





plt.rc('font', family='serif')
#plt.rc('xtick', labelsize='x-small')
#plt.rc('ytick', labelsize='x-small')
plt.rcParams.update({'font.size': 15})
plt.rc('xtick', labelsize=17)
plt.rc('ytick', labelsize=17)
fig = plt.figure(figsize=(7.2, 7.2))
ax=fig.add_subplot(111)
(ax1,ax2) = fig.subplots(2)
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


fp=open("massen.txt","r")
line=fp.readlines()
x1=[]
y1=[]
for i in range(len(line)):
	x1.append(np.float(line[i].split()[0]))
	y1.append(np.float(line[i].split()[1]))


fp1=open("massen1.txt","r")
line1=fp1.readlines()
x2=[]
y2=[]
for i in range(len(line1)):
	x2.append(np.float(line1[i].split()[0]))
	y2.append(np.float(line1[i].split()[1]))

fp2=open("d112p111si.txt","r")
line2=fp2.readlines()
x3=[]
y3=[]
y4=[]
y5=[]
y6=[]
y7=[]
y8=[]
y9=[]
y10=[]
y11=[]
y12=[]

for i in range(len(line2)):
	x3.append(np.float(line2[i].split()[0]))
	y3.append(np.float(line2[i].split()[1]))
	y4.append(np.float(line2[i].split()[2]))
	y5.append(np.float(line2[i].split()[3]))
	y6.append(np.float(line2[i].split()[4]))
	y7.append(np.float(line2[i].split()[5]))
	y8.append(np.float(line2[i].split()[6]))
	y9.append(np.float(line2[i].split()[7]))


fter1=open("d112p111sitersoff.txt","r")
lineter1=fter1.readlines()

xter1=[]
yter1=[]

for i in range(len(lineter1)):
	xter1.append(np.float(lineter1[i].split()[0]))
	yter1.append(np.float(lineter1[i].split()[1]))

fter2=open("d110p111sitersoff.txt","r")
lineter2=fter2.readlines()
xter2=[]
yter2=[]

for i in range(len(lineter2)):
	xter2.append(np.float(lineter2[i].split()[0]))
	yter2.append(np.float(lineter2[i].split()[1]))



ax2.plot(x2, y2,'o-',color='black',linewidth=2.0,markersize=4,label='dft')
ax2.plot(x3, y3,'o-',color='red',linewidth=2.0,markersize=4,label='present')
ax2.plot(y4, y5,'o-',color='blue',linewidth=2.0,markersize=4,label='Baskes')
ax2.plot(y6, y7,'o-',color='green',linewidth=2.0,markersize=4,label='Bond-order')
ax2.plot(y8, y9,'o-',color='cyan',linewidth=2.0,markersize=4,label='SW')
ax2.plot(xter1,yter1,'o-',color='m',linewidth=2.0,markersize=4,label='Tersoff')

fp3=open("d110p111si.txt","r")

line3=fp3.readlines()
xx1=[]
yy1=[]
xx2=[]
yy2=[]
xx3=[]
yy3=[]
xx4=[]
yy4=[]

for i in range(len(line2)):
	xx1.append(np.float(line3[i].split()[0]))
	yy1.append(np.float(line3[i].split()[1]))
	xx2.append(np.float(line3[i].split()[2]))
	yy2.append(np.float(line3[i].split()[3]))
	xx3.append(np.float(line3[i].split()[4]))
	yy3.append(np.float(line3[i].split()[5]))
	xx4.append(np.float(line3[i].split()[6]))
	yy4.append(np.float(line3[i].split()[7]))

ax1.plot(x1,y1,'o-',color='black',markersize=4,linewidth=2.0,label='dft')
ax1.plot(xx1, yy1,'o-',color='r',linewidth=2.0,markersize=4,label='present')
ax1.plot(xx2, yy2,'o-',color='b',linewidth=2.0,markersize=4,label='Baskes')
ax1.plot(xx3, yy3,'o-',color='g',linewidth=2.0,markersize=4,label='Bond-order')
ax1.plot(xx4, yy4,'o-',color='c',linewidth=2.0,markersize=4,label='SW')
ax1.plot(xter2,yter2,'o-',color='m',linewidth=2.0,markersize=4,label='Tersoff')



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


#ax.xaxis.set_major_locator()
#ax.yaxis.set_major_locator()
#plt.legend(fontsize=13,loc=0)
#ax.tick_params(direction='in', length=6, width=2, colors='r',grid_color='r', grid_alpha=0.5)

ax1.set_xlim(0, 1, 1)
ax2.set_xlim(0, 1, 1)




ax1.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax1.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax1.tick_params(axis='x',which='minor', length=3)
ax1.tick_params(axis='y',which='minor', length=3)
#ax1.set_xticklabels([])

ax2.tick_params(axis='x',which='both',direction='in',length=6,width=1,top='on')
ax2.tick_params(axis='y',which='both',direction='in',length=6,width=1,right='on')
ax2.tick_params(axis='x',which='minor', length=3)
ax2.tick_params(axis='y',which='minor', length=3)

ax2.legend(fontsize=10,loc=0)
ax1.legend(fontsize=10,loc=0)
plt.text(0.1, 100,"(a)")
plt.text(0.1, 300,"(b)")
#plt.text(100, 0.14,"(c)")

ax.set_xlabel('Displacement (u/b)',size=17)
#ax.set_xlabel('{112} Facet length ($\AA$)',size=17)
ax.set_ylabel('Energy/Area (meV/$\AA^2$)',size=17)
plt.savefig('enervsub.png')
plt.show()
