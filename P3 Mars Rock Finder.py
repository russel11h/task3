import random

# Predefined rock target (for simulation)
target_rock = 'Rock-42'
target_location = 'Zone-A'
rock_collected = False  # Memory to avoid re-collecting

# Mars Lander Agent
def mars_lander_agent(rock, location, collected):
    print('Perception Received: Rock =', rock, ', Location =', location)

    # Check if rock is target and at correct location
    if rock == target_rock and location == target_location:
        if not collected:
            return 'Collect Rock', True
        else:
            return 'Ignore Rock (Already Collected)', True
    else:
        return 'Ignore Rock (Wrong Location)', collected


# ---------------------- Simulation Loop ----------------------
while True:
    # Simulate rock and location
    rock = random.choice(['Rock-42', 'Rock-99', 'Rock-X'])
    location = random.choice(['Zone-A', 'Zone-B', 'Zone-C'])

    # Agent decides what to do
    action, rock_collected = mars_lander_agent(rock, location, rock_collected)
    print('Action Performed:', action)

    # User control
    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
