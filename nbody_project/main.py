import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy import constants as const
import csv

"""
initializes and returns fundamental constants and number of bodies
it uses astropy to set value for gavitational constant, speed of light,
and the solar mass. the number of bodies is set to 100 by default.
The solar mass will be used for the gaussian distribution of the masses of the bodies.
returns tuple of values
"""
def init_constants():
    G = const.G.value  # Gravitational constant in m^3 / (kg s^2)
    c = const.c.value  # Speed of light in m/s
    solar_mass = const.M_sun.value  # Solar mass in kg
    n = 100  # Number of bodies

    return G, c, solar_mass, n


"""
initializes the initial states for the bodies in the simulation. the function takes in the number of bodies (n) and 
average parameters for mean and standard deviation for position, velocity, and mass.
positions (pos) are generated using a gaussian distribution centered around mean_pos with a standard deviation of
std_pos in 3D space. here, mean_pos=5 * 1.496e11 means the average starting position is about 5 astronomical units (AU)
from a reference point. std_pos=1 * 1.496e11 means the positions are scattered around that mean with a
standard deviation of 1 AU.
velocities (vel) are similarly generated in 3D space, centered around mean_vel with a standard deviation of std_vel.
masses (mass) are generated in the same way.
the function returns these initial states (pos, vel, mass) as a tuple.
"""

def init_states(n, mean_pos=5 * const.au.value, std_pos=1 * const.au.value, mean_vel=250000, std_vel=50000, mean_mass=None, std_mass=None):
    pos = np.random.normal(mean_pos, std_pos, (n, 3))
    vel = np.random.normal(mean_vel, std_vel, (n, 3))
    mass = np.random.normal(mean_mass, std_mass, n) if mean_mass and std_mass else None
    return pos, vel, mass



"""
initializes a 3D plot for visualizing the positions and masses 'particles'
using matplotlib for visulization, axis change dynamically with the simulation
norm_mass normalizes the mass values to a range between 0 and 1. this is used to assign colors to the plotted points.
colormap to convert the normalized mass to a color.
sc plots the positions (pos) in 3D space with sizes proportional to their mass (mass / 1e28) and colors based on colors.
the function returns the figure (fig), the axes (ax), and the scatter plot (sc) as a tuple for further manipulation.
"""

def init_plot(pos, mass):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    norm_mass = (mass - np.min(mass)) / (np.max(mass) - np.min(mass))
    colors = plt.cm.viridis(norm_mass)
    sc = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], s=mass / 1e28, c=colors)
    return fig, ax, sc

"""
updates the state and visualization of the simulation for each dt
the function takes in the current axes (ax), scatter plot (sc), positions (pos), velocities (vel), masses (mass), time step (dt), csv data (csv_data), and gravitational constant (G).

dx calculates the pairwise differences in positions between all bodies.
distance computes the pairwise distances, adding a small constant (softening) 1e-9 to avoid division by zero.
force calculates the gravitational force between all pairs using newton's law of gravitation.
the loop sets the force exerted by a body on itself to zero because physics.

net_force sums up the forces to get the net force on each body.
updates the velocities (vel) and positions (pos) using the calculated net forces and time step (dt).
clears the current axes (ax.clear()) and redraws the scatter plot with updated positions and colors.

the quiver plot shows the velocity vectors for each point.
csv_data.append() collects the current state for each body for later export to a CSV file.
finally, it sets the axis labels and returns the updated scatter plot (sc).
"""
def update(frame, ax, sc, pos, vel, mass, dt, csv_data, G):
    #difference in position between each pair
    dx = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
    #distance between each pair, sum them for euclidean distance, avoid division by zero
    distance = np.sqrt(np.sum(dx ** 2, axis=-1)) + 1e-9
    #gravitational force between each pair, indexing between every pair of bodies at once
    force = G * mass[:, np.newaxis, np.newaxis] * mass[np.newaxis, :, np.newaxis] * dx / (distance[:, :, np.newaxis] ** 3)
    #remove self force, n body can't exert force on itself
    for i in range(len(mass)):
        force[i, i, :] = 0.0
    #Net force on each body
    net_force = np.sum(force, axis=1)
    #eulers method to update velocities and positions, numerical solve of differential equation
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

"""
writes the simulation data to a csv file. it takes in a list of lists (csv_data), where each inner list contains the state information for a celestial body at a particular frame.
opens a new csv file called 'data.csv' and prepares to write into it.
the first row is written with headers ['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'] to describe the columns.
then, writes each row from csv_data into the csv file.
"""
def write_csv(csv_data):
    with open('data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['unique_id', 'mass', 'x_pos', 'y_pos', 'z_pos', 'vel_x', 'vel_y', 'vel_z', 'frame', 'dt'])
        csv_writer.writerows(csv_data)

"""
main:
calls init_constants() to get fundamental constants e G, c, and solar_mass.
initializes the state vectors pos, vel, and mass for n bodies using init_states().
sets the time step dt to 10,000 seconds and initializes an empty list csv_data to store simulation data.
initializes the 3D plot with init_plot() and stores the figure, axes, and scatter plot in fig, ax, and sc.
sets up the animation using FuncAnimation. it will call the update function every 50 milliseconds for 100,000 frames, updating the state and the plot.
displays the plot with plt.show().
finally, writes the collected data to a csv file using write_csv().
the simulation runs, visualizes the motion of celestial bodies in real-time, and saves the data for further analysis.
"""
if __name__ == '__main__':
    G, c, solar_mass, n = init_constants()
    pos, vel, mass = init_states(n, mean_mass=solar_mass, std_mass=0.1 * solar_mass)
    dt = 10000
    csv_data = []

    fig, ax, sc = init_plot(pos, mass)
    ani = animation.FuncAnimation(fig, update, fargs=(ax, sc, pos, vel, mass, dt, csv_data, G), frames=100, interval=50)

    plt.show()
    write_csv(csv_data)

