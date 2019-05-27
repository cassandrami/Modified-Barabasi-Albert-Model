

# The changes I made to the BA model were:

# - neglecting the (1/total degree) coeffecient. I used the individual degrees of the nodes as the probablities ( > 0) instead of dividing by the total for each since this is trivial difference doesn't proportionally matter.
# - reversing the probability for attachment. A new node is more likely to attach to a less connected node than a more directed node in my model.

# The differences between my B-A and the original are small. Nodes tend to attach in the same way and pattern, just to different nodes. The graph tends to be pretty evenly distributed with respect to degree,
# since nodes prefer to attach to nodes of lower degree. There aren't nearly as many outliers. Local clustering coefficient tends to be comparatively low, as does shortest path length.




import networkx as nx
import numpy as np


def barabasi_albert_modified(n, m):

    # (1) initialize
    G = nx.Graph()


    # generate m many nodes in the graph
    for i in range(m):
        G.add_node(i)

    nodelist = nx.nodes(G)

    # make the graph fully connected
    # for every node, if another node is not itself, make an edge
    for i in range(len(nodelist)):
        for j in range(len(nodelist)):
            if ( i != j ):
                G.add_edge(i, j)

    # while N < n
    while (len(G.nodes()) < n):

        # (2) growth
        G.add_node(len(G.nodes()))

        # (3) preferential attachment

        # make a list of the degree for each node
        degrees = []
        for i in G.nodes():
            degrees.append(G.degree[i])

        # MODIFICATION - subtract the degree from the total graph degree to
        # reverse the probabilities & attachment

        # sum the degrees of the graph, divide by 2 for double counted edges
        total = sum(degrees) / 2

        for i in range(len(degrees) - 1):
            degrees[i] = total - degrees[i]

        # END MODIFICATION

        # choose m many nodes from the list of nodes, with probability <degree>
        # to attach to
        attachto = np.random.choice(range(len(G.nodes()) - 1), m, degrees[:-1])
        for choice in attachto:
            G.add_edge(len(G.nodes) - 1, choice)


    # draw & return

    #print(G.nodes())
    #print(G.edges())

    nx.draw(G, with_labels = True)
    return G

# barabasi_albert_modified(10, 3)
