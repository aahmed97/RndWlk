"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
   Monte Carlo agent using RLGlue - barebones.
"""
from rl_glue import BaseAgent
import numpy as np


class sarsaAgent(BaseAgent):
    """
    Monte Carlo agent -- Section 5.3 from RL book (2nd edition)

    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """

    def __init__(self):
        """Declare agent variables."""
        act = []
        self.Q = []
        self.alpha = 0
        self.epsilon = 0
        self.last_state = [0,0]
        self.num_eps_completed = 0
        self.num_actions = 0


    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        """
        self.Q = [[[0 for x in range(self.num_actions)] for y in range(7)] for a in range(10)]
        self.last_state = [0, 0]
        self.num_eps_completed = 0


    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        Hint: Initialize the variables that you want to reset before starting
        a new episode, pick the first action, don't forget about exploring
        starts
        """
        # for s in state:
        #     for a in range(1,min(s,100-s)):
        #         self.Returns[s][a] = 0
        x = state[0]
        y = state[1]
        prob = np.random.rand()
        if (prob >= self.epsilon):
            action = self.Q[x][y].index(max(self.Q[x][y]))
            length = len(self.Q[x][y])
            for i in range(action+1,length):
                if (self.Q[x][y][action] == self.Q[x][y][i]) and action!=i:
                    flip = np.random.randint(0,2)
                    if flip == 1:
                        action = i
            self.last_action = action
        else:
            action = np.random.randint(0,self.num_actions)
            self.last_action = action
        self.last_state = [x,y]
        return self.last_action

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        Hint: select an action based on pi
        """
        self.num_eps_completed = 0
        x = state[0]
        y = state[1]
        last_x = self.last_state[0]
        last_y = self.last_state[1]
        prob = np.random.rand()
        if (prob >= self.epsilon):
            action = self.Q[x][y].index(max(self.Q[x][y]))
            length = len(self.Q[x][y])
            for i in range(action,length):
                if (self.Q[x][y][action] == self.Q[x][y][i]) and action!=i:
                    flip = np.random.randint(0,2)
                    if flip == 1:
                        action = i
        else:
            action = np.random.randint(0,self.num_actions)
        self.Q[last_x][last_y][self.last_action] = self.Q[last_x][last_y][self.last_action] + self.alpha * (reward + self.Q[x][y][action] - self.Q[last_x][last_y][self.last_action])
        self.last_state[0] = x
        self.last_state[1] = y
        self.last_action = action
        return action



    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        # return
        self.num_eps_completed+=1




    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        alpha_str = ""
        eps_str = ""
        num_str = ""
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        if "alpha" in in_message:
            for x in in_message:
                if x in numbers:
                    alpha_str+=x
            self.alpha = float(alpha_str)
        elif "epsilon" in in_message:
            for x in in_message:
                if x in numbers:
                    eps_str+=x
            self.epsilon = float(eps_str)
        else:
            for x in in_message:
                if x in numbers:
                    num_str+=x
            self.num_actions = int(num_str)
        return


