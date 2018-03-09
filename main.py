import sys
from avltree import avltree

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
    locations = []
    locations = mainTree.ReturnTreeAsList(locations, 0, 0)
    print(locations)
    
    mainString=[]
    yaxis = 2
    xaxis = 1
    maxPrintWidth = 100
    pCenter = maxPrintWidth//2

    for idx, loc in enumerate(locations):
        if len(mainString)<(abs(loc[yaxis])+1):
            mainString.append(" "*maxPrintWidth)
        temp = mainString[abs(loc[yaxis])]
        temp = temp[:(pCenter+loc[xaxis]*10)]+ str(loc[0]) + temp[pCenter+loc[xaxis]*10:]
        mainString[abs(loc[yaxis])] = temp
        
    for elem in mainString:
        print(elem)

    print("The height of the root node is {}".format(mainTree.root.height))
    print("The subtree size of the root node is {}".format(mainTree.root.subtreeSize))
    print("The smallest key in the tree is {}".format(mainTree.GetMin().key))
    print("The biggest key in the tree is {}".format(mainTree.GetMax().key))
    print("The successor of {} is {}".format(node17.key, node17.GetSuccessor().key))
    print("The predecessor of {} is {}".format(node17.key, node17.GetPredecessor().key))

    print("The successor of {} is {}".format(leftMost.key, leftMost.GetSuccessor().key))
    print("The predecessor of {} is {}".format(leftMost.key, leftMost.GetPredecessor().key if leftMost.GetPredecessor() is not None else "NA" ))
        
    
if __name__ == "__main__":
    main()
