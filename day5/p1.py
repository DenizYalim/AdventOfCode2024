with open("input", "r") as file:
    text = [text.strip('\n') for text in file.readlines()]
    ordering_rules = [text.split('|') for text in text[:text.index('')]]
    updates = [text.split(',') for text in text[text.index(
        '') + 1:]]  # No need to turn string numbers in to ints, they will be just used as symbols


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.afters = []

    def addAfter(self, after):
        self.afters.append(after)

    def printAfters(self):
        for after in self.afters:
            print(after, end=' ')

    def getAfters(self):
        return self.afters


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, node):
        if node in self.nodes:
            return
        self.nodes[node] = Node(node)

    def addAfterToNode(self, node, after):
        if node in self.nodes:
            self.nodes[node].addAfter(after)

    def checkAfterIsAnyNodesAfter(self, after):
        for node in self.nodes:
            afters = self.nodes[node].getAfters()
            if after in afters:
                print(after, end= '  ')
                return True
            return False

    def printNodes(self):
        for key in self.nodes:
            print(key, end=' -> ')
            self.nodes[key].printAfters()
            print()


def findWrongOrders(graph):
    """
    for node, after in ordering_rules:  # Turn ordering list in to topological sort
        graph.addNode(node)
        graph.addAfterToNode(node, after)
    """

    correctOrders = []
    for update in updates:
        newGraph = Graph()
        visited = []
        correct_update = True
        for symbol in update:
            visited.append(symbol)
            correct_update = not newGraph.checkAfterIsAnyNodesAfter(symbol)
            newGraph.addNode(symbol)
        if correct_update:
            correctOrders.append(update)
        # print(visited)

    print(correctOrders)


graph = Graph()
findWrongOrders(graph)
