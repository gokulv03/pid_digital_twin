class VirtualHeater:
    def __init__(self, ambient_temp=20.0):
        # The State Variables
        self.ambient_temp = ambient_temp
        self.current_temp = ambient_temp
        self.heater_power = 0.0 
        
        # --- NEW: Physical Constants ---
        # These dictate the physics of our specific tank
        self.heating_constant = 0.05   # How efficiently the heater warms the liquid
        self.cooling_constant = 0.02   # How fast heat escapes through the tank walls

    def update(self, dt):
        """
        Simulates the physics of the tank over a small time step (dt).
        """
        # --- NEW: The Physics Engine ---
        
        # 1. Calculate heat added by the active heater
        heat_added = self.heater_power * self.heating_constant * dt
        
        # 2. Calculate heat lost to the room (Newton's Law of Cooling)
        heat_lost = (self.current_temp - self.ambient_temp) * self.cooling_constant * dt
        
        # 3. Apply the thermodynamic changes to our tank
        self.current_temp += heat_added - heat_lost
        
        # Print the status, formatted to 2 decimal places
        print(f"Power: {self.heater_power:5.1f}% | Temp: {self.current_temp:.2f}°C")


# --- The Execution Area ---
if __name__ == "__main__":
    import time
    
    print("Initializing Digital Twin...")
    tank = VirtualHeater(ambient_temp=22.0)
    
    print("\n--- Starting 60 Second Physics Simulation ---")
    
    # We will simulate 60 seconds of time passing
    for second in range(1, 61):
        
        # Turn the heater on for the first 30 seconds, then shut it off
        if second <= 30:
            tank.heater_power = 50.0
        else:
            tank.heater_power = 0.0
            
        # Advance the physics engine by 1 second
        tank.update(dt=1.0)
        
        # Pause the script for 0.1 seconds so we can watch it happen live!
        time.sleep(0.1)