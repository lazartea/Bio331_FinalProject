# Bio331_FinalProject
This project ranks the importance of each individual node in an undirected, unconnected social network. The data that was used was from Michael Weiss' 2016 Reed senior thesis, "Non-Kinship Social Bonds in Resident Killer Whales (Orcinus Orca)." This exact code cannot be used without that data, but another gml file containing a social network could be substituted.

In order to run the code, the Comparison function should be called with the results of the NodeRemoval and Centrality functions (both of which take a network as input). The order of nodes will then be printed to the terminal, and each node will list the name of the centrality measure that was used, the dictionary containing the new centrality measures, and the average amount that each measure changed when compared to the corresponding baseline measure.

## Files
- `whale_data.py` This file contains the bulk of the programing done for this project. First, it processes the .gml data into a networkx graph. Then, it runs three centrality measures on each node (which represents a whale pod) of the graph. Then it removes one node at a time, calculates the change in each centrality measures, and sorts the nodes by the mean change their removal produces. 
