class PDController:
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0  # Assuming 2D position (x, y)

    def compute_action(self, reference, observation):

        # Calculate current error
        error = reference - observation
        
        # Calculate control action using the PD control law
        action = self.Kp * error + self.Kd * (error - self.previous_error)
        
        # Update previous error for next iteration
        self.previous_error = error
        
        return action