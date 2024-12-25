import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega_c = 2 * np.pi  
N = 100000           
t1 = 1.0             
t2 = 3.0             

# Random variables
A = 1                # Assuming A is constant
theta = np.random.uniform(-np.pi, np.pi, N)  # Uniformly distributed in (-pi, pi)

# Calculate X(t) for t1 and t2
X_t1 = A * np.cos(omega_c * t1 + theta)
X_t2 = A * np.cos(omega_c * t2 + theta)

# Mean calculation
mean_t1 = np.mean(X_t1)
mean_t2 = np.mean(X_t2)

# Autocovariance calculation
autocov_t1_t2 = np.mean(X_t1 * X_t2) - mean_t1 * mean_t2
autocov_t1_t1 = np.mean(X_t1 * X_t1) - mean_t1 * mean_t1

# Display results
print(f"Mean at t1: {mean_t1:.4f}, Mean at t2: {mean_t2:.4f}")
print(f"Autocovariance at (t1, t2): {autocov_t1_t2:.4f}")
print(f"Autocovariance at (t1, t1): {autocov_t1_t1:.4f}")

# Time difference
tau = t2 - t1
print(f"Time difference (tau): {tau:.2f}")

# Plotting X(t) for visualization
t = np.linspace(0, 10, 1000)
X_t = A * np.cos(omega_c * t[:, None] + theta).mean(axis=1)

plt.figure(figsize=(10, 5))
plt.plot(t, X_t, label="Mean of X(t)")
plt.axhline(0, color="red", linestyle="--", label="Zero Line")
plt.title("Visualization of the Random Process X(t)")
plt.xlabel("Time (t)")
plt.ylabel("X(t)")
plt.legend()
plt.grid()
plt.show()