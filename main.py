import time
from digital_twin import VirtualHeater
from pid_controller import PIDController

print("Wiring systems together...")

tank = VirtualHeater(ambient_temp=20.0)
controller = PIDController(kp=2.0, ki=0.1, kd=1.0)
target_temperature = 50.0

print(f"Target set to {target_temperature}°C. Starting simulation...\n")

for second in range(1, 101):
    power = controller.compute(
        setpoint=target_temperature, 
        current_value=tank.current_temp, 
        dt=1.0
    )
    tank.heater_power = power
    tank.update(dt=1.0)
    time.sleep(0.1)

print("\nSimulation Complete.")