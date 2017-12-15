# Programming for Spatial Analysts Assessment 1
Here you will find the final code for an agent-based model that was built following practical sessions from the module: Programming for Spatial Analysts: Core Skills in Python. This module is part of my MA Social Research (Interdisciplinary) programme, which trains me to learn the Python language, allowing me to utilise this skill during my PhD at the University of Leeds.

## About the Model
Following the practicals allowed me to produce an agent-based model (ABM) written in Python, that features agents that eat their environment. There are three key parts to the ABM; the framework, the model itself, and an environment that contains data that is read into the model.

### Key Notes
* The environment can be altered by the agents as they eat their way around.
* The agents know that they are not alone in the model and can interact.
* If an agent is in the way of another, it will move around the environment, and not on top.
* Each agent has a data store capacity of 1000, if it consumes any more data it will become sick, and will deposit its stores.
* The agent behaviours in their environment can be viewed as an animation has been coded in. If a piece of data has been consumed b an agent, the environment patch will change colour.
