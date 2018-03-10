import sys
from avltree import avltree
from graphviz import Digraph
import time

def main():
    mainTree = avltree()
    mainTree.Insert(10)
    mainTree.Insert(20)
    mainTree.Insert(30)
    mainTree.Insert(40)
    mainTree.Insert(18)
    mainTree.Insert(19)
    mainTree.Insert(20)
    mainTree.Insert(9)
    mainTree.Insert(8)
    leftMost = mainTree.Insert(7)
    mainTree.Insert(12)
    node17 = mainTree.Insert(17)
    node35 = mainTree.Insert(35)
    mainTree.Insert(100)

    showMeTheTree(mainTree, 'origTree')
    time.sleep(2)
    
    print("The height of the root node is {}".format(mainTree.root.height))
    print("The subtree size of the root node is {}".format(mainTree.root.subtreeSize))
    print("The smallest key in the tree is {}".format(mainTree.GetMin().key))
    print("The biggest key in the tree is {}".format(mainTree.GetMax().key))
    print("The successor of {} is {}".format(node17.key, node17.GetSuccessor().key))
    print("The predecessor of {} is {}".format(node17.key, node17.GetPredecessor().key))

    print("The successor of {} is {}".format(leftMost.key, leftMost.GetSuccessor().key))
    print("The predecessor of {} is {}".format(leftMost.key, leftMost.GetPredecessor().key if leftMost.GetPredecessor() is not None else "NA" ))

    mainTree.InOrderRecursion()

    if(mainTree.FindKey(20) is not None):
        print("Found Key 20!")
    else:
        print("Did not find key 20.")

    if(mainTree.FindKey(33) is not None):
        print("Found Key 33!")
    else:
        print("Did not find key 33.")
    
    mainTree.DeleteKey(18)
    showMeTheTree(mainTree, 'deletedNode')


def showMeTheTree(mainTree, filename):
    locations = mainTree.ReturnTreeAsList([])
    dot = Digraph(comment='My Tree')
    
    for elem in locations:
        dot.node('key'+str(elem[0]), str(elem[0]))

    spuriousNodeCount=1    
    for elem in locations:
        if elem[2] is not None:
            dot.edge('key'+str(elem[0]), 'key'+str(elem[2]))
        if elem[3] is not None:
            dot.edge('key'+str(elem[0]), 'key'+str(elem[3]))



    dot.render(filename)
    

        
if __name__ == "__main__":
    main()
