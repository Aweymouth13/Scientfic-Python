
# Simulation Code Explained with LaTeX

## Difference in Position (`dx`)

The difference in position between each pair of particles is calculated as follows:

\[
\text{{dx}}_{ij} = \text{{pos}}_i - \text{{pos}}_j
\]

### Dummy Numbers Example

Let's say we have two particles with positions \( \text{{pos}}_1 = [1, 1] \) and \( \text{{pos}}_2 = [4, 5] \).

\[
\text{{dx}}_{12} = [1, 1] - [4, 5] = [-3, -4]
\]

## Distance (`distance`)

The distance between each pair of particles is:

\[
\text{{distance}}_{ij} = \sqrt{{\text{{dx}}_{ij}^2 + \text{{dy}}_{ij}^2}} + 1 \times 10^{-9}
\]

### Dummy Numbers Example

Using the \( \text{{dx}}_{12} = [-3, -4] \) from earlier:

\[
\text{{distance}}_{12} = \sqrt{{(-3)^2 + (-4)^2}} + 1 \times 10^{-9} = \sqrt{{9 + 16}} + 1 \times 10^{-9} = \sqrt{{25}} + 1 \times 10^{-9} = 5 + 1 \times 10^{-9}
\]

## Gravitational Force (`force`)

The gravitational force between each pair of particles is:

\[
\text{{force}}_{ij} = G \times \frac{{\text{{mass}}_i \times \text{{mass}}_j \times \text{{dx}}_{ij}}}{{\text{{distance}}_{ij}^3}}
\]

### Dummy Numbers Example

Let \( G = 6.674 \times 10^{-11} \), \( \text{{mass}}_1 = 5 \), and \( \text{{mass}}_2 = 6 \).

\[
\text{{force}}_{12} = 6.674 \times 10^{-11} \times \frac{{5 \times 6 \times [-3, -4]}}{(5 + 1 \times 10^{-9})^3} \approx [-1.601 \times 10^{-11}, -2.134 \times 10^{-11}]
\]
