#!/usr/bin/env python
# coding: utf-8

# # 2D Maze 
# - Q-Learning
# - Static Environment (5x5)

# In[1]:


# Kaustav Vats (2016048)
import sys
import numpy as np
import math
from random import random
import gym
import gym_maze
import matplotlib.pyplot as plt

print("--------Import Done!--------")


# In[17]:


class MazeSolverTest:
    
    def NextAction(self, CurrentState):
        Action = int(np.argmax(QTable[CurrentState]))
        return Action

    def ShowResults(self, TotalPenalties, TotalEpochs, TotalReward):
        print("Total Episodes: ", EpisodesCount)
        print("Average steps per episode: ", TotalEpochs/EpisodesCount)
        print("Average penalties per episode: ", TotalPenalties/EpisodesCount)
        print("Average Reward per Episode: ", TotalReward/EpisodesCount)

    def StartTesting(self):
        TotalPenalties = 0
        TotalEpochs = 0
        TotalReward = 0.0

        for iteration in range(EpisodesCount):
            CurrentState = env.reset()
            CurrentState = tuple(map(int, CurrentState))
            Penalties = 0
            Epochs = 0
            Reward = 0.0

            Finished = False
            while not Finished:
                Action = self.NextAction(CurrentState)
                NewState, RewardAction, Finished, info = env.step(Action)
                NewState = tuple(map(int, NewState))
                CurrentState = NewState
                Reward += RewardAction

                if RewardAction < 0.0:
                    Penalties += 1
                # env.render()
                Epochs += 1
            TotalPenalties += Penalties
            TotalEpochs += Epochs
            TotalReward += Reward
            print("Episode Number: ", iteration)
        self.ShowResults(TotalPenalties, TotalEpochs, TotalReward)
                


# In[14]:


if __name__ == "__main__":
    env = gym.make("maze-sample-5x5-v0")
    
    # Total Training Iterations
    EpisodesCount = 100
    
    QTable = np.load('QTable.npy')
    


# In[15]:


    mazeSolver = MazeSolverTest()
    mazeSolver.StartTesting()


# In[ ]:




