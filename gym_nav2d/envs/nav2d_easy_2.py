from gym import error, spaces, utils
import numpy as np
import math

from gym_nav2d.envs.nav2d_env_2 import Nav2dEnv2


class Nav2dEasyEnv2(Nav2dEnv2):
    metadata = {'render.modes': ['human', 'ansi', 'rgb_array'],
                'video.frames_per_second': 30}

    def __init__(self):
        Nav2dEnv2.__init__(self)

    def reset(self):
        # Changing start point and fixed goal point
        self.count_actions = 0
        self.positions = []
        #self.agent_x = self.np_random.uniform(low=0, high=self.len_court_x)
        #self.agent_y = self.np_random.uniform(low=0, high=self.len_court_y)
        #self.goal_x = 127
        #self.goal_y = 127
        self.goal_x = self.np_random.uniform(low=0, high=self.len_court_x)
        self.goal_y = self.np_random.uniform(low=0, high=self.len_court_y)
        self.agent_x = 127   
        self.agent_y = 127
        #print(self.goal_x,self.goal_y)
        self.goal_x_agent = self.goal_x - self.agent_x
        self.goal_y_agent = self.goal_y - self.agent_y
        if self.goal_y == self.agent_y or self.goal_x == self.agent_x:
            self.reset()
        self.positions.append([self.agent_x, self.agent_y])
        if self.debug:
            print("x/y  - x/y", self.agent_x, self.agent_y, self.goal_x, self.goal_y)
            print("scale x/y  - x/y", self.agent_x*self.scale, self.agent_y*self.scale, self.goal_x*self.scale,
                  self.goal_y*self.scale)
        obs = self._observation()

        return self._normalize_observation(obs)
