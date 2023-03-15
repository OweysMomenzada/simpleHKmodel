## Simple HK model

This implementation was developed in the context of a seminar at the UHH.
Note that this notebook is only for explanation purposes, it does not consider error handling, such as division by zero.

### Example usage
```
from HKmodel import model, agentsgenerator as ag

n = 200
dim = 1
min_val = 0
max_val = 1
epsilon = 0.1

agentmodul = ag.RandomAgents(n, dim, min_val, max_val) 
init_agents = agentmodul.generate_configuration()

model = model.HKmodel(init_agents, epsilon)

try:
    res = model.update_untilfreeze()
except: 
    print("System already froze on initial point.")
    res = init_agents
```

### Plot
You can than plot the results by using plotly:

```
import plotly.graph_objects as go

fig = go.Figure()

for agent in range(n):
    fig.add_trace(go.Scatter(y=[float(i[agent]) for i in res], 
                             mode='lines'))

fig.update_layout(title=f'HK-model on d={dim}, n={n}, epsilon={epsilon}, with the opinions range between {min_val} and {max_val}',
                   xaxis_title='timesteps t',
                   yaxis_title='some opinion of dimension d')

    
fig.show()
```
![exampleplot](/img/exampleplot.PNG "example plot")