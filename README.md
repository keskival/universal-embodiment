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
produces a self-supervised token sequence which incorporates intents and a sea of agency in an organic and controllable fashion.

## Citing

Recursive Self-improvement Suite

```
@article{keskival2024universal,
  title={Universal Embodiment},
  author={Keski-Valkama, Tero},
  year={2024}
}
```

## References

- [Genie: Generative Interactive Environments](https://deepmind.google/research/publications/60474/)

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
