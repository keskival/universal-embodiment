# Mining Multi-agent Experience Benchmark

We aim to define a minimal benchmark which measures a capability of an agent in harvesting third party
experience and utilize it.

Let's make it a minimal grid world with pixels as entities.

One way to use it is to first show a demonstration how the rules
of the world work, and then test how fast the agent learns to
succeed in that world.

Goals shouldn't be based on rewards, because rewards aren't observable.
They should be based on intents.

The basic scheme should be based on static pixels of a specific color
spawning, representing herbs, and pixels of another color
representing herbivores to eat them.

There are no rewards from eating the herbs. It's just something herbivores
do if they want. And they do that in the demonstrations.

## Stage 1 - Passive learning

At this stage we show the system a large number of trajectories
in a virtual ecosystem with different kinds of agents with varying goals
and affordances.

## Stage 2 - Embody

The ego agent is embodied to a random agent embodiment in a simulated ecosystem, and
it needs to learn a mapping between its outputs and agent's movements.

The ego agent will be provided a representation of the goal to pursue.
