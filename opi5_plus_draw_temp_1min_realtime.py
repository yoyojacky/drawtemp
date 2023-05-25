import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import subprocess


# Set the backend to TkAgg
matplotlib.use('TkAgg')

# Initialize the lists to store temperature data
timestamps = []
temperatures = []

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create an empty line object for the plot
line, = ax.plot([], [])

# Customize the plot settings
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('CPU Temperature')

# Define the update function for the plot
def update_plot():
    # Get the CPU temperature using the command 'cat /sys/class/thermal/thermal_zone0/temp'
    process = subprocess.Popen(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    temperature = float(output) / 1000  # Convert temperature to Celsius
    current_time = len(timestamps) * interval

    # Append the current timestamp and temperature to the lists
    timestamps.append(current_time)
    temperatures.append(temperature)

    # Update the plot data
    line.set_data(timestamps, temperatures)

    # Adjust the plot limits if necessary
    ax.relim()
    ax.autoscale_view()

    plt.pause(interval)

# Define the duration and interval for data collection
duration = 60  # Collect data for 60 seconds
interval = 1  # Collect data every 1 second

# Collect the CPU temperature data
start_time = plt.time.time()
while plt.time.time() - start_time <= duration:
    update_plot()

# Display the final plot
plt.show()

