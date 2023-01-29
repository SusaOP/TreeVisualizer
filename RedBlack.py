from graphviz import Digraph

class RedBlackTree:

    def __init__(self):
        self.graph = Digraph()
        self.root = -1
        self.size = 0

    def reload(self):
        # Render graph again after all changes are made
        self.graph.render("Red-Black Tree", view=True)

    #given a node, (e.g. "A -> B"), return parent ("A") and child ("B")
    def __get__parent_child(self,node):
        parent = node.split("->")[0].replace("\t","").replace(" ","").replace("\n","")
        child = node.split("->")[1].replace("\t","").replace(" ","").replace("\n","")
        return parent,child
    
    # Insert targetNode appropriately into tree
    def insertNode(self,targetNode):
        print(f'Inserting node {targetNode}')

        self.graph.node(targetNode)

        self.reload()

    # Delete targetNode from the tree and rebalance
    def deleteNode(self,targetNode):
        # needs to better handle lost edges
        parent
        children = []
        # iterate through the existing graph
        for node in self.graph.body:
            # find the node/edges to be deleted
            if targetNode in node:
                #handle edge and save connections
                if "->" in node:
                    par,chi=self.__get__parent_child(node)
                    if (par == targetNode):
                        # parent is desired to be removed
                        children.append(chi)

                    elif (chi == targetNode):
                        # child is desired to be removed
                        parent = par

                self.graph.body.remove(node)
        
        self.reload()

    # Find targetNode in the tree
    def findNode(self,targetNode):

        self.reload()




    # More methods here for handling rebalancing/rules

