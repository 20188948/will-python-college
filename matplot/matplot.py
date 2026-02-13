import matplotlib.pyplot as plt
import numpy as np

#xpoints=np.array([0,6])
#ypoints=np.array([0,250])

#change axis 
#xpoints=np.array([20,100])
#ypoints=np.array([20,80])
#plt.plot(xpoints,ypoints,'o')


#markers 
#ypoints=np.array([3,8,1,10])
#plt.plot(ypoints,marker = 'o')

#dotted line represneted by : and colour red by r 
#plt.plot(ypoints,'o:r')

#marker size (ms) #marker colour (mec) # face colour (mfc)
#plt.plot(ypoints, marker = 'o', ms = 5,mec = 'g',mfc = 'hotpink')

#linestyle and color and linewidth
#plt.plot(ypoints, linestyle= 'dashdot',color = 'r',linewidth=40)



#plotting two lines 
#x1=np.array([0,1,2,3])
#y1=np.array([3,8,1,10])
#x2=np.array([0,1,2,3])
#y2=np.array([6,2,7,11])
#plt.plot(x1,y1,x2,y2)

#for two lines
#plt.plot(y1)
#plt.plot(y2)


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.xlabel('Average pulse')
plt.ylabel('Calorie burnage')
plt.title('sports watch data')


print(plt.show())
plt.savefig('Graph.png')