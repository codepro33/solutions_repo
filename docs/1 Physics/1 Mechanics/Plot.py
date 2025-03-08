
import numpy as np
import matplotlib.pyplot as plt

def projectile_range(v0, theta_deg, g=9.8, h=0):
    """Calculate range with initial height h."""
    theta = np.radians(theta_deg)
    if h == 0:
        return (v0**2 * np.sin(2 * theta)) / g
    else:
        # Time of flight with initial height
        a = -g / 2
        b = v0 * np.sin(theta)
        c = h
        t_flight = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)  # Positive root
        return v0 * np.cos(theta) * t_flight

# Parameters
v0_values = [10, 20, 30]  # m/s
g = 9.8  # m/s^2
h_values = [0, 10]  # m
theta_deg = np.linspace(0, 90, 91)  # 0 to 90 degrees

# Plotting
plt.figure(figsize=(10, 6))
for v0 in v0_values:
    for h in h_values:
        R = [projectile_range(v0, t, g, h) for t in theta_deg]
        label = f'v0={v0} m/s, h={h} m'
        plt.plot(theta_deg, R, label=label)

plt.xlabel('Angle of Projection (degrees)')
plt.ylabel('Range (meters)')
plt.title('Projectile Range vs. Angle of Projection')
plt.legend()
plt.grid(True)
plt.show()