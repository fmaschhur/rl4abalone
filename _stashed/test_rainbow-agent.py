import random

import gym

import torch
import numpy as np

from agents.rainbow.agent import RainbowAgent
from agents.rainbow.config import RainbowConfig

AGENT_FILE_PATH: str = "rainbow-agent.pth"
LOAD_FROM_FILE: bool = False


def seed_torch(seed):
    torch.manual_seed(seed)
    if torch.backends.cudnn.enabled:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True


env = gym.make("abalone-v0")

seed = 777

np.random.seed(seed)
random.seed(seed)
seed_torch(seed)
env.seed(seed)

num_frames = 2000
memory_size = 1000
batch_size = 128
target_update = 100


if LOAD_FROM_FILE:
    with open(AGENT_FILE_PATH, "rb") as f:
        agent = torch.load(f, map_location=torch.device('cpu'))
        agent.reset_torch_device()
else:
    config = RainbowConfig()
    agent = RainbowAgent(env, memory_size, batch_size, target_update, feature_conf=config)

