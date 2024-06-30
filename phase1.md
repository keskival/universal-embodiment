## Phase 1: Towards Proof-of-Concept

Goal: We need to prove that a model with a multi-agentic bias can
learn autoregressive prediction of videos which decomposes
agents, intents and actions.

We will use [Sports Videos in the Wild](https://cvlab.cse.msu.edu/project-svw.html)
to train a structured video prediction model.

To prove decomposition, we will follow the ideas of
[Genie: Generative Interactive Environments](https://deepmind.google/research/publications/60474/)
and create interventions to the contained agent, intent and action embeddings,
and observe the results. We will also use XAI methods to check what parts
of the inputs each embedding is conditional on through attention and activation maps.

Since the volume of data is very small, we will need to make compromises
on the level of quality and utility we expect to achieve,
and we will for example utilise existing image backbones
for frame embeddings. We will also actively hunt for more data.
