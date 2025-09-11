import physics_calculator

time = 2.0

# Calculate the time it takes for the ball to hit the ground
position = physics_calculator.building_height + (physics_calculator.initial_velovity * time) - (0.5 * physics_calculator.gravity * (time ** 2) )
velocity = physics_calculator.initial_velocity - ( physics_calculator.gravity * time )
kinetic_energy = 0.5 * physics_calculator.ball_mass * (physics_calculator.velocity ** 2)

# Print the results
print(f" Height: {physics_calculator.building_height} m")
print(f" Velocity: {physics_calculator.velocity} m/s")
print(f" Mass: {physics_calculator.ball_mass} kg")
