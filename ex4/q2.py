import networkx as nx
from numpy import random
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, sharex=True, sharey=True, constrained_layout=True)

for i, p in enumerate([0.2, 0.4, 0.5, 0.6, 0.8]):
    x = []
    y = []
    j = 0
    n_arr = sorted(random.randint(2, 500, 6))
    while j < 6:
        n = n_arr[j]
        print(n, p)
        G = nx.gnp_random_graph(n, p)
        try:
            diam = nx.diameter(G)
            appr_diam = nx.approximation.diameter(G)
            ratio = diam / appr_diam
            x.append(n)
            y.append(ratio)
            print(f"diameter: {diam}, diameter approximation: {appr_diam}")
            j += 1
        except:
            continue
        print(x, y)
        row = 0 if i < 3 else 1
        col = i % 3
        axes[row, col].plot(x, y,marker='o', linestyle='-', color='r',)
        axes[row, col].set_title(f"p: {p}")
plt.xticks(x)
fig.supxlabel('n')
fig.supylabel('ratio')
plt.show()
