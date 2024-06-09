# Universal Embodiment

Universal Embodiment is a rethinking of classical reinforcement learning principles to be based on
mining of abundant third party experience in heterogeneous signals rather than naively leaning
on ego experience alone.

It is a way to train a foundation model for robotic control which isn't tied to any specific embodiment,
but which can inhabit any robotic body or a machine opportunistically. It is based on in-context learning
of control policies.

Its basic premise is recognizing all agency and intentionality in natural signals, to learn maximally from third-party experience,
side-stepping the RL ego learning bottlenecks.
Ego becomes just a special case of "other".

We will also implicitly get natural expectations of what would others do if they were ego as counter factuals against
robotic ego control signals.
This allows natural recognition of degrees of freedom and the reach of ego in any arbitrary embodiment.
It also allows empathy, better prediction of what others plan and how they will act, and true collaboration in a living world.
The living world is an ocean of agency, not a single-player game for which classic RL was designed for.

Since large models are data-defined, and this isn't an exception, this could be described as a scheme to synthesize intentional agentic token sequences from observing the living world across multiple modalities.

## Applications

This framework has applications in all complex and unstructured environments, at least in following domains:
- Space, ocean, underground exploration
- Disasters and rescue
- Military and defence

## General Principles

All highly developed animals learn from the experience of others, whether others are of the same species, individuals of totally
different species, or even non-living dynamic phenomena. The living world is an ocean of agency which is qualitatively different from
the desert of agency of single player games the traditional reinforcement learning has been designed for. Mining the abundant
agency in the signals from the living world allows learning how to inhabit any body and how to act in the physical world
from abundant bits of information compared to scarce bits of information present in ego learning alone.

Learning from experience of others, and considering ego as just one of the others, allows organic exploitation of observed experience
of others, to generalize to an arbitrary ego embodiment, to quickly learn to take control of any machine body in a purposeful fashion.

Learning control policies should happen in-context rather than on the level of backpropagated learning objectives. This allows
learning and adapting robotic control models faster than with engineered learning rules, which allows quick adaptation to new or changed
embodiments.

This isn't traditional reinforcement learning guided by sparse rewards. It would be madness to try to do sparse reward odelling for the entire living world. Instead we'll model the reinforcement through intents which don't suffer from the same problems as reward-based reinforcement learning does.

Did you know you don't have to use just plain autoregressive objective for token sequences?

## Main Challenges

### 1. Data from a living world

Data is where it all starts. How do we collect and refine a lot of multimodal
data which represents oceans of agency and intent.

Some initial sources:
- Nature documentaries
- Traffic videos
- Simulations and synthetic data

### 2. Real-time high-volume data tokenization

Embodied data and control signals are asynchronous, real-time and of a very
high volume. How to handle these, considering the context-length constraints
of existing large models.

- Hierarchical contexts, where higher level contexts are appended only occasionally based on lower level context token streams.
- Registries where the contexts can read and write long-term data.
- More modern long-context large model architectures.

### 3. In-context learning of robotic control

To support in-context learning of robotic control, we'll need ways to both
represent agency and control in multi-modal token sequences, but also something
analogous to instruct-tuning (or nowadays instruct training) in LLMs, which allows
us to instruct, command, or intervene to the token sequences to
direct them towards ego level intents and goals.

- Multi-modal asynchronous token sequences representing both observations and control signals.
- Generalist encoding of control signals spanning line level protocols, TCP/IP, protobuf and everything.
- Intent-encoding the data, so that overriding intents by token level interventions allows controllability.

Intent encoding is tricky in practice because we need to mine the intents from other agents to be able to encode them.

Mining intents can be done in a self-supervised process which:
1. Recognizes agents and their degrees of freedom and perception constraints,
2. Recognizes their intents and uses those, and their estimated perception to predict their actions,
3. Closes the loop by using the actions to predict the next state of the world in observable signals.

Doing the above requires some clever tricks which I haven't yet written down here, but it
produces a self-supervised token sequence which incorporates intents and an ocean of agency in an organic and controllable fashion.

## Intent-based Tokenization

One of the main contributions of this work is intent-based tokenization which serves an analogous purpose to
instruct-tuning or instruct-training of large language models. In instruct-tuning the language sequences are
separated into instruction and instruction following. By convention, the instruction comes first and is marked
as a message from the user (or in some cases system). The tokens aren't otherwise specially marked but their role
is clear from the context. The data is organized so that the instruction following tokens are conditioned by
the instruction tokens so that they provide controllability.

We need to extend this into robotic control in a more universalist fashion.

Let's first consider a single agent. In practical use we'll have an interlaced sequences with multiple agents,
but the general idea remains the same, and tokens for one recognized agent will have an intrinsic bond to other
tokens relating to that agency. We'll later get into how the tokens are negotiated between different agencies
in competitive optimization.

Instead of language based instructions, or indeed, intents, we'll simply denote tokens into specific classes.
It becomes a bit more complex than in plain instruction following, but this complexity serves a purpose.
We will have the following kinds of tokens forming a sequence of agentic action:
1. AGENT (a sequential embedding of who or what this is: Encodes the identity, degrees of freedom, observational constraints, appearance, ...)
2. INTENT (a sequential embedding of what is the current intent of the agent: Encodes the immediate goals of the agent.)
3. ACTION (a sequential embedding limited by an information bottleneck, which is roughly analogous to a chosen action.)
4. OBSERVATION (a sequential embedding describing the world and changes in it.)

These tokens have inherent relations to each others, and inherent causations and correlations which can be used to train
these embeddings and sequences with self-supervision:
1. The AGENT, INTENT and OBSERVATION token sequences from the past wholly condition the subsequent ACTION tokens of the agent in question.
2. OBSERVATION tokens wholly condition an estimate for all the raw signal data received at the moment and in the immediate future. The raw signal data also conditions the observation tokens.
3. ACTION tokens wholly condition the estimate of the causally following OBSERVATION tokens which relate to the agent, which basically segment the regions
   of the observed signals which can be predicted by the agent's actions. This produces an outline of the agent's span in the signals,
   no matter if imagery, sound, or anything else. ACTION tokens are inherently causal, and predict the changes in the signals observed.

The above list of relations is not exhaustive yet.

Using the above relations we can form self-supervised objectives which make sure these tokens converge into meaningful representations.

A keen reader notices that we don't get the mentioned token sequences from raw corpuses, like we do get textual tokens from internet text corpuses for large language models. But that's not important. We actually don't get instruction following from raw internet text either; it requires some data refinement.

If you know classical reinforcement learning, you should be reminded of SAR-sequences of state-action-reward in the above suggested intent-based tokenization. For those sequences we also only get the state and the reward from the environment; the action is generated by the agent. It is analogous here, except we just have many agents and don't control the actions. We will need self-supervised objectives to converge these agent, intent, observation and action representations into causal and predictive representations which in effect decompose the observed signals into an explaining set of agents and their dynamics. This decomposition process produces the token sequences, where the subobjectives are intertwined into the substrate of the token regressive model.

If you notice that we're trying to decompose dynamics in observations into low dimensional representations (actions, like in DeepMind Genie), you can see how ACTION tokens emerge. If you notice that we need to separate different agents, you'll see how the AGENT tokens support this separation. And in between sit the INTENT tokens allowing for controllability, you'll see this isn't ad-hoc, but a clean system which has only the representations which are needed and nothing superfluous.

All that we need to get such controllability over universal embodiments is to define generative data processes which generate these kinds of sequences, and we'll do that with a set of self-supervised objectives in an inherently generative sequence model.

All the tokens form one sequence, but certain objectives mask out tokens of specific types to impose correct information flows.

## Multi-agent Deconflicting

A single agent typically affects only its immediate locality, whether it's in image space, or in any other signaling modality,
depending on the degrees of freedom and presence of the agent. To define an optimizing model which is able to converge
into representing separate agents realistically, it is necessary to have competitive optimization objectives in a way where
ACTION tokens by one agent are predictive of some region in the observed signals, while ACTION tokens of another agent are less so.

This strength of predictive power of ACTION tokens in span of signal localities will define the reaches of discrete agents.

Overall, the system will be built so that observing media or signals from the living world, it is able to recognize all the different
agents, whether hierarchical or not, and their inherent intents and actions in the space of those signals, and ultimately
generalize the experience it so extracts into ego control models.

Multi-agent competitive deconflicting is a set of self-supervised objectives which allow the system to separate the explaining factors of the observation dynamics into a set of agent representations. Agent representations impose coherence on the intents which are conditioned by the agent and its history, which in turn impose coherence on the actions for each agent. Additionally, depending on signal modalities, there might be a need to impose connectedness and locality objectives for each agent.

Hierarchical agents can be represented as compositions conditioned by the higher level representations.

## Ego Control

How do we "instruct" such a model? Simply, we inject intents, and observe what changes in the world these intents produce through
the actions they induce. This lets an embodied agent learn of its own reach, while utilizing experience mined from observing other
agents in the world.

In addition to actions, we need to project these actions into practical hardware control signals. This is a still open problem, but certainly
doable with a separate model which tries to learn the control language and translate the actions into that.

## Asynchronicity

Classical reinforcement learning is typically formulated as a synchronous sequence of state-action-reward, indeed derivimg the name of the SARSA algorithm from those.
Here, we instead want the token sequences to be asynchronous.
Asynchronous token sequences are driven by a stream of observation tokens. To support predictive objectives, the model can emit other tokens of agents, intents and actions. This is a simple asynchronous decomposition of causal dynamics in the sequence of observation tokens.

## Translation of Tokens

For example intent tokens aren't inherently in plain human language; they are just good representations of intents. There are luckily a lot of existing art in translating such token representations into human language and back, for example by CLIP embeddings, or by training a model mapping large multimodal model descriptions of intents of agents in scenes into intent representations in the universal embodiment system.

Translation from actions to raw control signals also requires these sorts of translations, and also from raw observation signals to observation tokens and back.

## Objectives

### Basic Predictive Observation

The sensory input pipeline is complicated by the fact that it is asynchronous, interlaced multimodal stream which
needs to be encoded as dense representations first before combining them into world state observations.

First of all, the sensory input pipeline is encoded into simple modality-dependent autoencoding representations.
That means that we have an encoder and a decoder for each sensory modality which can produce an embedding from the
signal slice or frame, and conversely, can produce a signal slice from the embedding, trained by a simple
reconstruction loss. This is just to compress the otherwise high redundancy signals.

We want to go further than that though. We want to represent the observation stream as sequences of tokens which
are independent of modality, while these encoders and decoders and their representations are modality dependent.
We also want to make the observation stream tokens represent surprise or change.

The OBSERVATION token is determined by the previous OBSERVATION tokens and the input data stream encoded
in patches or slices in small representations. This means it represents a change or delta to what the previous
OBSERVATION token sequence already encoded, in a multi-modal fashion, conditioned on tokens from any modality.
Conversely, we'll have a decoder side for this as well, producing the original dense input representation
from the sequence of OBSERVATION tokens. The decoder produces any of the next slice representations in any modality.

The sequence of the observation tokens must be such that they predict the current and the following observations
as well as possible.
This forces the first observation tokens to encode the general whole of the observational context, and the subsequent
ones encoding the dynamics and the changes to that.

To make the token representations forecast oriented and causal, they will need to not only predict the next frames
and signal slices, but the subsequent ones as well. Hence we'll condition the encoder with the time index as well,
so that it is able to do some amount of limited forecast to the future as well, just based on the information encoded
in the OBSERVATION token. Conversely, this delayed reconstruction loss forces the OBSERVATION token encode in as much
dynamics of the world as possible.

OBSERVATION tokens are rated to be synchronous with the input data slices coming in, a constant number of OBSERVATION
tokens corresponding to the newest sensory information packet. This forms the basic clock of the system, and everything
else is dependent on the input token cadence.

### Agent Tokenization

AGENT tokens decompose the OBSERVATION tokens into regions where each agent has presence and reach. After each OBSERVATION
token, we will induce a set of AGENT tokens which represent the agents present in the observable world.
Each of these AGENT tokens will attend to the previous OBSERVATION token sequence in a competitive fashion so that best matching
AGENT tokens will claim specific OBSERVATION tokens.

This means that we'll force the AGENT token to represent the appearance of a single agent (among other things). The AGENT
token needs to be able to condition an decoder which produces the tokens it attends to, and the set of all AGENT token decoders
need to be able to produce the whole scene, that is, a sequence of OBSERVATION tokens relating to the current world.
Since the sequence of OBSERVATION tokens probably cannot be made exactly unambiguous, we'll need to use a reconstruction loss
which depends on the reconstruction of the current scene in the sensory input signal domains.

The scheme has competing objectives: First of all, all AGENT tokens need to contain information for reconstruction of the whole scene.
Additionally, since each AGENT token can only encode so much presence information in the scene, they will need to distribute
the representational capacity between themselves in a competitive fashion, so that each AGENT token will come to represent some
coherent locality in the input signals.

The sequence of AGENT tokens associated to the previous OBSERVATION token will condition the next sequence of AGENT tokens to conserve
the agents over time.

### Action Tokenization

Similarly to DeepMind Genie, which has a reconstructive loss objective for a model generating the dynamics of a single-player game views from a single, inferred, low-dimensional encoding of an action, we will do the same but for multiple agents.

An ACTION token is always tied to a specific pair of AGENT tokens across sequential OBSERVATION tokens, so that the ACTION represents the information required to represent the change in the AGENT token over time.

It does this by basic information bottleneck and self-supervised reconstructive objectives.

### Intent Tokenization

Finally as we have grounding for OBSERVATION, AGENT and ACTION, we'll ground the INTENT tokens by forcing their representations to predict the sequences of ACTION tokens, while being consistent over time for a single agent.

These tokens provide controllability within context, so that injecting INTENT tokens to the ego agent will induce subsequent ACTION tokens, but also en evolution of coherent INTENT tokens which conserve the original controlling intent but also react to the changing circumstances in the world.

Unintervented INTENT tokens will evolve over time similarly as agent intents evolve in the training materials.

## Citing

Universal Embodiment

```
@article{keskival2024universal,
  title={Universal Embodiment},
  author={Keski-Valkama, Tero},
  year={2024}
}
```

## References

- [Genie: Generative Interactive Environments](https://deepmind.google/research/publications/60474/)
- [Recognizing Everything from All Modalities at Once: Grounded Multimodal Universal Information Extraction](https://arxiv.org/abs/2406.03701v1)

## Related Posts

- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7197360229779435520-Ob6T](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7197360229779435520-Ob6T)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7192888281502511104-9RgC](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7192888281502511104-9RgC)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7189275168412733440-8VjI](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7189275168412733440-8VjI)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7182658395991134208-odsl](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7182658395991134208-odsl)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7177348690838233089-B6iK](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7177348690838233089-B6iK)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-universalembodiment-universalembodiment-activity-7177319114363846656-7W-U](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-universalembodiment-universalembodiment-activity-7177319114363846656-7W-U)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7177256036314013697-I6hl](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7177256036314013697-I6hl)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7175129606159515649-zVlV](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7175129606159515649-zVlV)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7174712111506284544-2dme](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7174712111506284544-2dme)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7174157973626249216-eIOF](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7174157973626249216-eIOF)
- [https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7172248302460125184-jj9w](https://www.linkedin.com/posts/terokeskivalkama_universalembodiment-activity-7172248302460125184-jj9w)
