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
import time

print("--------Import Done!--------")


# In[17]:


class MazeSolver:
    
    def __init__(self, ExplorationRate):
        self.ExplorationRate = ExplorationRate
    
    def NextAction(self, CurrentState):
        RandomValue = random()
        if RandomValue < self.ExplorationRate:
            Action = env.action_space.sample()
        else:
            Action = int(np.argmax(QTable[CurrentState]))
        return Action
    
    # def updateParameters(self, iteration):
    #     self.LearningRate = max(MinLearningRate, min(0.9, 1.0-math.log10((iteration+1)/10)))
    
    def updateParameters(self):        
        self.ExplorationRate = self.ExplorationRate - 0.03*self.ExplorationRate
        self.ExplorationRate = max(MinExplorationRate, self.ExplorationRate)
    
    def ShowLearningCurve(self, rewards):
        episodes = []
        for i in range(len(rewards)):
            episodes.append(i+1)
        plt.plot(episodes, rewards)
        plt.xlabel('Number of Episodes') 
        plt.ylabel('Rewards')
        plt.title('Learning Curve for 5x5 Maze')
        plt.legend(["Learning Rate- " + str(LearningRate)], loc='lower right')
        plt.savefig('LearningCurve_1.png')
        plt.show()

    def ShowStepsCurve(self, steps):
        episodes = []
        stepcount = 0
        for i in range(len(steps)):
            episodes.append(i+1)
            stepcount += steps[i]
        print("Average steps per episode: ", stepcount/len(steps))
        print("Total Number of Steps: ", stepcount)
        plt.plot(episodes, steps)
        plt.xlabel('Number of Episodes') 
        plt.ylabel('Each Episode Step count')
        plt.title('Learning Curve for 5x5 Maze')
        plt.legend(["Each Episode steps"], loc='upper right')
        plt.savefig('LearningCurve_2.png')
        plt.show()

    def ShowActionProbability(self):
        episodes = []
        for i in range(len(Probability_Action_1)):
            episodes.append(i+1)
        plt.plot(episodes, Probability_Action_1)
        plt.plot(episodes, Probability_Action_2)
        plt.plot(episodes, Probability_Action_3)
        plt.plot(episodes, Probability_Action_4)
        plt.xlabel('State Visited Count') 
        plt.ylabel('Probability')
        plt.title('Probability change for each Action at State x,y=2,4')
        plt.legend(['Up Action', 'Down Action', 'Right Action', 'Left Action'], loc='upper right')
        plt.savefig('ActionProbability.png')
        plt.show()

    def CalculateValue(self, state, state2, reward, action, action2):
        predict = QTable[CurrentState + (Action, )]
        target = reward + DiscountFactor*Q[state2, action2]
        QTable[CurrentState + (Action, )] = QTable[CurrentState + (Action, )] + LearningRate * (target - predict)

    def StartLearning(self):
        if Debug:
            env.render()
        Reward = [0.0]*EpisodesCount
        Steps = [0]*EpisodesCount
        
        for iteration in range(EpisodesCount):
            CurrentState = env.reset()
            CurrentState = tuple(map(int, CurrentState))
            TotalReward = 0
            TotalSteps = 0
            Action = self.NextAction(CurrentState)

            Finished = False
            while not Finished:
                
                NewState, RewardAction, Finished, info = env.step(Action)
                NewState = tuple(map(int, NewState))
                
                Action2 = self.NextAction(NewState)

                print("QT NewState: ", QTable[NewState] )
                
                # self.CalculateValue(CurrentState, NewState, RewardAction, Action, Action2)
                predict = QTable[CurrentState + (Action, )]
                target = RewardAction + DiscountFactor*QTable[NewState + (Action2, )]
                QTable[CurrentState + (Action, )] = QTable[CurrentState + (Action, )] + LearningRate * (target - predict)

                CurrentState = NewState
                Action = Action2

                TotalReward += RewardAction
                if Debug:
                    env.render()
                    # time.sleep(3)
                if NewState[0] == 2 and NewState[1] == 4:
                    D = 0
                    for i in range(4):
                        D += math.fabs(QTable[NewState][i])
                    Probability_Action_1.append(math.fabs(QTable[NewState][0]/D))
                    Probability_Action_2.append(math.fabs(QTable[NewState][1]/D))
                    Probability_Action_3.append(math.fabs(QTable[NewState][2]/D))
                    Probability_Action_4.append(math.fabs(QTable[NewState][3]/D))
                # print("A1 ", QTable[NewState][0])
                # print("A2 ", QTable[NewState][1])
                # print("A3 ", QTable[NewState][2])
                # print("A4 ", QTable[NewState][3])

                TotalSteps += 1
                if Finished:
                    print("\nEpisode = %d" % iteration)
                    print("Learning rate: %f" % LearningRate)
                    print("Exploration Rate: %f" % self.ExplorationRate)
                    print("Reward: %f \n" % TotalReward)
                    break
                    
            self.updateParameters()
            # self.updateParameters(iteration)
            Reward[iteration] = TotalReward
            Steps[iteration] = TotalSteps
        print(QTable)
        # print(Reward)
        self.ShowLearningCurve(Reward)
        self.ShowStepsCurve(Steps)
        self.ShowActionProbability()
                


# In[14]:


if __name__ == "__main__":
    env = gym.make("maze-sample-5x5-v0")
    
    # Total Training Iterations
    EpisodesCount = 150  # Default should be 100.

    # Hyperparameters
    LearningRate = 0.7
    ExplorationRate = 0.8
    MinExplorationRate = 0.1

    DiscountFactor = 0.8

    # Q Table size
    ActionSize = env.action_space.n
    StateSize = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))

    print("ActionSize:", ActionSize)
    print("StateSize:", StateSize)
    
    Debug = False   # Make it True to enable env.render()

    # Initialize Q Table
    QTable = np.zeros(StateSize + (ActionSize,), dtype=float)
    print(QTable)  

    # Part 3
    Probability_Action_1 = []
    Probability_Action_2 = []
    Probability_Action_3 = []
    Probability_Action_4 = []
    


# In[15]:


    mazeSolver = MazeSolver(LearningRate)
    mazeSolver.StartLearning()
    np.save('QTable', QTable)


# In[ ]:




