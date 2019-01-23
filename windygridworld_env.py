"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018,
  University of Alberta.
  Gambler's problem environment using RLGlue.
"""
from rl_glue import BaseEnvironment
import numpy as np


class windyGridenv(BaseEnvironment):
    """
    Slightly modified Gambler environment -- Example 4.3 from
    RL book (2nd edition)

    Note: inherit from BaseEnvironment to be sure that your Agent class implements
    the entire BaseEnvironment interface
    """

    def __init__(self):
        """Declare environment variables."""

    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """
        self.state = []
        self.last_state = []



    def env_start(self):
        """
        Arguments: Nothing
        Returns: state - numpy array
        Hint: Sample the starting state necessary for exploring starts and return.
        """
        self.last_state = [0,3]
        return self.last_state

    def env_step(self, action):
        """
        Arguments: action - integer
        Returns: reward - float, state - numpy array - terminal - boolean
        Hint: Take a step in the environment based on dynamics; also checking for action validity in
        state may help handle any rogue agents.
        """
        x = self.last_state[0]
        y = self.last_state[1]

        if action == 0:
            new_y = y-1
            new_x = x
            if (new_y < 0):
                new_y = y
        elif action == 1:
            new_y = y+1
            new_x = x
            if (new_y >= 7):
                new_y = y
        elif action == 2:
            new_y = y
            new_x = x-1
            if (new_x < 0):
                new_x = x
        elif action == 3:
            new_y = y
            new_x = x+1
            if (new_x >= 10):
                new_x = x
        elif action == 4:
            new_x = x+1
            new_y = y+1
            if ((new_x >= 10) or (new_y >= 7)):
                new_x = x
                new_y = y
        elif action == 5:
            new_x = x-1
            new_y = y-1
            if ((new_x < 0) or (new_y <0)):
                new_x = x
                new_y = y
        elif action == 6:
            new_x = x+1
            new_y = y-1
            if ((new_x >= 10) or (new_y < 0)):
                new_x = x
                new_y = y
        elif action == 7:
            new_x = x-1
            new_y = y-1
            if ((new_x < 0) or (new_y < 0)):
                new_x = x
                new_y = y
        elif action == 8:
            new_x = x
            new_y = y

        if (x == 3 or x == 4 or x == 5 or x == 8):
            wind_y = new_y-1
            if (wind_y >= 0):
                new_y = wind_y
        elif (x == 6 or x ==7):
            wind_y = y-2
            if (wind_y >= 0):
                new_y = wind_y

        if(new_x == 7 and new_y == 3):
            terminal = True
        else:
            terminal = False
        reward = -1
        self.last_state = [new_x,new_y]
        return reward, self.last_state, terminal




    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass


