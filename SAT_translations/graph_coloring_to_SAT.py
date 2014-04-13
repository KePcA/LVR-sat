#coding:utf-8

"""
Translation of graph coloring problem to SAT problem
"""
import bool_formulas as bf


def graph_coloring(G, b):
    """
    INPUT: Graph G given as list of connections between nodes - example: [(a,b) (a,c) (b,d) (d,e)]
            and b - number of colors
    OUTPUT: logic formula which translates problem onto SAT
    """

    colors = range(1,b+1)
    nodes = list(set([u for (u, v) in G] + [v for (u, v) in G]))

    #Each node has to have at least color
    at_least_one_color = bf.And([])
    for node in nodes:
        node_at_least_one_color = bf.Or([])
        for color in colors:
            node_is_color = bf.Var(node+str(color))
            node_at_least_one_color.formulas.append(node_is_color)
        at_least_one_color.formulas.append(node_at_least_one_color)

    #Each node must not be colored twice
    not_twice = bf.And([])
    for i in range(len(colors)):
        for j in range(i):
            color_pair = (colors[j], colors[i])
            each_node_not_both_colors = bf.And([])
            for node in nodes:
                node_not_both_colors = bf.Not(bf.And([bf.Var(node+str(colors[j])), bf.Var(node+str(colors[i]))]))
                each_node_not_both_colors.formulas.append(node_not_both_colors)
            not_twice.formulas.append(each_node_not_both_colors)

    #Connected nodes must not be same color
    connected_not_same_color = bf.And([])
    for (node1, node2) in G:
        for color in colors:
            nodes_not_same_color = bf.Not(bf.And([bf.Var(node1+str(color)), bf.Var(node2+str(color))]))
            connected_not_same_color.formulas.append(nodes_not_same_color)

    return bf.And([at_least_one_color, not_twice, connected_not_same_color])


G = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('d', 'e'),
    ('e', 'a')
]
b = 2
print graph_coloring(G, b)



