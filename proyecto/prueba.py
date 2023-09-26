import graphviz

# Crea un nuevo objeto Digraph (gráfico dirigido) de Graphviz
dot = graphviz.Digraph(comment='Árbol de Ejemplo')

# Agrega nodos al árbol
dot.node('A', 'Raíz')
dot.node('B', 'Nodo B')
dot.node('C', 'Nodo C')
dot.node('D', 'Nodo D')

# Agrega bordes entre nodos
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('B', 'D')

# Renderiza el árbol y abre una ventana emergente
dot.view()