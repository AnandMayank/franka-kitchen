import time 
import gymnasium as gym 
import numpy as no 
from gym_robotics_custom import RoboGymObservationWrapper
from buffer import ReplayBuffer
from model import *
from agent import *
from meta_agent import * 


if __name__ == '__main__':

    env_name='FrankaKitchen-v1'
    max_episode_steps=500
    replay_buffer_size = 1000000
    tasks = [  'hinge cabinet','top burner', 'microwave']
    gamma = 0.99
    tau = 0.005
    alpha = 0.1
    target_update_interval = 1
    updates_per_steps = 4
    hidden_size = 512
    learning_rate = 0.0001
    batch_size = 64
    live_test = True

    if live_test :
        env = gym.make(env_name , max_episode_steps = max_episode_steps, tasks_to_complete=tasks, render_mode='human')
        env = RoboGymObservationWrapper(env)

        meta_agent = MetaAgent(env , tasks, max_episode_steps=max_episode_steps)

        meta_agent.initialize_agents()

        meta_agent.test()

        env.close()


    