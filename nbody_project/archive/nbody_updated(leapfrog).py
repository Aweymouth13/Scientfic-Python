import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy import constants as const
import csv

G = const.G.value
n = 10

mean_pos = 5 * 1.496e11
std_pos = 1 * 1.496e11
pos = np.random.normal(mean_pos, std_pos, (n, 3))

mean_vel = 250000
std_vel = 50000
vel = np.random.normal(mean_vel, std_vel, (n, 3))

mean_mass = 1.9885e30
std_mass = 0.1 * mean_mass
mass = np.random.normal(mean_mass, std_mass, n)

csv_data = []
dt = 5000  # Smaller time step
softening = 1e-9  # Softening factor

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = plt.cm.viridis((mass - np.min(mass)) / (np.max(mass) - np.min(mass)))
sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)


def get_forces(pos, mass):
    dx = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
    distance = np.sqrt(np.sum(dx ** 2, axis=-1)) + 1e-9
    force = G * mass[:, np.newaxis, np.newaxis] * mass[np.newaxis, :, np.newaxis] * dx / (distance[:, :, np.newaxis] ** 3)
    for i in range(force.shape[0]):
        force[i, i, :] = 0.0  # Manually setting diagonal to zero
    net_force = np.sum(force, axis=1)
    return net_force



def update(frame, ax, sc):
    global pos, vel, dt, csv_data

    # Leapfrog integration
    half_dt = 0.5 * dt
    net_force = get_forces(pos, mass)
    vel += half_dt * net_force / mass[:, np.newaxis]
    pos += dt * vel
    net_force = get_forces(pos, mass)
    vel += half_dt * net_force / mass[:, np.newaxis]

    ax.clear()
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')

    for i in range(len(pos)):
        csv_data.append([i, mass[i], pos[i, 0], pos[i, 1], pos[i, 2], vel[i, 0], vel[i, 1], vel[i, 2], frame, dt])

    return sc,


ani = animation.FuncAnimation(fig, update, fargs=(ax, sc), frames=100000, interval=50)
plt.show()

with open('data1.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'])
    csv_writer.writerows(csv_data)
