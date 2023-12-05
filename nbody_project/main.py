from typing import Tuple, List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import csv
from astropy import constants as const


def init_constants() -> Tuple[float, float, float, int]:
    """
    Initialize and return physical constants using astropy constants and a default parameter.

    Returns:
        Tuple[float, float, float, int]: A tuple containing:
            - G (float): the gravitational constant in m^3 kg^-1 s^-2
            - c (float): the speed of light in vacuum in m s^-1
            - solar_mass (float): the mass of the sun in kilograms
            - n (int): parameter for the number of bodies
    """
    G = const.G.value
    c = const.c.value
    solar_mass = const.M_sun.value
    n = 20
    return G, c, solar_mass, n


def init_states(n: int, mean_pos: float, std_pos: float, mean_vel: float, std_vel: float, alpha1=0.3, alpha2=1.3, alpha3=2.3, m0=1.989e28, m1=1.5912e29, m2=9.945e29, m3=2.386e32) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Initialize the states of 'n' bodies with position, velocity, and mass.

    Args:
        n (int): number of bodies.
        mean_pos (float): mean of the Gaussian distribution for position (user entered)
        std_pos (float): standard deviation of the Gaussian distribution for position (user entered)
        mean_vel (float): mean of the Gaussian distribution for velocity (user entered)
        std_vel (float): Standard deviation of the Gaussian distribution for velocity (user entered)
        alpha1, alpha2, alpha3 (float, optional): Parameters for the Kroupa initial mass function
        m0, m1, m2, m3 (float, optional): Mass scales used in the Kroupa initial mass function

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing:
            - pos (np.ndarray): Array of positions for each body, shaped (n, 3)
            - vel (np.ndarray): Array of velocities for each body, shaped (n, 3)
            - mass (np.ndarray): Array of masses for each body, shaped (n,)
    """
    pos = np.random.normal(mean_pos, std_pos, (n, 3))
    vel = np.random.normal(mean_vel, std_vel, (n, 3))

    #kroupa IMF in kg
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
    """
    Normalize the mass values in an array to a scale of 0 to 1

    Args:
        mass (np.ndarray): array of mass values

    Returns:
        np.ndarray: the normalized array of mass values, where the minimum mass
                    is scaled to 0 and the maximum mass to 1
    """
    return (mass - np.min(mass)) / (np.max(mass) - np.min(mass))


def init_plot(pos: np.ndarray, mass: np.ndarray) -> Tuple:
    """
    Initialize a 3D scatter plot with positions and mass-based color coding

    Args:
        pos (np.ndarray): A 2D array of positions for each point, with shape (n, 3), 
                          where 'n' is the number of points and 3 represents the x, y, and z coordinates.
        mass (np.ndarray): A 1D array of mass values for each point

    Returns:
        Tuple: A tuple containing the figure, axes, and scatter plot objects:
            - fig : the figure object for the plot
            - ax : the 3D axes object of the plot
            - sc : the scatter plot object
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    norm_mass = normalize_mass(mass)
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)
    return fig, ax, sc


def update(frame: int, ax, sc, pos: np.ndarray, vel: np.ndarray, mass: np.ndarray, dt: int, csv_data: List[List], G: float) -> None:
    """
    Update the positions and velocities of particles for each frame in a simulation and redraw the plot

    This function applies gravitational forces to update the velocities and positions of particles,
    then updates the scatter plot with the new positions

    Args:
        frame (int): the current frame number in the animation
        ax: the 3D axes object of the plot
        sc: the scatter plot object
        pos (np.ndarray): A 2D array of current positions of particles, shape (n, 3)
        vel (np.ndarray): A 2D array of current velocities of particles, shape (n, 3)
        mass (np.ndarray): A 1D array of mass values for each particle
        dt (int): time step for the simulation
        csv_data (List[List]): list to log data for each frame
        G (float): the gravitational constant

    Returns:
        None
    """
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
    """
    Redraw the plot for each frame of the simulation updating positions and velocities

    This function clears the existing plot, recalculates normalized mass for color coding,
    updates the scatter plot with new positions, and adds velocity vectors. It also logs
    data for each particle to a CSV list

    Args:
        ax: the 3D axes object of the plot
        sc: The scatter plot object
        pos (np.ndarray): A 2D array of current positions of particles, shape (n, 3)
        mass (np.ndarray): A 1D array of mass values for each particle
        csv_data (List[List]): list to log data for each frame
        frame (int): the current frame number in the animation
        dt (int): Time step for the simulation

    Returns:
        None
    """
    ax.clear()
    norm_mass = normalize_mass(mass)
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c=colors)

    for i, (position, velocity) in enumerate(zip(pos, vel)):
        ax.quiver(*position, *velocity, length=1e10, normalize=True, color=colors[i])
        csv_data.append([i, mass[i], *position, *velocity, frame, dt])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def write_csv(csv_data: List[List], csvfile) -> None:
    """
    Write simulation data to a CSV file

    This function writes a header row followed by rows of simulation data. Each row in the
    CSV file corresponds to the data for a single particle at a single frame

    Args:
        csv_data (List[List]): list of lists where each sublist contains data for a single particle
                               at a single frame. The data includes unique ID, mass, position (x, y, z),
                               velocity (x, y, z), frame number, and time step
        csvfile: pathw which the data will be written to

    Returns:
        None
    """
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
    

    with open('data.csv', 'w', newline='') as csvfile:
        write_csv(csv_data, csvfile)
