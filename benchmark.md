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

Maybe we can make the embodiment grow as it eats herbs, and a goal would be to become longer.

Let's make an even simpler version where the agents are already encoded as a sequence of agents and intents and observations. Then we don't need to extract and characterize the agencies.

We can also have a variant where the controls are transparent and the agent doesn't need to learn the control model. It can already see what "buttons" each other agent pressed. This becomes just a slight generalization of imitation learning.

Let's make it even simpler, go all the way to the basics. Make it a line world, not a grid world. There are only two choices for movement, left or right, and the agent is shown traces where another agent makes preference selections of which color pixels they want to eat.

## Stage 1 - Passive learning

> "What are the laws of this world from my subjective experience?"

At this stage we show the system a large number of trajectories
in a virtual ecosystem with different kinds of agents with varying goals
and affordances.

It is suggested that learning an agentic world model from this data should help in the next stages.

## Stage 2 a - Embody

> "Which one am I? How do I move?"

The ego agent is embodied to a random agent embodiment in a simulated ecosystem, and
it needs to learn a mapping between its outputs and agent's movements.

It is suggested that the agent can leverage its agentic world model and control counterfactuals from it to understand what its controls cause. Using causal learning of the controls will help the agent in the subsequent stage.

## Step 2 b - Pursue

> "I must reach my goal."

The ego agent will be provided a representation of the goal to pursue. This should probably be implicit and depend on the body recognized as self. So e.g. blue things do certain thing in the passive observation, red things do another thing, and the ego agent needs to imitate, or behave natural.

Once it has learned the embodiment, it will need to start pursuing its objective.

It is suggested that the agent can utilize both the agentic world model and its own control model to plan and pursue given objectives in a sensible and efficient fashion with minimal trial and error.

## Open Questions

1. How to encode the objectives? How to make the agent understand them?
2. What dynamics should the virtual grid world implement?
3. What kinds of variability in the dynamics we want to implement to make hard-coded solutions infeasible?
4. How to represent control, i.e. the action space?

