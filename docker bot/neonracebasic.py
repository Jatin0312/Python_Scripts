import gym
import universe

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1)

observation_n = env.reset()

i=0;
while True:
 if i%2==0:
   action = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),('KeyEvent', 'ArrowRight', False)]
 else:
   action = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
 action_n = [action for ob in observation_n]
 observation_n,reward_n,done_n,info = env.step(action_n)
 env.render() 
 i=i+1
print(env.observation_space) 