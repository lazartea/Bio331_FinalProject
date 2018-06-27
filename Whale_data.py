import networkx as nx
import graphspace_utils
from operator import itemgetter
import matplotlib.pyplot as plt
import math

#this reads Michael's graph into a useable networkx format
#Graph = nx.read_gml("mw_thesisgraph.gml",) 

def createAttrDictionary(Graph):
  attr_dictionary = {}
  for node in Graph.nodes():
    for attr in Graph.nodes(node):
      attr_dictionary[str(attr[0])] = attr[1]
  print(G.nodes())
  return attr_dictionary

def initClosenessCetrality(closenessCentrality):
  close_node,close_val,close_label = ([] for i in range(3))
  
  num = 1
  for key in closenessCentrality:
    close_node.append(num)
    close_label.append(str(key))
    close_val.append(close[key])
    num +=1

  return [close_node,close_label,close_val]

def initDegreeCentrality(degreeCentrality):
  degree_node,degree_val,degree_label = ([] for i in range(3))

  num = 1
  for key in degreeCentrality:
    degree_node.append(degree_num)
    degree_label.append(str(key))
    degree_val.append(degree[key])
    num += 1

  return [degree_node,degree_label,degree_val]

def initBetweenessCentrality(betweennessCentrality):
  between_node,between_val,between_label = ([] for i in range(3))

  num = 1
  for key in betweennessCentrality:
    between_node.append(num)  
    between_label.append(str(key))
    between_val.append(between[key])
    num += 1
  return [between_node,between_label,between_val]

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

def centrality(G):
  close = nx.closeness_centrality(G,u=None,distance=None,normalized=True)
  degree = nx.degree_centrality(G)
  between = nx.betweenness_centrality(G,k=None,normalized=True,weight=None,endpoints=False,seed=None)

  return [closenessCentrality,degreeCentrality,betweennessCentrality]

#input: a networkx graph, G
#output: a list of dictionaries for three centrality measures of each graph that
#has been created through removing individual nodes
def NodeRemoval(Graph): 
  centralityDictionaries = {}
  for node in Graph.nodes():
    removedEdge = []
    Graph.remove_node(node)
    for edge in Graph.edges():
      if node in edge:
        removedEdge.append(edge)
        Graph.remove_edge(edge[0],edge[1])
    centralityDictionaries[node] = centrality(Graph)
    Graph.add_node(node)
    for edge in removedEdge:
      Graph.add_edge(edge[0],edge[1])

  for key in centralityDictionaries:
    print key,centralityDictionaries[key] + "\n \n"
  return centralityDictionaries
  
#input: baseline centrality measures for a graph, centrality measures for each version
# of the graph with a node removed, list of baseline centrality measures means
#output: a list of nodes in order of the change that it's removal caused
def Comparison(graphCentrality,individualCentrality,baseline):  
  influentialNodeList = []
  for key in individualCentrality:
    for measure in range(3):
      change = {}
      indiv = individualCentrality[key][measure] 

      for index in indiv:
        change[index] = abs(x[index]-G_Cent[measure][index]) #finds absolute value of centrality measure's change

      mean = 0   
      for index in change:
        mean += change[index]
      mean =  mean/int(len(change)) #finds the mean amount each value changed

      if measure == 0:
        full_ls.append([key,"degree",change,mean])
      elif measure == 1:
        full_ls.append([key,"close",change,mean])
      elif measure == 2:
        full_ls.append([key,"between",change,mean])
       
  for measure in influentialNodeList:
    if measure[1] == "degree":
      measure[3] = (measure[3]-baseline[0]/baseline[0]) * 100 #percent change formula 
    elif measure[1] == "close":
      measure[3] = (measure[3]-baseline[1]/baseline[1]) * 100
    elif measure[1] == "between":
      measure[3] = (measure[3]-baseline[2]/baseline[2]) * 100

  influentialNodeList = sorted(influentialNodeList, key=itemgetter(3)) #sorts items from smallest mean change to biggest
  for node in influentialNodeList:
    print node + "\n \n"

  return

#this function was added to compute the mean of each baseline centrality measure
#input: a list of dictonaries with centrality measures as values and nodes as keys
#output: a list of each dictionary's mean
def baselineCal(centralityMeasures):
  baselines = []
  for measure in centralityMeasures: 
    sum = 0
    for key in measure:
      sum += measure[key]
    baseline.append(sum/(int(len(measure))))
  return baseline
