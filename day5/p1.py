with open("input", "r") as file:
    text = [text.strip('\n') for text in file.readlines()]
    ordering_rules = [text.split('|') for text in text[:text.index('')]]
    updates = [text.split(',') for text in text[text.index(
        '') + 1:]]  # No need to turn string numbers in to ints, they will be just used as symbols

print(ordering_rules)
print(updates)


class Node:
    def __init__(self, name):
        self.name = name
        self.directed_nodes = []

    def addNode(self, node: 'Node'):
        self.directed_nodes.append(node)

    def getDirectedNodes(self):
        return self.directed_nodes


class Graph:
    def __init__(self, ordering_rules: list):
        self.nodes = []
        for node, node2 in ordering_rules:
            self.defineNode(node)
            self.defineNode(node2)

        for tuple in ordering_rules:
            self.addNodetoNode(tuple)

        # self.printNodeNames()

    def defineNode(self, name: str):
        if self.getNode(name) == None:
            self.nodes.append(Node(name))

    def printNodeNames(self):
        # print("Nodes size: "+ str(len(self.nodes)))
        for node in self.nodes:
            print(node.name)

    def getNode(self, name: str):
        for node in self.nodes:
            if node.name == name:
                # print("Node was found!  " + name)
                return node
        # print("Node wasnt found! " + name)

    def isNodeAfterNode(self, node1_name: str, node2_name: str):
        # node1,node2 = self.getNode(node1_name),self.getNode(node2_name)
        startNode = self.getNode(node1_name)
        targetNode = self.getNode(node2_name)

        cur_directed_nodes = startNode.getDirectedNodes()

        if targetNode in cur_directed_nodes:
            return True

        if cur_directed_nodes == None:
            return False

        return any([self.isNodeAfterNode(node.name, node2_name) for node in cur_directed_nodes])

    def checkIfUpdateValid(self, order:list):
        currentRoaster = []
        for curLetter in order:
            # print("asd")
            # node = self.getNode(curLetter)
            for currentRoasterLetter in currentRoaster:
                # print("asd")
                if self.isNodeAfterNode(curLetter, currentRoasterLetter):
                    # print("dsa")
                    return False
            currentRoaster.append(curLetter)
        return True

    def addNodetoNode(self, tuple: tuple):
        self.getNode(tuple[0]).addNode(self.getNode(tuple[1]))


if __name__ == "__main__":
    graph = Graph(ordering_rules)

    sum = 0
    for update in updates:

        if graph.checkIfUpdateValid(update):
            print(update)
            sum += int(update[int(len(update)/2)]) # Lol great line

    print(int(sum))