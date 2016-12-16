import networkx as nx
import graphspace_utils

from operator import itemgetter
import matplotlib.pyplot as plt
import math
G = nx.read_gml("mw_thesisgraph.gml",) #this reads Michael's graph into a useable networkx format


d = {}
for node in G.nodes():
  for attr in G.nodes(node):
    d[str(attr[0])] = attr[1]
print(G.nodes())

#these plots were used to produce scatterplots of the baseline centrality measures

close = nx.closeness_centrality(G,u=None,distance=None,normalized=True)
close_node = []
close_val = []
close_label = []
degree = nx.degree_centrality(G)
degree_node = []
degree_val = []
degree_label = []
between = nx.betweenness_centrality(G,k=None,normalized=True,weight=None,endpoints=False,seed=None)
between_node = []
between_val = []
between_label = []


i = 1
for key in close:
  close_node.append(i)
  close_label.append(str(key))
  close_val.append(close[key])
  i += 1
i = 1
for key in degree:
  degree_node.append(i)
  degree_label.append(str(key))
  degree_val.append(degree[key])
  i += 1
i = 1
for key in between:
  between_label.append(str(key))
  between_node.append(i)
  between_val.append(between[key])
  i += 1
i = 1




def plot(prefix,x,y,labels):
  fig = plt.figure(figsize=(6.5,4))
  plt.plot(x,y,'o')
  plt.xticks(x, labels, rotation='vertical')
  plt.ylabel(prefix)
  plt.title(prefix)
  plt.subplots_adjust(bottom=0.15)

  plt.tight_layout()

  plt.savefig(prefix+'.png')
  print "Wrote to "+prefix+".png"
  return 
  
#plot("In Degreee centrality",in_deg_node,in_deg_val,in_deg_label)

def centrality(G): #input: a networkx graph G
                   #output:
  degree = nx.degree_centrality(G)
  
  
  close = nx.closeness_centrality(G,u=None,distance=None,normalized=True)
  between = nx.betweenness_centrality(G,k=None,normalized=True,weight=None,endpoints=False,seed=None)
  
  return [degree,close,between]


def NodeRemoval(G): #input: a networkx graph G
                    #output: a list of dictionaries for three centrality measures of each graph that has been created through removing indiv. nodes
  listCent = {}
  for n in G.nodes(): #iterate through each node in the graph
    removedEdge = []
    G.remove_node(n) #remove node of interest
    for edge in G.edges():
      if node in edge:
        removedEdge.append(edge)
        G.remove_edge(edge[0],edge[1]) #remove edges with the node of interest
    listCent[n] = centrality(G) #computes centrality measures with node removed, adds to a dictionary
    G.add_node(n) #add node back to Graph
    for edge in removedEdge:
      G.add_edge(edge[0],edge[1]) #add removed edges back to graph

  for key in listCent:
    print key,listCent[key]
    print
    print
  return listCent #return dictionary 
y = centrality(G)
x = NodeRemoval(G)

def Comparison(G_Cent,ind_cent,per): #input: baseline centrality measures for a graph, centrality measures for each version of the graph with a node removed, list of baseline centrality measures means
                                 #output: a list of nodes in order of the change that it's removal caused
  
  full_ls = []
  for key in ind_cent:
    for item in range(3):
      change = {}
      x = ind_cent[key][item] 

      for key1 in x:
        change[key1] = abs(x[key1]-G_Cent[item][key1]) #finds absolute value of centrality measure's change

      mean = 0   
      for k in change:
        mean += change[k]
      mean =  mean/int(len(change)) #finds the mean amount each value changed

      if item == 0:
        full_ls.append([key,"degree",change,mean])
      if item == 1:
        full_ls.append([key,"close",change,mean])
      if item == 2:
        full_ls.append([key,"between",change,mean])
       
  for item in full_ls:
    if item[1] == "degree":
      item[3] = (item[3]-per[0]/per[0]) * 100 #percent change formula 
    if item[1] == "close":
      item[3] = (item[3]-per[1]/per[1]) * 100
    if item[1] == "between":
      item[3] = (item[3]-per[2]/per[2]) * 100

  full_ls = sorted(full_ls, key=itemgetter(3)) #sorts items from smallest mean change to biggest
  for item in full_ls:
    print item
    print 
    print


  return 


#this function was added to compute the mean of each baseline centrality measure
#input: a list of dictonaries with centrality measures as values and nodes as keys
#output: a list of each dictionary's mean
def baselineCal(lst):
  ls = []
  for item in lst: 
    t = 0
    for key in item:
      t += item[key]
    ls.append(t/(int(len(item))))
  return ls









