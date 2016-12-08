# Bio331_FinalProject
Final Project for Bio331

## Files
- `whale_data.py` This file contains the bulk of the programing done for this project. First, it processes the .gml data into a networkx graph. Then, it runs three centrality measures on each node (which represents a whale pod) of the graph. Then it removes one node at a time, calculates the change in each centrality measures, and sorts the nodes by the mean change their removal produces. 
