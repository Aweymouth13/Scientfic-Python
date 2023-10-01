import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy import constants as const
import csv

G = const.G.value
c = 3e8
solar_mass = 1.9885e30
n = 100

mean_pos = 5 * 1.496e11
std_pos = 1 * 1.496e11
pos = np.random.normal(mean_pos, std_pos, (n, 3))

mean_vel = 250000
std_vel = 50000
vel = np.random.normal(mean_vel, std_vel, (n, 3))

mean_mass = solar_mass
std_mass = 0.1 * solar_mass
mass = np.random.normal(mean_mass, std_mass, n)

csv_data = []
dt = 10000

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
norm_mass = (mass - np.min(mass)) / (np.max(mass) - np.min(mass))
colors = plt.cm.viridis(norm_mass)
sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], s=mass / 1e28, c=colors)

def update(frame, ax, sc):
    global pos, vel, csv_data

    dx = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
    distance = np.sqrt(np.sum(dx ** 2, axis=-1)) + 1e-9
    force = G * mass[:, np.newaxis, np.newaxis] * mass[np.newaxis, :, np.newaxis] * dx / (distance[:, :, np.newaxis] ** 3)
    for i in range(n):
        force[i, i, :] = 0.0

    net_force = np.sum(force, axis=1)
    vel += net_force * dt / mass[:, np.newaxis]
    pos += vel * dt

    ax.clear()
    norm_mass = (mass - np.min(mass)) / (np.max(mass) - np.min(mass))
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)

    for i in range(len(pos)):
        ax.quiver(pos[i, 0], pos[i, 1], pos[i, 2], vel[i, 0], vel[i, 1], vel[i, 2], length=1e10, normalize=True, color=colors[i])
        csv_data.append([i, mass[i], pos[i, 0], pos[i, 1], pos[i, 2], vel[i, 0], vel[i, 1], vel[i, 2], frame, dt])

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    return sc,

ani = animation.FuncAnimation(fig, update, fargs=(ax, sc), frames=100000, interval=50)
plt.show()

with open('data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'])
    csv_writer.writerows(csv_data)
