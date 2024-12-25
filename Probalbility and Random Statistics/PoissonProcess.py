import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean_messages_per_day = 50  # Average number of messages per day (Poisson parameter λ)
days = 30                   # Number of days to simulate

# Simulate the number of messages per day
np.random.seed(42)  # For reproducibility
messages_per_day = np.random.poisson(mean_messages_per_day, days)

# Example: Specific day details
specific_day = 15  # Pick a specific day for analysis
messages_on_specific_day = messages_per_day[specific_day - 1]  # Zero-indexed

# Display results
print(f"Simulated messages per day for {days} days: {messages_per_day}")
print(f"Messages received on day {specific_day}: {messages_on_specific_day}")

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(range(1, days + 1), messages_per_day, color='skyblue', edgecolor='black')
plt.axhline(mean_messages_per_day, color='red', linestyle='--', label=f"Mean ({mean_messages_per_day} messages)")
plt.title("Number of Messages Received Per Day")
plt.xlabel("Day")
plt.ylabel("Number of Messages")
plt.xticks(range(1, days + 1, max(1, days // 10)))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()