from apm import *  #  import APMonitor libraries
import matplotlib.pyplot as plt

z = apm_solve('grill',4)

print z

# plt.figure(1)
# plt.subplot(211)
plt.plot(z['time'],z['t'],'r:')
plt.ylabel('Firepot Temperature (K)')
plt.xlabel('Time (sec)')
plt.legend(['Temp'])
plt.show()

# plt.subplot(212)
# plt.plot(z['time'],z['m_fuel'],'r:')
# plt.plot(z['time'],z['m_wood_in'],'b--')
# plt.xlabel('Time (sec)')
# plt.ylabel('Mass (lb)')
# plt.legend(['Mass of pellets in pot','Pellet Feed Rate'])
