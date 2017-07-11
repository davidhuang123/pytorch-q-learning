from ReplayBuffer import ReplayBuffer
from Environment import Environment
import gym
import numpy as np
from Agent import Agent
from stolen_openai_wrappers import wrap_dqn

agent = Agent(2)
_env = wrap_dqn(gym.make("PongDeterministic-v4"))
env = Environment(_env,0,False,[2,3],False,-1,1)
agent.load_weights("./zwischenstand_model.torch")
agent.train(100,32,env,1000000,1000000,0.1)
