import psutil
import matplotlib.pyplot as plt

# Step 1: Create the figure and axis for the plot
fig, ax = plt.subplots()
x_data, y_data = [], []

# Set the title and labels
ax.set_title("Real-Time CPU Usage")
ax.set_xlabel("Time (s)")
ax.set_ylabel("CPU Usage (%)")
ax.set_ylim(0, 100)  # CPU usage percentage from 0 to 100

# Duration for how long to collect data (in seconds)
duration = 60

# Step 2: Collect CPU usage data over time (for the specified duration)
for i in range(duration):
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Append the new CPU usage and time data
    y_data.append(cpu_percent)
    x_data.append(i)  # Use the iteration count as the x-axis value (time in seconds)

# Step 3: Plot the data (no need to show the plot)
ax.fill_between(x_data, y_data, color="blue", alpha=0.5)

# Set chart labels and limits again
ax.set_ylim(0, 100)
ax.set_title("Real-Time CPU Usage")
ax.set_xlabel("Time (s)")
ax.set_ylabel("CPU Usage (%)")

# Step 4: Save the plot to a file (without showing it)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.savefig("cpu_usage_chart.png")  # Save the plot as a PNG file

# Optional: Save in other formats like PDF, SVG, etc.
# plt.savefig("cpu_usage_chart.pdf")
# plt.savefig("cpu_usage_chart.svg")

print("CPU usage chart saved as cpu_usage_chart.png")
