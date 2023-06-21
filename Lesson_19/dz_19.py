import networkx as nx
import matplotlib.pyplot as plt

cities_list = []
with open ('cities.csv') as file:
    for i in file.readlines():
        obj = i.replace('\n', '').split(';')
        obj[2] = int(obj[2])
        cities_list.append(obj)


g = nx.Graph()
for cities in cities_list:
    g.add_edge(cities[0], cities[1], weight= cities[2])

position = nx.spring_layout(g)
nx.draw_networkx(g, position)
plt.title('Міста України')
plt.show()

print(nx.shortest_path(g, 'Lebedyn', 'Bilhorod-Dnistrovskyi', weight='weight'))
print(nx.shortest_path_length(g, 'Lebedyn', 'Bilhorod-Dnistrovskyi', weight='weight'))

print(nx.shortest_path(g, 'Reni', 'Korsun-Shevchenkivskyi', weight= 'weight'))
print(nx.shortest_path_length(g, 'Reni', 'Korsun-Shevchenkivskyi', weight= 'weight'))

