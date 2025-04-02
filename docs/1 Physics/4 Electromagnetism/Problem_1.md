# Problem 1

# Simulating the Effects of the Lorentz Force

## Motivation
The Lorentz force, expressed as $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$, governs the motion of charged particles in electric and magnetic fields. It is fundamental in fields like plasma physics, particle accelerators, and astrophysics. By focusing on simulations, we can explore the practical applications and visualize the complex trajectories that arise due to this force.

## Task Overview
1. **Theory and Application**: Identify systems where the Lorentz force is key and discuss the roles of electric ($\mathbf{E}$) and magnetic ($\mathbf{B}$) fields.
2. **Simulating Particle Motion**: Simulate the trajectory of a charged particle under various field configurations (uniform magnetic field, combined electric and magnetic fields, crossed fields, and non-uniform magnetic field).
3. **Parameter Exploration**: Vary parameters like field strengths, initial velocity, charge, and mass to observe their effects.
4. **Visualization**: Create 2D and 3D plots to visualize the particle’s trajectory and highlight phenomena like Larmor radius and drift velocity.

## Solution

### 1. Theory and Application

#### Systems Involving the Lorentz Force
The Lorentz force plays a critical role in several systems:
- **Particle Accelerators**: In cyclotrons, the magnetic field causes charged particles to move in circular paths, while electric fields accelerate them. The Lorentz force ensures particles follow a spiral trajectory as their energy increases.
- **Mass Spectrometers**: The Lorentz force separates ions based on their mass-to-charge ratio by deflecting them in a magnetic field.
- **Plasma Confinement**: In fusion devices like tokamaks, magnetic fields confine charged particles in a plasma, preventing them from hitting the reactor walls.

#### Role of Electric and Magnetic Fields
- **Electric Field ($\mathbf{E}$)**: Exerts a force $\mathbf{F}_E = q \mathbf{E}$, accelerating the particle in the direction of the field (if $q$ is positive). This force is independent of the particle’s velocity.
- **Magnetic Field ($\mathbf{B}$)**: Exerts a force $\mathbf{F}_B = q (\mathbf{v} \times \mathbf{B})$, which is perpendicular to both the velocity $\mathbf{v}$ and the magnetic field $\mathbf{B}$. This force causes circular or helical motion but does no work since it is always perpendicular to the velocity.

### 2. Simulating Particle Motion

We’ll simulate the motion of a charged particle under the Lorentz force using the following equation of motion:

$$
\mathbf{F} = m \mathbf{a} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

This gives the acceleration:

$$
\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{q}{m} (\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

We’ll use the **Runge-Kutta 4th-order method (RK4)** to numerically solve this differential equation, as it provides better accuracy than the Euler method. We’ll simulate the following cases:
- **Uniform Magnetic Field**: $\mathbf{B} = (0, 0, B_z)$, $\mathbf{E} = 0$.
- **Combined Uniform Electric and Magnetic Fields**: $\mathbf{B} = (0, 0, B_z)$, $\mathbf{E} = (E_x, 0, 0)$.
- **Crossed Fields**: $\mathbf{B} = (0, 0, B_z)$, $\mathbf{E} = (E_x, 0, 0)$, with $\mathbf{E} \perp \mathbf{B}$.
- **Non-Uniform Magnetic Field (Magnetic Bottle)**: $\mathbf{B}$ varies spatially.

#### Python Script for Simulation
Below is a Python script that simulates the particle’s motion under the Lorentz force for the above cases. It uses NumPy for calculations and Matplotlib for 2D and 3D visualizations.


![alt text](image.png)

![alt text](image-1.png)  

<p align="center">

  <img src="image.png" width="400">
  <img src="image-1.png" width="400">
  

</p>


![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

![alt text](image-7.png)