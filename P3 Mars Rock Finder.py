import random


target_rock = 'Rock-42'
target_location = 'Zone-A'
rock_collected = False  


def mars_lander_agent(rock, location, collected):
    print('Perception Received: Rock =', rock, ', Location =', location)

   
    if rock == target_rock and location == target_location:
        if not collected:
            return 'Collect Rock', True
        else:
            return 'Ignore Rock (Already Collected)', True
    else:
        return 'Ignore Rock (Wrong Location)', collected


while True:
  
    rock = random.choice(['Rock-42', 'Rock-99', 'Rock-X'])
    location = random.choice(['Zone-A', 'Zone-B', 'Zone-C'])

   
    action, rock_collected = mars_lander_agent(rock, location, rock_collected)
    print('Action Performed:', action)

   
    cmd = input("Type 'x' to exit or any key to continue: ")
    if cmd.lower() == 'x':
        break
