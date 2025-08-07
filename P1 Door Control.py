import random 


def door_reflex_agent(distance, person_side):
    print('Perception Received: Distance =', distance, 'meter, Person Side =', person_side)

    if distance <= 1.0:
       
        open_side = 'right' if person_side == 'left' else 'left'
        return f'Open Door on {open_side} side'
    else:
        return 'Close Door'


while True:
  
    distance = round(random.uniform(0.5, 2.0), 2)  
    person_side = random.choice(['left', 'right']) 

  
    action = door_reflex_agent(distance, person_side)
    print('Action Performed:', action)


    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
