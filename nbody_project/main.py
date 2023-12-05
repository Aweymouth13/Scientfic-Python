from typing import Tuple, List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import csv
from astropy import constants as const

def init_constants() -> Tuple[float, float, float, int]:
    G = const.G.value
    c = const.c.value
    solar_mass = const.M_sun.value
    n = 100
    return G, c, solar_mass, n

def init_states(n: int, mean_pos: float, std_pos: float, mean_vel: float, std_vel: float, alpha1=0.3, alpha2=1.3, alpha3=2.3, m0=1.989e28, m1=1.5912e29, m2=9.945e29, m3=2.386e32) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    pos = np.random.normal(mean_pos, std_pos, (n, 3))
    vel = np.random.normal(mean_vel, std_vel, (n, 3))

    # Kroupa IMF in kg
    masses = []
    for _ in range(n):
        x = np.random.uniform(0, 1)
        if x < 0.3:
            mass = (x / 0.3) ** (1 / alpha1) * m0
        elif x < 0.5:
            mass = ((x - 0.3) / 0.2) ** (1 / alpha2) * m1
        else:
            mass = ((x - 0.5) / 0.5) ** (1 / alpha3) * m2
        masses.append(mass)  # Already in kg

    mass = np.array(masses)

    return pos, vel, mass



def normalize_mass(mass: np.ndarray) -> np.ndarray:
    return (mass - np.min(mass)) / (np.max(mass) - np.min(mass))

def init_plot(pos: np.ndarray, mass: np.ndarray) -> Tuple:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    norm_mass = normalize_mass(mass)
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)
    return fig, ax, sc

def update(frame: int, ax, sc, pos: np.ndarray, vel: np.ndarray, mass: np.ndarray, dt: int, csv_data: List[List], G: float) -> None:
    dx = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
    distance = np.sqrt(np.sum(dx ** 2, axis=-1)) + 1e-9
    force = G * mass[:, np.newaxis, np.newaxis] * mass[np.newaxis, :, np.newaxis] * dx / (distance[:, :, np.newaxis] ** 3)

    for i, _ in enumerate(mass):
        force[i, i, :] = 0.0

    net_force = np.sum(force, axis=1)
    vel += net_force * dt / mass[:, np.newaxis]
    pos += vel * dt

    redraw_plot(ax, sc, pos, mass, csv_data, frame, dt)

def redraw_plot(ax, sc, pos: np.ndarray, mass: np.ndarray, csv_data: List[List], frame: int, dt: int) -> None:
    ax.clear()
    norm_mass = normalize_mass(mass)
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)

    for i, (position, velocity) in enumerate(zip(pos, vel)):
        ax.quiver(*position, *velocity, length=1e10, normalize=True, color=colors[i])
        csv_data.append([i, mass[i], *position, *velocity, frame, dt])

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')

def write_csv(csv_data: List[List], csvfile) -> None:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'])
    csv_writer.writerows(csv_data)

if __name__ == '__main__':
    G, c, solar_mass, n = init_constants()
    pos, vel, mass = init_states(n, mean_pos=5 * const.au.value, std_pos=1 * const.au.value, mean_vel=250000, std_vel=50000)
    dt = 10000
    csv_data = []

    fig, ax, sc = init_plot(pos, mass)
    ani = animation.FuncAnimation(fig, update, fargs=(ax, sc, pos, vel, mass, dt, csv_data, G), frames=100000, interval=50)

    plt.show()

    with open('data_output/data.csv', 'w', newline='') as csvfile:
        write_csv(csv_data, csvfile)
