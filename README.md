# 3D Surface Pathfinding Problem

A surface is given as input, with its points specified by `(x, y, z)` coordinates. An intelligent agent walks on the surface such that it can move from any point to a neighboring point, provided that point does not contain an obstacle. Two points are considered neighbors if their `x` and/or `y` coordinates differ by 1.

We want the agent to reach the goal point **G** from the starting point **S** by taking the most optimal path possible.

## The 3D Surface and the Obstacles

The path between the two endpoints can be optimal according to several different criteria, and these optimal paths do not necessarily coincide with each other. Some optimization criteria include:

- **By number of steps** – the agent's path should have the minimal number of steps;
- **By distance** – the total length of the path taken by the agent should be minimal (e.g., using Euclidean distance);
- **By required energy** – note that the energy required to move between two points correlates with the distance between the two points (the longer the path, the more energy it requires), but moving downhill is easier (requires less energy) than moving uphill.# 3D Surface Pathfinding Problem

A surface is given as input, with its points specified by `(x, y, z)` coordinates. An intelligent agent walks on the surface such that it can move from any point to a neighboring point, provided that point does not contain an obstacle. Two points are considered neighbors if their `x` and/or `y` coordinates differ by 1.

We want the agent to reach the goal point **G** from the starting point **S** by taking the most optimal path possible.

## The 3D Surface and the Obstacles

The path between the two endpoints can be optimal according to several different criteria, and these optimal paths do not necessarily coincide with each other. Some optimization criteria include:

- **By number of steps** – the agent's path should have the minimal number of steps;
- **By distance** – the total length of the path taken by the agent should be minimal (e.g., using Euclidean distance);
- **By required energy** – note that the energy required to move between two points correlates with the distance between the two points (the longer the path, the more energy it requires), but moving downhill is easier (requires less energy) than moving uphill.