import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy import constants as const
import csv


def init_constants():
    G = const.G.value  # Gravitational constant in m^3 / (kg s^2)
    c = const.c.value  # Speed of light in m/s
    solar_mass = const.M_sun.value  # Solar mass in kg
    n = 100  # Number of bodies

    return G, c, solar_mass, n

def init_states(n, mean_pos=5 * 1.496e11, std_pos=1 * 1.496e11, mean_vel=250000, std_vel=50000, mean_mass=None, std_mass=None):
    pos = np.random.normal(mean_pos, std_pos, (n, 3))
    vel = np.random.normal(mean_vel, std_vel, (n, 3))
    mass = np.random.normal(mean_mass, std_mass, n) if mean_mass and std_mass else None
    return pos, vel, mass


def init_plot(pos, mass):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    norm_mass = (mass - np.min(mass)) / (np.max(mass) - np.min(mass))
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], s=mass / 1e28, c=colors)
    return fig, ax, sc

def update(frame, ax, sc, pos, vel, mass, dt, csv_data, G):
    dx = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
    distance = np.sqrt(np.sum(dx ** 2, axis=-1)) + 1e-9
    force = G * mass[:, np.newaxis, np.newaxis] * mass[np.newaxis, :, np.newaxis] * dx / (distance[:, :, np.newaxis] ** 3)

    for i in range(len(mass)):
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

def write_csv(csv_data):
    with open('data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'])
        csv_writer.writerows(csv_data)

if __name__ == '__main__':
    G, c, solar_mass, n = init_constants()
    pos, vel, mass = init_states(n, mean_mass=solar_mass, std_mass=0.1 * solar_mass)
    dt = 10000
    csv_data = []

    fig, ax, sc = init_plot(pos, mass)
    ani = animation.FuncAnimation(fig, update, fargs=(ax, sc, pos, vel, mass, dt, csv_data, G), frames=100000, interval=50)

    plt.show()
    write_csv(csv_data)

