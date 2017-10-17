import gym
import universe # register the universe environments
import random

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) # automatically creates a local docker container
observation_n = env.reset()

# Create variable for moving the car
goleft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
goright = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
         ('KeyEvent', 'ArrowRight', True)]

# Move the car forward with nitroboost 
boostforward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowRight', False),
       ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'n', True)]


sum_reward = 0
turn = 0
rewards = []
buffer_size = 100
action = boostforward

while True:
action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n] # your agent here
 observation_n, reward_n, done_n, info = env.step(action_n) # Reinforcement Learning action by agent
 print ("observation: ", observation_n) # Observation of the environment
 print ("reward: ", reward_n) # If the action had any postive impact +1/-1
env.render() # Run the agent on the environment