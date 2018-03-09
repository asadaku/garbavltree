import sys
from avltree import avltree

def main():
    avltree()
    mainTree.Insert(10)
    mainTree.Insert(20)
    mainTree.Insert(30)
    mainTree.Insert(40)
#    mainTree.Insert(9)
#    mainTree.Insert(8)
#    mainTree.Insert(7)
#    mainTree.Insert(12)
#    mainTree.Insert(17)
#    mainTree.Insert(100)
    print("Tree Height: ", mainTree.height)
    print("Tree Subtree Size: ", mainTree.subtreeSize)

    locations = []
    locations = mainTree.DisplayTree(locations, 0, 0)
    print(locations)
    
    mainString=[]
    yaxis = 2
    xaxis = 1
    maxPrintWidth = 100
    pCenter = maxPrintWidth//2

    for loc in locations:
        if len(mainString)<(abs(loc[yaxis])+1):
            mainString.append(" "*maxPrintWidth)
        temp = mainString[abs(loc[yaxis])]
        temp = temp[:(pCenter+loc[xaxis]*10)]+ str(loc[0]) + temp[pCenter+loc[xaxis]*10:]
        mainString[abs(loc[yaxis])] = temp
        
    for elem in mainString:
        print(elem)
        
    
if __name__ == "__main__":
    main()
