import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


ukrainian_personalities = ["Тарас Шевченко", "Леся Українка", "Іван Франко", "Михайло Грушевський", "Олександр Довженко"]
G.add_nodes_from(ukrainian_personalities)


G.add_edges_from([
    ("Тарас Шевченко", "Леся Українка"),
    ("Тарас Шевченко", "Іван Франко"),
    ("Тарас Шевченко", "Михайло Грушевський"),
    ("Леся Українка", "Іван Франко"),
    ("Леся Українка", "Михайло Грушевський"),
    ("Іван Франко", "Михайло Грушевський"),
    ("Іван Франко", "Олександр Довженко"),
    ("Михайло Грушевський", "Олександр Довженко")
])

# Візуалізація графа
nx.draw(G, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_color="black", font_weight="bold")
plt.title("Мережа Instagram з відомими українськими особистостями")
plt.show()

# Аналіз основних характеристик
print("Кількість особистостей (вершин):", G.number_of_nodes())
print("Кількість зв'язків (ребер):", G.number_of_edges())
print("Ступінь вершин:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
