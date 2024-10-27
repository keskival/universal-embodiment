from selfgensys.universal_embodiment.benchmark import get_best_choice, Rules, World

def test_get_best_choice1():
    rules = Rules(num_agent_types=1, num_prey_types=3, size_world=10)
    rules.preferences = [[5.0, -1.0, -1.0]]
    world = World(rules=rules, num_prey=3)
    # Let's make the right prey of negative value, and the left prey as well
    # but the left-most prey of a higher positive value.
    world.prey_positions = [3, 4, 6]
    # The correct action is to take both preys to the left and leave the prey
    # on the right.
    world.agent_type = 0
    world.prey_types = [0, 1, 2]
    move = world.get_optimal_move()
    assert(-1 == move)
    world.move(move)
    move = world.get_optimal_move()
    assert(-1 == move)
    world.move(move)
    move = world.get_optimal_move()
    assert(move is None)

def test_get_best_choice2():
    rules = Rules(num_agent_types=1, num_prey_types=3, size_world=10)
    rules.preferences = [[5.0, 1.0, 1.0]]
    world = World(rules=rules, num_prey=3)
    # Let's make all preys positive value.
    world.prey_positions = [3, 4, 2]
    # The correct action is to take all preys to the left.
    world.agent_type = 0
    world.prey_types = [0, 1, 2]
    move = world.get_optimal_move()
    assert(-1 == move)
    world.move(move)
    move = world.get_optimal_move()
    assert(-1 == move)
    world.move(move)
    move = world.get_optimal_move()
    assert(-1 == move)
    world.move(move)
    move = world.get_optimal_move()
    assert(move is None)
