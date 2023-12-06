
# N-Body Simulation with Astropy and Matplotlib

## 1. A brief Summary Summar of our project and why we are doing it
- This project invloves creating a python simulation of 'celestial bodies' under gravitational influences visualised and logged to a csv.
- The purpose was to demonstrate the dynamics of celestial/astronomical systems.
- This project shows the heavy overlap between physics, data analysis, and visualization in a computational setting.
- We have no doubt there are a many better (and more accruate) simulations readily avaliable to the public however, this really let us test our knowledge of some very important libraries (numpy, astropy et. al.) and how they can interact to futher the scientific body of knowledge.

## 2. A list of python packages used in our project
- Default/Standard Libraries: csv, typing
- Numpy
- Matplotlib (pyplot and ani)
- Astropy

## 3. Source code for any packages written
- Self contained code in `main.py`
- You will find all functions defined with docstrings at the top, and a main call at the bottom.

## 4. A written Presentation of our results:
**Results of Animation**

The animation shows n bodies moving through space and interacting with eachother due to gravitational forces. The masses of the bodies are determined by an initial mass function and are depicited/normalized by color. You can see given a random (within spec) mass, velocity, and position in this case the system drifted in the +x,+y,+z direction. When writing this I would have expected a larger conglomeration of the bodies but given the limited timestep we do not quite see this.

**Results of COM calculation**

The aim of doing a center of mass analysis was to examine how the position and mass of the stars in our simulation changed from frame to frame. To ensure the validity of the simulation, we assumed that the mass of the stars remained constant, and only the position of the stars varied due to the perturbation. To perform this analysis, we grouped the stars by their frame number, from 1 to 225, and calculated the center of mass of the system for each frame, using the center of mass function:

`rcm​=1/M∑(mi)(​r​i)`

where `rcm​` is the position vector of the center of mass, `M` is the total mass of the system, `mi​` is the mass of the i-th body, and `ri​` is the position vector of the i-th body1

This resulted in a set of vectors that represented the center of mass of the system with respect to time (frame). We expected to see a linear change in the center of mass of the system from frame to frame, as the system moved as a whole due to the inital external force. To visualize this, we plotted the first and the last center of mass vectors, marked with green and red respectively, and then plotted all the intermediate center of mass vectors, marked with blue. We then created an animation to observe the system’s change over time. We did not find any significant deviations or fluctuations in the center of mass vectors, which indicated that the simulation was consistent and realistic, and that the center of mass of the system was conserved throughout the simulation.

**Results for the momentum analysis**

One of the objectives of our simulation was to test whether the momentum of the system was conserved throughout the perturbation of the stars. This would help us verify that the simulation was running accurately from start to finish, and that there were no errors or anomalies in the data. To perform this analysis, we calculated the three-dimensional momentum of each star within each frame, using their velocity and mass values. We did this for all the frames, from 1 to 225, and obtained a set of arrays that represented the momentum of each star at each time step. We then plotted these arrays and created an animation to visualize the changes in the momentum of the stars over time. We were looking for any signs of inconsistency or deviation from the expected behavior of the system, such as sudden jumps or drops in the momentum values. Since we did not find any such discrepancies, we concluded that the simulation was consistent and reliable, and that the momentum of the system was conserved throughout the simulation.



## 5. Clear Instructions on how to run the code:
- Ensure main.py is in a python environment with the given packages avaliable (Astropy, Matplotlib, Numpy)
- This will not run sucessfully in an ipython env as the animation will not display, please use default python or an ide.
- The 3D matplotlib SC should appear and run course, it will also save a file called `data.csv` to the directory folder where it is being ran.




1. A written presentation of results of your coding project (a brief narrative, accompanying plots/animations/etc) and a very brief discussion of the implications
