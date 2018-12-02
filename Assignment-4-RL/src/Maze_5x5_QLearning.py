#!/usr/bin/env python
# coding: utf-8

# # 2D Maze 
# - Q-Learning
# - Static Environment (5x5)

# In[1]:


# Kaustav Vats (2016048)
# Ref:- Code-run.py (Given with the Resources)
import sys
import numpy as np
import math
from random import random
import gym
import gym_maze
import matplotlib.pyplot as plt

print("--------Import Done!--------")


# In[17]:


class MazeSolver:
    
    def __init__(self, ExplorationRate, LearningRate):
        self.ExplorationRate = ExplorationRate
        self.LearningRate = LearningRate
    
    def NextAction(self, CurrentState):
        RandomValue = random()
        if RandomValue < self.ExplorationRate:
            Action = env.action_space.sample()
        else:
            Action = int(np.argmax(QTable[CurrentState]))
        return Action
    
    # def updateParameters(self, iteration):
    #     self.ExplorationRate = max(MinExplorationRate, min(0.9, 1.0-math.log10((iteration+1)/10)))
    #     self.LearningRate = max(MinLearningRate, min(0.9, 1.0-math.log10((iteration+1)/10)))
    
    def updateParameters(self):
        self.ExplorationRate = self.ExplorationRate - 0.01*self.ExplorationRate
        self.ExplorationRate = max(MinExplorationRate, self.ExplorationRate)
        
        self.LearningRate = self.LearningRate - 0.01*self.LearningRate
        self.LearningRate = max(MinLearningRate, self.LearningRate)
    
    def ShowLearningCurve(self, rewards):
        episodes = []
        for i in range(len(rewards)):
            episodes.append(i+1)
        plt.plot(episodes, rewards)
        plt.xlabel('Episodes') 
        plt.ylabel('Rewards')
        plt.title('Learning Curve for 5x5 Maze')
        lgd = "Learning Rate- " + str(LearningRate) +"\n" + "Exploration Rate- "+ str(ExplorationRate) +"\n"+"Decay Rate- "+ str(DecayRate)
        plt.legend([lgd], loc='lower right')
        plt.show()

    def StartLearning(self):
        DiscountFactor = 0.8
        env.render()
        Reward = [0.0]*EpisodesCount
        
        for iteration in range(EpisodesCount):
            CurrentState = env.reset()
            CurrentState = tuple(map(int, CurrentState))
            TotalReward = 0
            
            Finished = False
            while not Finished:
                Action = self.NextAction(CurrentState)
                NewState, RewardAction, Finished, info = env.step(Action)
                NewState = tuple(map(int, NewState))
                
                BestQValue = np.amax(QTable[NewState])
                QTable[CurrentState + (Action, )] += self.LearningRate*(RewardAction + (DiscountFactor * BestQValue) - QTable[CurrentState + (Action, )])
                CurrentState = NewState
                
                TotalReward += RewardAction
                env.render()
                
                if Finished:
                    print("\nEpisode = %d" % iteration)
                    print("Explore rate: %f" % self.ExplorationRate)
                    print("Learning rate: %f" % self.LearningRate)
                    print("Reward: %f" % TotalReward)
                    print("")
                    break
                    
            self.updateParameters()
            # self.updateParameters(iteration)
            Reward[iteration] = TotalReward
        print(QTable)
        print(Reward)
        self.ShowLearningCurve(Reward)
                


# In[14]:


if __name__ == "__main__":
    env = gym.make("maze-sample-5x5-v0")
    
    # Total Training Iterations
    EpisodesCount = 100

    # Hyperparameters
    LearningRate = 0.9  # Alpha
    ExplorationRate = 0.9  # Gamma
    DecayRate = 10  
    
    MinExplorationRate = 0.001
    MinLearningRate = 0.3

    # Q Table size
    ActionSize = env.action_space.n
    StateSize = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))

    print("ActionSize:", ActionSize)
    print("StateSize:", StateSize)
    
    # Initialize Q Table
    QTable = np.zeros(StateSize + (ActionSize,), dtype=float)
#     print(QTable)  
    


# In[15]:


mazeSolver = MazeSolver(ExplorationRate, LearningRate)
mazeSolver.StartLearning()
np.save('QTable', QTable)


# In[ ]:




