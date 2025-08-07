import random  # To simulate environment status

# Define the smart room agent function
def room_reflex_agent(person_present, time_of_day):
    print('Perception Received: Person Present =', person_present, ', Time =', time_of_day)

    if not person_present:
        return 'Turn OFF Light and Fan'
    elif time_of_day == 'night':
        return 'Turn ON Light and Fan'
    elif time_of_day == 'day':
        return 'Turn ON Fan Only'
    else:
        return 'Invalid Time'


# ---------------------- Simulation Loop ----------------------
while True:
    # Randomly simulate environment
    person_present = random.choice([True, False])  # True = person in room, False = empty
    time_of_day = random.choice(['day', 'night'])  # Random time

    # Agent decides action
    action = room_reflex_agent(person_present, time_of_day)
    print('Action Performed:', action)

    # Ask user if they want to continue
    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
