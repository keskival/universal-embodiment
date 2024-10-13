"""This is a 1-D grid world with random rules for each run.
The rules are in the form of a table with n agent types having
different reward preferences (positive or negative) for each of
the m prey types.
The agent types and the prey types have random RGB colors associated."""


def _get_preference():
    """The reward/penalty for eating this prey type."""
    return 1


def _get_color_agent():
    """A color for an agent or prey."""
    color = (1.0, 1.0, 1.0)
    while (True):
        yield color
        color = color + (0.2, 0.3, 0.4)
        # TODO


def _get_color_prey():
    """A color for an agent or prey."""
    return (1.0, 1.0, 1.0)


class World():
    """Defines the world rules."""
    
    def __init__(self, num_agent_types: int, num_prey_types: int, size_world: int):
        self.num_agent_types = num_agent_types
        self.num_prey_types = num_prey_types
        self.size_world = size_world

        self.rules = [[_get_preference() for prey_type in range(num_prey_types)] for agent_type in range(num_agent_types)]
        self.agent_colors = [_get_color_agent() for agent_type in range(num_agent_types)]
        self.prey_colors = [_get_color_prey() for agent_type in range(num_agent_types)]


if __name__ == "main":
    world = World()
