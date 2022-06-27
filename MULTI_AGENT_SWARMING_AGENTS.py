import matplotlib.pyplot as plt
import numpy as np
	

v0           = 0.5     
eta          = 0.6     
L            = 5       
R            = 0.5      
dt           = 0.1    
Nt           = 200      
N            = 300      
plotRealTime = True


np.random.seed(30)     


x = np.random.rand(N,1)*L
y = np.random.rand(N,1)*L


theta = 2 * np.pi * np.random.rand(N,1)
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)


fig = plt.figure(figsize=(6,6), dpi=96)
ax = plt.gca()


for i in range(Nt):

	
	x += vx*dt
	y += vy*dt
	
	
	x = x % L
	y = y % L
	
	
	mean_theta = theta
	for b in range(N):
		neighbors = (x-x[b])**2+(y-y[b])**2 < R**2
		sx = np.sum(np.cos(theta[neighbors]))
		sy = np.sum(np.sin(theta[neighbors]))
		mean_theta[b] = np.arctan2(sy, sx)
		
	
	theta = mean_theta + eta*(np.random.rand(N,1)-0.5)
	

	vx = v0 * np.cos(theta)
	vy = v0 * np.sin(theta)
	

	if plotRealTime or (i == Nt-1):
		plt.cla()
		plt.quiver(x,y,vx,vy,color='r')
		ax.set(xlim=(0, L), ylim=(0, L))
		ax.set_aspect('equal')	
		plt.pause(0.001)
			

plt.savefig('activematter.png',dpi=240)
plt.show()