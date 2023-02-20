# Graph Theory Assignments

This repository contains my solutions for the Graph Theory Assignments course at [Federal Institute of Education, Science and Technology of Paraíba](https://www.ifpb.edu.br/en) The course covers various topics in graph theory, including graph representations and graph algorithms. 


## Table of Contents
- Getting Started
- Graph Representations
- Graph Algorithms


## Getting Started
To get started with this repository, simply clone it to your local machine:

~~~shell
$ git clone https://github.com/rafaelfigueredog/GraphTheoryAssignments
~~~

## Graph Representations

### Dictionary and Adjacency List
In Python, you can represent a graph using a dictionary where the keys represent the vertices and the values represent the adjacency list of each vertex. The adjacency list is a list of adjacent vertices for a given vertex. 

### Adjacency matrix

In Python, an adjacency matrix for an undirected graph can be represented as a 2D matrix, where the element at the i-th row and j-th column represents the edge weight between the i-th and j-th vertices. If there is no edge between vertices i and j, the element at the i-th row and j-th column is set to 0.

## Graph Algorithms

### Eulerian path

An Euler path, also known as Eulerian path, is a path in a graph that passes through every edge exactly once. A graph that has an Euler path is called Eulerian. A special case of an Euler path is an Euler circuit, which is a closed path that passes through every edge exactly once.

### Warshall Algoritm 

The Warshall algorithm is an algorithm used to find the transitive closure of a directed graph. The transitive closure of a directed graph is a graph in which there is an edge from vertex i to vertex j if and only if there is a directed path from vertex i to vertex j.

 ### Dijkstra's algorithm 
 
Dijkstra's algorithm is a popular algorithm for finding the shortest path between nodes in a graph. Given a weighted graph and a source node, it can find the shortest path to all other nodes in the graph.

 ### Kruskall Algoritm 
 
Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree of an undirected, weighted graph. It works by sorting the edges of the graph by weight and then adding them to the minimum spanning tree in ascending order of weight.

## Conclusion
This repository contains my solutions for the Graph Theory Assignments course at IFPB. I hope you find these programs useful and informative, and I welcome any feedback or suggestions for improvement. If you have any questions or comments, please feel free to reach out me.
