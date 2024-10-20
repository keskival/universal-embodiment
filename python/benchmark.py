"""This is a 1-D grid world with random rules for each run.
The rules are in the form of a table with n agent types having
different reward preferences (positive or negative) for each of
the m prey types.
The agent types and the prey types have random RGB colors associated."""

import numpy as np
import random
from PIL import Image
import copy
from collections import deque


rng = np.random.default_rng()


def _get_preferences(num_prey_types: int):
    """The reward/penalty for eating this prey type."""
    return rng.uniform(-1, 1, num_prey_types)


def _get_color(start, delta):
    """A color for an agent or prey."""
    color = np.array(start, dtype=np.uint8)
    delta = np.array(delta, dtype=np.uint8)
    while (True):
        yield color
        color = (color + delta) % 256


def _get_color_agent():
    """A color for an agent."""
    agent_generator = _get_color([10, 240, 70], [5, 15, 44])
    while (True):
        yield next(agent_generator)


def _get_color_prey():
    """A color for a prey."""
    prey_generator = _get_color([140, 40, 20], [58, 23, 104])
    while (True):
        yield next(prey_generator)


def get_best_choice(world) -> tuple[float, list]:
    """Depth first search. Returns the tuple of final score and a deque of all the moves to the end."""
    choices = []
    if len(world.prey_positions) > 0:
        # There are prey left.
        preys_left_of_agent = [prey_position for prey_position in world.prey_positions if prey_position < world.agent_position]
        preys_right_of_agent = [prey_position for prey_position in world.prey_positions if prey_position > world.agent_position]
        if len(preys_left_of_agent) > 0:
            # We have an option to take the prey on the left side.
            prey_position = max(preys_left_of_agent)
            move = prey_position - world.agent_position
            next_world_state = world.copy()
            next_world_state.move(move)
            choices.append((move, next_world_state))
        if len(preys_right_of_agent) > 0:
            # We have an option to take the prey on the right side.
            prey_position = max(preys_right_of_agent)
            move = prey_position - world.agent_position
            next_world_state = world.copy()
            next_world_state.move(move)
            choices.append((move, next_world_state))
        # Note that in running the plan we need to take multi-step moves as single moves.

    if len(choices) == 0:
        return (world.total_score, deque())
    score_before_this = world.total_score
    best_choice = None
    for choice in choices:
        (move, next_world) = choice
        # Choices are tuples of move and resulting world.
        # best choices are tuples of score and list of moves to the end.
        total_score, list_of_moves = get_best_choice(next_world)
        list_of_moves.appendleft(move)
        best_choice_for_this_path = (total_score, list_of_moves)
        if total_score < score_before_this:
            # A plan which reduces total score is not valid.
            continue
        if best_choice is None or best_choice[0] < total_score:
            best_choice = best_choice_for_this_path
        elif best_choice[0] == total_score:
            # We choose the shorter path in ties.
            if len(best_choice[1]) > len(best_choice_for_this_path[1]):
                best_choice = best_choice_for_this_path
    if best_choice is not None:
        # Returning the best choice.
        return best_choice
    else:
        return (world.total_score, deque())


class Rules():
    """Defines the world rules."""
    
    def __init__(self, num_agent_types: int, num_prey_types: int, size_world: int):
        self.num_agent_types = num_agent_types
        self.num_prey_types = num_prey_types
        self.size_world = size_world

        self.preferences = [_get_preferences(num_prey_types) for agent_type in range(num_agent_types)]
        agent_generator = _get_color_agent()
        self.agent_colors = list([next(agent_generator) for agent_type in range(num_agent_types)])
        prey_generator = _get_color_prey()
        self.prey_colors = list([next(prey_generator) for prey_type in range(num_prey_types)])


class World():
    """Defines the world state."""

    def __init__(self, rules: Rules, num_prey: int):
        self.rules = rules
        # We'll guarantee each prey is in its own non-overlapping position.
        available_positions_for_prey = list(range(rules.size_world))
        # Removing the place of the agent.
        self.agent_position = int(rules.size_world / 2)
        del(available_positions_for_prey[self.agent_position])
        self.prey_positions = random.sample(available_positions_for_prey, num_prey)
        self.agent_type = random.randint(0, rules.num_agent_types - 1)
        self.prey_types = np.random.randint(0, rules.num_prey_types - 1, num_prey)
        self.total_score = 0.0
        self.solution = None
    
    def get_diagram(self) -> np.array:
        """Returns a visualizable diagram of the world state."""
        diagram = np.zeros([self.rules.size_world, 3], dtype=np.uint8)
        for type, position in zip(self.prey_types, self.prey_positions):
            diagram[position, :] = self.rules.prey_colors[type]
        diagram[self.agent_position, :] = self.rules.agent_colors[self.agent_type]
        return diagram

    def move(self, move: int):
        new_position = self.agent_position + move
        if new_position < 0:
            new_position = 0
        if new_position >= self.rules.size_world:
            new_position = self.rules.size_world - 1
        for prey_index, prey_position in enumerate(self.prey_positions):
            if prey_position == new_position:
                # We eat this prey.
                prey_type = self.prey_types[prey_index]
                prey_value = self.rules.preferences[self.agent_type][prey_type]
                self.total_score += prey_value
                del(self.prey_positions[prey_index])
                self.prey_types = np.delete(self.prey_types, prey_index)
        self.agent_position = new_position

    def copy(self):
        """Clones the world state.
        Useful for the planner."""
        return copy.deepcopy(self)

    def get_optimal_move(self) -> int | None:
        """Returns either -1 or +1, for left and right respectively
        corresponding to the optimal move for the agent.
        Returns None when no moves are left."""
        # The planner has a tree of options where at each node it has:
        # 1. Take the prey left of the agent
        # 2. Take the prey right of the agent
        # 3. End
        # We'll traverse the whole tree and choose the best path.
        if self.solution is None:
            score_solution = get_best_choice(self)
            print(score_solution)
            self.solution = score_solution[1]
        # We need to peek the left-most plan item, and its sign is the move.
        # Then we'll need to decrement its absolute value by one, and if
        # it becomes zero, pop it out.
        if len(self.solution) == 0:
            return None
        move = np.sign(self.solution[0])
        self.solution[0] -= move
        if self.solution[0] == 0:
            self.solution.popleft()
        return move


if __name__ == "__main__":
    rules = Rules(num_agent_types=5, num_prey_types=5, size_world=10)

    num_runs = 10
    num_steps = 100
    for run_index in range(num_runs):
        frames = []
        world = World(rules=rules, num_prey=5)
        frame = world.get_diagram()
        frames.append(frame)
        for step in range(num_steps):
            move = world.get_optimal_move()
            if move is None:
                break
            world.move(move)
            frame = world.get_diagram()
            frames.append(frame)
        print(len(frames))
        image_array = np.stack(frames)
        print(image_array.shape, image_array.dtype)
        image = Image.fromarray(image_array)
        image.save(f"run_{run_index}.png")
