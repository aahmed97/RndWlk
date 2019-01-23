# RndWlk

Written in Python, this is a Reinforcement Learning experiment where an agent tries to
reach a goal state in a grid and there is "wind" which pushes the agent north in the
gridworld. The agent, therefore, has to figure out the best way to escape in the shortest
number of time steps. The agent uses epsilon-greedy to choose actions and SARSA
to update the action-values.

The agent is programmed to complete three experiments each with a different number
of actions that the agent can take. The plots show the number of episodes (number of times the agent reaches the
  goal) as a function of the number of time steps in the experiment. I took a cumulative number representing
  the number of times that the agent reached the goal at a time step and averaged it over 10 runs and plotted it. The plots are labelled and
  available as well. 

  1) Four actions: Up, down, left, right
  2) Eight actions: the four above plus the four diagonal movements
  3) Nine actions: the eight above plus a ninth action which is to stay still
