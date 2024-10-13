"""This is a 1-D grid world with random rules for each run.
The rules are in the form of a table with n agent types having
different reward preferences (positive or negative) for each of
the m prey types.
The agent types and the prey types have random RGB colors associated."""

import numpy as np


rng = np.random.default_rng()


def _get_preferences(num_prey_types: int):
    """The reward/penalty for eating this prey type."""
    return rng.uniform(-1, 1, num_prey_types)


def _get_color(start, delta):
    """A color for an agent or prey."""
    color = np.array(start)
    delta = np.array(delta)
    while (True):
        yield color
        color = (color + delta) % 256


def _get_color_agent():
    """A color for an agent."""
    while (True):
        yield _get_color([10, 240, 70], [5, 15, 44])


def _get_color_prey():
    """A color for a prey."""
    while (True):
        yield _get_color([140, 40, 20], [58, 23, 104])


class World():
    """Defines the world rules."""
    
    def __init__(self, num_agent_types: int, num_prey_types: int, size_world: int):
        self.num_agent_types = num_agent_types
        self.num_prey_types = num_prey_types
        self.size_world = size_world

        self.rules = [_get_preferences(num_prey_types) for agent_type in range(num_agent_types)]
        self.agent_colors = [_get_color_agent() for agent_type in range(num_agent_types)]
        self.prey_colors = [_get_color_prey() for prey_type in range(num_prey_types)]


if __name__ == "main":
    world = World()
