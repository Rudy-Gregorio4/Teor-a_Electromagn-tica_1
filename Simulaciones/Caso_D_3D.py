import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# Given data
data = {
    'X (m)': [0.25, 0.25, 0.25, 0.50, 0.50, 0.50, 0.75, 0.75, 0.75],
    'Y (m)': [0.25, 0.50, 0.75, 0.25, 0.50, 0.75, 0.25, 0.50, 0.75],
    'V(x,y) (Volts)': [0.000545, 0.00145, 0.00328, 0.000771, 0.00204, 0.00464, 0.000545, 0.00145, 0.00328]
}

# Create a grid for interpolation
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Interpolate using griddata
grid_z = griddata((data['X (m)'], data['Y (m)']), data['V(x,y) (Volts)'], (grid_x, grid_y), method='cubic')

# 2D Plot
plt.figure(figsize=(8, 7))
contour = plt.contourf(grid_x, grid_y, grid_z, levels=15, cmap='viridis')
plt.scatter(data['X (m)'], data['Y (m)'], color='red')  # data points
for i, txt in enumerate(data['V(x,y) (Volts)']):
    plt.annotate(f"{txt:.7f} V", (data['X (m)'][i], data['Y (m)'][i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.colorbar(contour)
plt.title('Electric Potential Distribution (2D) Case "D"')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)
plt.show()

# 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis', edgecolor='none')
ax.scatter(data['X (m)'], data['Y (m)'], data['V(x,y) (Volts)'], color='red')
for i, txt in enumerate(data['V(x,y) (Volts)']):
    ax.text(data['X (m)'][i], data['Y (m)'][i], data['V(x,y) (Volts)'][i], f"{txt:.7f} V", color='black')
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Voltage (V)')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('V (Volts)')
ax.set_title('3D Electric Potential Distribution, Case "D"')
plt.show()
