import physics_calculator

time = 2.0

# Calculate the time it takes for the ball to hit the ground
position = physics_calculator.building_height + (physics_calculator.initial_velocity * time) - (0.5 * physics_calculator.gravity * time ** 2 )
velocity = physics_calculator.initial_velocity - ( physics_calculator.gravity * time )
kinetic_energy = 0.5 * physics_calculator.ball_mass * (velocity ** 2)

# Moving status
if position > 0:
    moving_status = "Moving up"
elif position < 0:
    moving_status = "Moving down"
else:
    moving_status = "At rest"

# Print the results
print(f" Height: {physics_calculator.building_height} m")
print(f" Velocity: {velocity:.2f} m/s")
print(f" Mass: {physics_calculator.ball_mass} kg")
print(f" Position: {position:.2f} m")
print(f" Energy: {kinetic_energy:.2f} J")
print(f" Moving Status: {moving_status}")