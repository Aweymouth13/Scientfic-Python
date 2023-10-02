## Understanding the Physics Simulation Code

### Variables and Their Meanings
- \( 	ext{frame} \): Frame number, often used in animations.
- \( 	ext{ax} \): Axis for the plot, mainly used for visualization.
- \( 	ext{sc} \): Scatter plot object, used for visualization.
- \( 	ext{pos} \): Position matrix, stores the x, y, z coordinates for each body.
- \( 	ext{vel} \): Velocity matrix, stores the velocity components for each body.
- \( 	ext{mass} \): Mass array, stores the mass for each body.
- \( 	ext{dt} \): Time step, the amount of time each simulation step represents.
- \( 	ext{csv\_data} \): Data from a CSV file, if used (not referenced in the code snippet).
- \( G \): Gravitational constant.

### Calculating the Differences in Positions (\( dx \))
\( dx = 	ext{pos}[:, 	ext{np.newaxis}, :] - 	ext{pos}[	ext{np.newaxis}, :, :] \)

In LaTeX form:
\[ dx = X_{ij} - X_{ji} \]

For example, if \( 	ext{pos} = [x_1, y_1, x_2, y_2] \) and \( 	ext{pos} = [1, 2, 4, 5] \),
\[ dx = [3, 3] \]

### Calculating the Distance (\( 	ext{distance} \))
\[ 	ext{distance} = \sqrt{\sum dx^2} + 1 	imes 10^{-9} \]
For example, if \( dx = [3, 3] \),
\[ 	ext{distance} = \sqrt{3^2 + 3^2} + 1 	imes 10^{-9} = \sqrt{18} + 1 	imes 10^{-9} pprox 4.2426 \]

### Calculating the Gravitational Force (\( 	ext{force} \))
\[ 	ext{force} = rac{{G 	imes m_i 	imes m_j 	imes dx}}{{	ext{distance}^3}} \]
For example, if \( m_i = 2, m_j = 3, dx = [3, 3], 	ext{distance} = 4.2426 \),
\[ 	ext{force} = rac{{G 	imes 2 	imes 3 	imes [3, 3]}}{{4.2426^3}} \]

### Net Force on Each Body (\( 	ext{net\_force} \))
\[ 	ext{net\_force} = \sum 	ext{force} \]
For example, if \( 	ext{force} = [f_1, f_2] \),
\[ 	ext{net\_force} = f_1 + f_2 \]

### Updating Velocities and Positions
- Update velocities: \( 	ext{vel} += rac{{	ext{net\_force} 	imes dt}}{{	ext{mass}}} \)
- Update positions: \( 	ext{pos} += 	ext{vel} 	imes dt \)
