"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018, University of Alberta.
  Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlo agent using RLGlue.
"""
from rl_glue import RLGlue
from sarsa_agent import sarsaAgent
from windygridworld_env import windyGridenv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    max_steps = 8000
    num_runs = 10

    for n in range(4):
        # Create and pass agent and environment objects to RLGlue
        environment = windyGridenv()
        agent = sarsaAgent()
        rlglue = RLGlue(environment, agent)
        if n == 0:
            rlglue.rl_agent_message("alpha = 0.3")
            message = "alpha = 0.3"
        elif n == 1:
            rlglue.rl_agent_message("alpha = 0.5")
            message = "alpha = 0.5"
        elif n == 2:
            rlglue.rl_agent_message("alpha = 0.7")
            message = "alpha = 0.7"
        else:
            rlglue.rl_agent_message("alpha = 0.9")
            message = "alpha = 0.9"
        rlglue.rl_agent_message("epsilon = 0.1")
        rlglue.rl_agent_message("4")
        del agent, environment  # don't use these anymore

        time_steps = []
        for a in range(0,8000):
            time_steps.append(0)

        for run in range(num_runs):

            print("run number: {}\n".format(run))


            # initialize RL-Glue
            rlglue.rl_init()
            rlglue.rl_start()
            for num in range(max_steps):
                _,_,_,terminal = rlglue.rl_step()
                if terminal == True:
                    rlglue.rl_start()
                    time_steps[num]+=1
        m = list(range(8000))
        length = len(time_steps)
        for a in range(length-1):
            time_steps[a+1] += time_steps[a]
        for w in range(length):
            time_steps[w] = time_steps[w]/num_runs
        plt.figure(1)
        plt.ylabel("Episodes completed")
        plt.xlabel("Time steps")
        plt.title("Four actions SARSA, 10 runs, epsilon = 0.1")
        plt.plot(m,time_steps,label=message)
        plt.yticks([0, 50, 100, 150, 170], ["0", "50", "100", "150", "170"])
        plt.legend()
        plt.draw()


    for n in range(4):
        # Create and pass agent and environment objects to RLGlue
        environment = windyGridenv()
        agent = sarsaAgent()
        rlglue = RLGlue(environment, agent)
        if n == 0:
            rlglue.rl_agent_message("alpha = 0.3")
            message = "alpha = 0.3"
        elif n == 1:
            rlglue.rl_agent_message("alpha = 0.5")
            message = "alpha = 0.5"
        elif n == 2:
            rlglue.rl_agent_message("alpha = 0.7")
            message = "alpha = 0.7"
        else:
            rlglue.rl_agent_message("alpha = 0.9")
            message = "alpha = 0.9"
        rlglue.rl_agent_message("epsilon = 0.1")
        rlglue.rl_agent_message("8")
        del agent, environment  # don't use these anymore

        time_steps = []
        for a in range(0,8000):
            time_steps.append(0)

        for run in range(num_runs):

            print("run number: {}\n".format(run))


            # initialize RL-Glue
            rlglue.rl_init()
            rlglue.rl_start()
            for num in range(max_steps):
                _,_,_,terminal = rlglue.rl_step()
                if terminal == True:
                    rlglue.rl_start()
                    time_steps[num]+=1
        m = list(range(8000))
        length = len(time_steps)
        for a in range(length-1):
            time_steps[a+1] += time_steps[a]
        for w in range(length):
            time_steps[w] = time_steps[w]/num_runs
        plt.figure(2)
        plt.ylabel("Episodes completed")
        plt.xlabel("Time steps")
        plt.title("Eight actions SARSA, 10 runs, epsilon = 0.1")
        plt.plot(m,time_steps,label=message)
        plt.yticks([0, 50, 100, 150, 170], ["0","50","100","150","170"])
        plt.legend()
        plt.draw()


    for n in range(4):
        time_steps = []
        for a in range(0, 8000):
            time_steps.append(0)
        agent = sarsaAgent()
        environment = windyGridenv()
        rlglue = RLGlue(environment,agent)
        if n == 0:
            rlglue.rl_agent_message("alpha = 0.3")
            message = "alpha = 0.3"
        elif n == 1:
            rlglue.rl_agent_message("alpha = 0.5")
            message = "alpha = 0.5"
        elif n == 2:
            rlglue.rl_agent_message("alpha = 0.7")
            message = "alpha = 0.7"
        else:
            rlglue.rl_agent_message("alpha = 0.9")
            message = "alpha = 0.9"
        rlglue.rl_agent_message("epsilon = 0.1")
        rlglue.rl_agent_message("9")
        del agent,environment
        for run in range(num_runs):
            print("run number: {}\n".format(run))
            rlglue.rl_init()
            rlglue.rl_start()

            for num in range(max_steps):
                _,_,_,terminal = rlglue.rl_step()
                if terminal == True:
                    rlglue.rl_start()
                    time_steps[num]+=1

        m = list(range(8000))
        length = len(time_steps)
        for a in range(length-1):
            time_steps[a+1] += time_steps[a]
        for w in range(length):
            time_steps[w] = time_steps[w]/num_runs
        plt.figure(3)
        plt.ylabel("Episodes completed")
        plt.xlabel("Time steps")
        plt.title("Nine actions SARSA, 10 runs, epsilon = 0.1")
        plt.plot(m,time_steps, label=message)
        plt.yticks([0, 50, 100, 150, 170], ["0", "50", "100", "150", "170"])
        plt.legend()

    plt.draw()
    plt.show()

