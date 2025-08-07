import random 


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


while True:
   
    person_present = random.choice([True, False]) 
    time_of_day = random.choice(['day', 'night'])  

 
    action = room_reflex_agent(person_present, time_of_day)
    print('Action Performed:', action)


    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
