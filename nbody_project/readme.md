
# N-Body Simulation with Astropy and Matplotlib

## Table of Contents
- [Description](#description)
- [Dependencies](#dependencies)
- [Functions](#functions)
    - [init_constants](#init_constants)
    - [init_states](#init_states)
    - [init_plot](#init_plot)
    - [update](#update)
    - [write_csv](#write_csv)

## Description
This Python script simulates the motion of `n` celestial bodies interacting under gravity. The script makes use of the Astropy library to obtain physical constants and Matplotlib for visualization. Data about the celestial bodies' states are also saved in a CSV file.

## Dependencies
- `numpy`
- `matplotlib`
- `astropy`
- `csv`

## Functions

### `init_constants`
#### What it does:
Initializes physical constants like the gravitational constant `G`, speed of light `c`, solar mass `solar_mass`, and the number of bodies `n`.

#### Arguments:
None

#### Returns:
- `G`: Gravitational constant in \( m^3 / (kg \cdot s^2) \)
- `c`: Speed of light in \( m/s \)
- `solar_mass`: Solar mass in \( kg \)
- `n`: Number of bodies

### `init_states`
#### What it does:
Initializes the initial states of the celestial bodies.

#### Arguments:
- `n`: Number of bodies
- `mean_pos`: Mean position in 3D space
- `std_pos`: Standard deviation of position
- `mean_vel`: Mean velocity
- `std_vel`: Standard deviation of velocity
- `mean_mass`: Mean mass (optional)
- `std_mass`: Standard deviation of mass (optional)

#### Returns:
- `pos`: Array of positions
- `vel`: Array of velocities
- `mass`: Array of masses

### `init_plot`
#### What it does:
Initializes the 3D plot for visualization.

#### Arguments:
- `pos`: Array of positions
- `mass`: Array of masses

#### Returns:
- `fig`: Figure object
- `ax`: Axis object
- `sc`: Scatter plot object

### `update`
#### What it does:
Updates the plot and the states of the celestial bodies at each frame.

#### Arguments:
- `frame`: Current frame number
- `ax`: Axis object
- `sc`: Scatter plot object
- `pos`: Array of positions
- `vel`: Array of velocities
- `mass`: Array of masses
- `dt`: Time step
- `csv_data`: List to store data for CSV
- `G`: Gravitational constant

#### Returns:
- `sc`: Updated scatter plot object

### `write_csv`
#### What it does:
Writes the states of the celestial bodies into a CSV file.

#### Arguments:
- `csv_data`: List containing data to be written

#### Returns:
None

## Running the Script
Just run the script. Make sure to have all the dependencies installed.
