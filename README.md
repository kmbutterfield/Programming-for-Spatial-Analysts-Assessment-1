# Programming for Spatial Analysts Assessment 1
Here you will find the final code for an agent-based model that was built following practical sessions from the module: Programming for Spatial Analysts: Core Skills in Python. This module is part of my MA Social Research (Interdisciplinary) programme, which has taught me the Python language, allowing me to utilise this skill during my PhD at the University of Leeds.

## About the Model
Following the weekly practicals allowed me to produce an agent-based model (ABM) written in Python, that features agents that eat their environment. There are three key parts to the ABM; the framework, the model itself, and an environment that contains data that is read into the model.

### Key Model Notes
* The environment can be altered by the agents as they eat their way around.
* The agents know that they are not alone in the model and can interact such as being able to share 'data' stores.
* If an agent is in the way of another, it will move around the environment, and not on top of the other agent.
* Each agent has a data store capacity of 1000, if it consumes any more data it will vomit, depositing all of its data stores.
* The behaviours of each agent in their environment can be viewed as an animation. If a piece of data has been consumed by an agent, the environment patch will change colour and will have a decreased data store.
