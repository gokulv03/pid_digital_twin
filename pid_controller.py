class PIDController:
    def __init__(self, kp, ki, kd):
        # 1. Tuning Parameters (The "Personality" of the controller)
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        # 2. Memory Variables (Needed for Integral and Derivative math)
        self.integral_error = 0.0
        self.previous_error = 0.0

    def compute(self, setpoint, current_value, dt):
        """
        Calculates the required control output (heater power) to reach the setpoint.
        """
        # A. Calculate the current error
        error = setpoint - current_value
        
        # B. Proportional Term
        p_out = self.kp * error
        
        # C. Integral Term (Accumulate error over time)
        self.integral_error += error * dt
        i_out = self.ki * self.integral_error
        
        # D. Derivative Term (Rate of change of the error)
        derivative = (error - self.previous_error) / dt
        d_out = self.kd * derivative
        
        # E. Calculate total output
        output = p_out + i_out + d_out
        
        # F. Save the current error for the next loop's derivative calculation
        self.previous_error = error
        
        # G. Clamp the output to physical reality (Heater can't be > 100% or < 0%)
        if output > 100.0:
            output = 100.0
        elif output < 0.0:
            output = 0.0
            
        return output

# --- Quick Test ---
if __name__ == "__main__":
    print("Testing PID Math...")
    # Create a controller with some basic tuning parameters
    pid = PIDController(kp=2.0, ki=0.1, kd=1.0)
    
    # If our target is 50, but we are at 20, what should the heater do?
    power = pid.compute(setpoint=50.0, current_value=20.0, dt=1.0)
    print(f"Calculated Heater Power: {power:.1f}%")