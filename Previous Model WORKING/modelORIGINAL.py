# -*- coding: utf-8 -*-
"""

Created on Oct 30 20:54:02 2017

@author: ed12k3b

Programming for Geographical Information Analysts: Core Skills
Module taught for MA Social Research Methods (Interdisciplinary)
Module taught by Dr. Andy Evans, University of Leeds.

The ABM contains the three key code elements; model code, agent code, and environment code.
 
"""

# Import the modules required for model creation:

import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import agentframework
import csv
import requests
import bs4


# Beign to initialise the model using provided x and y data:

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


# Pythagoras code for calculating distance between the two agent coordinates:
                
def distance_between(agent0, agent1):
    return (((agent0.x-agent1.x)**2)+((agent0.y-agent1.y)**2))**0.5


# Creating model lists:
        # First, the environment for the agents to roam around in;
        # Second, the agent list which will be used within the environment.

environment = []
agents = []


# Defining model parameters such as number of agents, iterations, and neighbourhoods:

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 50


# Defining the ABM's window size for animation, and variabe axes:

fig = matplotlib.pyplot.figure(figsize=(8,8))
ax= fig.add_axes([0,0,1,1])


# Reading in the environmental data containing CSV and running it:

f =open('in.txt', newline='') 
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)


# Appending environment CSV into rows:

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item) 	
    environment.append(rowlist)


# Creating the agents, and appending coordinates to the list to plot their initial locations within the environment: 

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))


# Function to display the movement of agents as an animation:
    
carry_on = True
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
        
def update(frame_number):
   fig.clear()
   global carry_on #CHECK THIS
    

# Plot the agent locations:
    
   for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].vomit
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.imshow(environment)    
        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a		
        a = a + 1


# Animating the ABM within the environment, and displaying agent movements: 
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()  


# Creating a Graphical User Interface (GUI) to display the model:

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.show()
    
# Building the animation's main window to display the environment:
    
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


# Provide the GUI waiting time:

tkinter.mainloop()


# Writing the new environment output into a csv file and closing when finished:

f2= open ('environmentdataoutput.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = '')
for row in environment:
    writer.writerow(row)
f2.close
