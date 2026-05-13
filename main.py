import time
import matplotlib.pyplot as plt  # NEW: Import the graphing library
from digital_twin import VirtualHeater
from pid_controller import PIDController

print("Wiring systems together...")

tank = VirtualHeater(ambient_temp=20.0)
controller = PIDController(kp=2.0, ki=0.1, kd=1.0)
target_temperature = 50.0

print(f"Target set to {target_temperature}°C. Starting simulation...\n")

# NEW: Create empty lists to store our data history
time_history = []
temp_history = []
power_history = []
target_history = []

# We'll run it for 120 seconds to get a good look at the stabilized flatline
for second in range(1, 121):
    power = controller.compute(
        setpoint=target_temperature, 
        current_value=tank.current_temp, 
        dt=1.0
    )
    tank.heater_power = power
    tank.update(dt=1.0)
    
    # NEW: Save the data point for this exact second
    time_history.append(second)
    temp_history.append(tank.current_temp)
    power_history.append(power)
    target_history.append(target_temperature)
    
    # (Optional: I removed time.sleep() so the graph generates instantly)

print("\nSimulation Complete. Generating telemetry graph...")

# --- NEW: The Matplotlib Dashboard ---
# Create a figure with a specific size
plt.figure(figsize=(10, 6))

# Top Graph: Temperature vs Target
plt.subplot(2, 1, 1) # (2 rows, 1 column, plot 1)
plt.plot(time_history, temp_history, label='Tank Temperature', color='red', linewidth=2)
plt.plot(time_history, target_history, label='Target Setpoint', color='black', linestyle='--')
plt.title('Digital Twin: PID Control Telemetry')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.legend()

# Bottom Graph: Heater Power Output
plt.subplot(2, 1, 2) # (2 rows, 1 column, plot 2)
plt.plot(time_history, power_history, label='Heater Power Output', color='blue', linewidth=2)
plt.xlabel('Time (seconds)')
plt.ylabel('Power (%)')
plt.grid(True, alpha=0.3)
plt.legend()

# Clean up the layout and show the window
plt.tight_layout()
plt.show()