import random  # To randomly simulate distance and side

# Define the door agent function
def door_reflex_agent(distance, person_side):
    print('Perception Received: Distance =', distance, 'meter, Person Side =', person_side)

    if distance <= 1.0:
        # Open the door on the opposite side
        open_side = 'right' if person_side == 'left' else 'left'
        return f'Open Door on {open_side} side'
    else:
        return 'Close Door'


# ---------------------- Simulation Loop ----------------------
while True:
    # Randomly simulate environment
    distance = round(random.uniform(0.5, 2.0), 2)  # Random distance between 0.5m and 2.0m
    person_side = random.choice(['left', 'right'])  # Random side

    # Agent decides action
    action = door_reflex_agent(distance, person_side)
    print('Action Performed:', action)

    # Ask user if they want to continue
    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
