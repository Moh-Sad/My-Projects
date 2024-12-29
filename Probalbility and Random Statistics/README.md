# Probability and Random Statistics Assignment

This project involves the analysis and simulation of random processes, stationarity, and Poisson distributions using Java and Python. Below is the detailed documentation of the tasks, solutions, and methodologies employed.

## Course Information
- **Course Title:** Probability and Random Statistics
- **Instructor:** Mrs. Gemechu Dinkisa
- **Submission Date:** 27th December 2024

## Contributors
- Mohammed Sadik (ID: UGR/30960/15, Sec: 3)
- Moti Alemu (ID: UGR/30963/15, Sec: 3)
- Mekhluqat Abdulwehab (ID: UGR/30876/15, Sec: 3)

---

## Assignment Questions

### 1. Wide-Sense Stationarity (WSS)
**Problem:** Determine whether the process \(X(t) = At\) (where \(A\) is uniformly distributed over \((-2, 3)\)) is WSS.

**Solution Steps:**
1. **Key Concepts:**
   - A process is WSS if:
     - The mean \(E[X(t)]\) is time-independent.
     - The autocovariance \(C_X(t_1, t_2)\) depends only on \(\tau = t_2 - t_1\).
2. **Methodology:**
   - Generate random samples of \(A\).
   - Compute \(E[X(t)]\) and \(C_X(t_1, t_2)\).
3. **Implementation:**
   - **Code:** `WideSenseStationary.java`
   - **Execution:**
     ```bash
     javac WideSenseStationary.java
     java WideSenseStationary
     ```
4. **Expected Output:**
   - Mean at \(t_1\): 0.5000, \(t_2\): 1.5000
   - Autocovariance: 1.2500
   - Conclusion: \(X(t)\) is **not WSS** as the mean and autocovariance depend on time.

---

### 2. Time Dependency of a Random Process
**Problem:** Verify whether \(X(t) = \cos(\omega t + \theta)\), where \(\theta\) is uniformly distributed in \((-π/2, π/2)\), is time-independent.

**Solution Steps:**
1. **Key Concepts:**
   - \(E[X(t)]\) and \(C_X(t_1, t_2)\) must be time-independent.
2. **Methodology:**
   - Generate random samples of \(\theta\).
   - Compute \(E[X(t)]\) and \(C_X(t_1, t_2)\).
3. **Implementation:**
   - **Code:** `RandomProcessTimeDependency.java`
   - **Execution:** Compile and run the code as per Java standards.
4. **Expected Output:**
   - Mean: 0.0000
   - Conclusion: \(X(t)\) is time-independent and satisfies WSS.

---

### 3. Stationarity of a Random Process
**Problem:** Verify the stationarity of \(X(t) = A\cos(\omega_c t + \theta)\), where \(A\) and \(\theta\) are random.

**Solution Steps:**
1. **Key Concepts:**
   - \(E[X(t)]\) must be time-independent.
   - \(C_X(t_1, t_2)\) must depend only on \(\tau\).
2. **Implementation:**
   - **Code:** `RandomProcessStationary.py`
   - **Execution:**
     ```bash
     python RandomProcessStationary.py
     ```
3. **Expected Output:**
   - Mean: 0.0000
   - Conclusion: \(X(t)\) is stationary.

---

### 4. Simulation of Mobile Messages
**Problem:** Simulate the number of messages received on a mobile phone per day using a Poisson process with \(\lambda = 50\).

**Solution Steps:**
1. **Key Concepts:**
   - Use a Poisson distribution for simulation.
2. **Implementation:**
   - **Code:** `PoissonProcess.py`
   - **Execution:**
     ```bash
     python PoissonProcess.py
     ```
3. **Expected Output:**
   - Simulated messages for 30 days.
   - A bar chart visualizing message counts.

---

## Tools and Libraries
- **Languages:** Java, Python
- **Libraries:** `numpy`, `matplotlib` (for Python)
- **Compilation/Execution:** Ensure the necessary tools (e.g., `javac`, Python environment) are installed.

## Repository Structure
```plaintext
├── WideSenseStationary.java
├── RandomProcessTimeDependency.java
├── RandomProcessStationary.py
├── PoissonProcess.py
├── README.md