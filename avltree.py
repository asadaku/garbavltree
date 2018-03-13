
# An augmented node class
class node:
    def __init__(self, key=None, subtreeSize=0, height=0, parent=None, rightNode=None, leftNode=None):
        self.key = key
        self.subtreeSize = subtreeSize
        self.height = height
        self.parent= parent
        self.right = rightNode
        self.left = leftNode
        
    def Insert(self, key):
        # Inserts a key inside a tree that is rooted at this node

        if( key == self.key ) :
            # No duplicates allowed in this tree
            return None
        if( key >= self.key ):
            # Increase subtree size of this node
            # Then inspect the right node
            self.subtreeSize += 1
            # Are we at a leaf?
            if( self.right == None ):
                # We are at a leaf
                # Insert the key here
                self.right = node(key, 1, 0, self)
                return self.right
            else:
                # We are not at a leaf. Keep going down the tree.
                return self.right.Insert(key)

        else:
            # Increase subtree size of this node
            # Then inspect the left node
            self.subtreeSize += 1;
            # Are we at a leaf?
            if( self.left == None ):
                # We are at a leaf
                self.left = node(key, 1, 0, self)
                return self.left
            else:
                # We are not at a leaf. Keep going down the tree.
                return self.left.Insert(key)

    def GetLeftRightHeight(self):

        if( self.left == None ):
            leftHeight = -1
        else:
            leftHeight = self.left.height

        if( self.right == None ):
            rightHeight = -1
        else:
            rightHeight = self.right.height

        return leftHeight, rightHeight

    def GetLeftRightSubtreeSize(self):

        if( self.left == None ):
            leftSize = 0
        else:
            leftSize = self.left.subtreeSize

        if( self.right == None ):
            rightSize = 0
        else:
            rightSize = self.right.subtreeSize

        return leftSize, rightSize

    
    def GetMin(self):
        # Gets the smallest element in the subtree rooted at this node
        if self.left is not None:
            return self.left.GetMin()
        else:
            return self

    def GetMax(self):
        # Gets the max element in the subtree rooted at this node
        if self.right is not None:
            return self.right.GetMax()
        else:
            return self

    def GetFirstRightParent(self):
        # If the node is in a right subtree, then returns the node that is the first
        # right parent encountered while walking up the tree
        if(self.parent.left):
            if(self.parent.left == self):
                # Current node is the left child. We have found the target node
                return self.parent
        else:
            if self.parent is not None:
                return self.parent.GetFirstRightParent()
            else:
                return None

    def GetFirstLeftParent(self):
        # If the node is in a left subtree, then returns the node that is the first
        # left parent encountered while walking up the tree
        if self.parent.right is not None:
            if(self.parent.right == self):
                # Current node is the left child. We have found the grandparent node
                return self.parent
        else:
            if self.parent is not None:
                return self.parent.GetFirstLeftParent()
            else:
                return None
    
        
    def GetSuccessor(self):
        """ Gets the successor of node
         Use the logic of in order traversal
         If asked for the successor of a node, consider the following picture
                      
                      grandparent
                       /
                    parent
                      |
                     node  
                    /    \
               left        right
              subtree     subtree

        The key of everthing in the left subtree is less than the key of the node
        The key of everything in the right subtree is greater than the key of the node
        If the node is a left child, the key of the parent is greater than the key of the node
        If the node has no right subtree, then it is the maximal element in left subtree of the 
        grandparent node, whose key is bigger than the node's key.
        The smallest key in the right subtree is the left most leaf

        So we end up with the following :

        1) If node has right subtree, the successor is the min of that (next item in in order traversal).
        2) else If the node is a left child, its successor is the parent (next item in in order traversal)
        3) else If the node has no right subtree and is not a left child, its successor is the grandparent
        Otherwise, there is no successor.

        
        """
        if self.right is None:
            if self.parent.left == self:
                return self.parent
            else:
                grandparentNode = self.GetFirstRightParent()
                if grandparentNode is None:
                    # There is no successor
                    return None
                else:
                    return grandparentNode
        else:
            return self.right.getMin()


    def GetPredecessor(self):
        """ Gets the predecessor of node
         Use the logic of in order traversal
         If asked for the successor of a node, consider the following picture
                      
              grandparent
                     \
                    parent
                      |
                     node  
                    /    \
               left        right
              subtree     subtree

        The key of everthing in the left subtree is less than the key of the node
        The key of everything in the right subtree is greater than the key of the node
        If the node is a left child, the key of the parent is greater than the key of the node
        If the node has no right subtree, then it is the maximal element in left subtree of the 
        grandparent node, whose key is bigger than the node's key.
        The smallest key in the right subtree is the left most leaf

        So we end up with the following :

        1) If node has left subtree, the predecessor is the max of that (previous item in in-order traversal).
        2) else If the node is a right child, its predecessor is the parent (previous item in in-order traversal)
        3) else If the node has no left subtree and is not a right child, its predecessor is the grandparent
        Otherwise, there is no predecessor.

        
        """
        if self.left is None:
            if self.parent.right == self:
                return self.parent
            else:
                grandparentNode = self.GetFirstLeftParent()
                if grandparentNode is None:
                    # There is no successor
                    return None
                else:
                    return grandparentNode
        else:
            return self.right.getMax()



    def InOrderRecursion(self, nodeList, startKey, endKey, debug):
        # Does in order recursion in the subtree rooted at this node

        if(self.left):
            self.left.InOrderRecursion(nodeList, startKey, endKey, debug)

        if(startKey is None or self.key >=startKey):
            if(endKey is None or self.key <= endKey):
                nodeList.append(self.key)    
                if(debug):    
                    print(self.key,end=', ')
                    print('stsize '+str(self.subtreeSize),end='   ')

        if(self.right):
            self.right.InOrderRecursion(nodeList, startKey, endKey, debug)


    def FindKey(self,key):
        # Find the key in the subtree rooted at this node
        if(self == None):
            return None
        
        if(self.key == key):
            return self
        else:
            if(key > self.key):
                if(self.right):
                    return self.right.FindKey(key)
                else:
                    return None
            else:
                if(self.left):
                    return self.left.FindKey(key)
                else:
                    return None
                    
    def NukeNode(self):
        # Assume this node has at most one child
        tempChild = None

        if self.left is not None:
            tempChild = self.left
        elif self.right is not None:
            tempChild = self.right
            
        if(tempChild is not None):
            tempChild.parent = self.parent

        if self.parent.left is self :
            self.parent.left = tempChild
        else:
            self.parent.right = tempChild

        self.parent.height = 0

    def GetNumElementsLessThanKey(self, key):
        numElements = 0
        
        if(self is None):
            return numElements
        
        if(self.key < key):
            numElements += 1 + [self.left.subtreeSize if self.left is not None else 0][0]
            if(self.right):
                numElements += self.right.GetNumElementsLessThanKey(key)
        else:
            if(self.left):
                numElements += self.left.GetNumElementsLessThanKey(key)

        return numElements

    def GetNumElementsGreaterThanKey(self, key):
        numElements = 0
        
        if(self is None):
            return numElements
        
        if(self.key > key):
            numElements += 1 + [self.right.subtreeSize if self.right is not None else 0][0]
            if(self.left):
                numElements += self.left.GetNumElementsGreaterThanKey(key)

        else:
            if(self.right):
                numElements += self.right.GetNumElementsGreaterThanKey(key)

        return numElements


            


            
class avltree:
    def __init__(self, root=None):
        self.root = None
        
    def Insert(self, key):
        # Inserts a key into the tree
        if self.root == None:
            # This tree isn't initialized, so initialize it
            self.root = node(key, 1, 0) 
            return self.root
        else:
            if(self.FindKey(key) is None):
                insertedNode = self.root.Insert(key)
            
                # Update tree heights
                if insertedNode is not None:
                    self.UpdateHeights(insertedNode)
                    self.BalanceTree(insertedNode)
            else:
                insertedNode = None

        return insertedNode

    def GetMin(self):
        # Gets the minimum element in the tree
        if self.root == None:
            # This tree isn't initialized
            return None
        else:
            return self.root.GetMin()

    def GetMax(self):
        # Gets the maximum element in the tree
        if self.root == None:
            # This tree isn't initialized
            return None
        else:
            return self.root.GetMax()

      
        
# Update heights as you go from the leaf up
# Assumes it is called with currentNode = one of the leaf nodes
# Walks up and fixes the heights of all parents
# For example, if a right node was added, go to the parent and
# compute left node vs right node height. If the parents current
# height is equal to the max of the two, then quit, otherwise update
# the parents height. Then move on to the next parent and so on.

    def UpdateHeights(self, currentNode):

        if currentNode.left is None and currentNode.right is None:
            currentNode = currentNode.parent

        leftHeight, rightHeight = currentNode.GetLeftRightHeight()

        if currentNode.height <= max(leftHeight, rightHeight) :
            currentNode.height += 1
            if currentNode == self.root:
                # We have reached the root node. We are done.
                return
            else:
                self.UpdateHeights(currentNode.parent)
        else:
            # The heights are already fixed. We are done
            return

    def UpdateSubtreeSize(self, currentNode):

        if currentNode.left is None and currentNode.right is None:
            currentNode = currentNode.parent

        leftSize, rightSize = currentNode.GetLeftRightSubtreeSize()

        currentNode.subtreeSize = 1+leftSize+rightSize
        
        if currentNode == self.root:
            # We just updated the root node. We are done.
            return
        else:
            self.UpdateSubtreeSize(currentNode.parent)



    def FindKey(self,key):
        # Finds the key if it exists in the tree.
        # Returns the node if it exists, otherwise None.
        node = self.root.FindKey(key)
        return node
            
        
    def DeleteKey(self,key):
        # Finds the key if it exists in the tree. Then deletes it.
        node = self.root.FindKey(key)

        if node is not None:
            if node.right is not None:
                maxNode = node.right.GetMin()
                node.key = maxNode.key
                tempNode = maxNode.parent
                maxNode.NukeNode()

            elif node.left is not None:
                minNode = node.left.GetMax()
                node.key = minNode.key
                tempNode = minNode.parent
                minNode.NukeNode()

            else:
                # This node has no subtree, so just nuke it
                tempNode = node.parent
                node.NukeNode()

            tempNode.subtreeSize -=1
            self.UpdateSubtreeSize(tempNode)
            self.UpdateHeights(tempNode)            
            self.BalanceTree(tempNode)                

            
        else:
            return None

        

    # A poorly implemented recursion that I find useful for debug purposes
    def ReturnTreeAsList(self, locations, currentNode = None):
        if currentNode is None:
            currentNode = self.root
        locations.append([currentNode.key, currentNode, currentNode.left.key if currentNode.left is not None else None,
                                                        currentNode.right.key if currentNode.right is not None else None])

        if currentNode.left:
            self.ReturnTreeAsList(locations, currentNode.left)
        if currentNode.right:
            self.ReturnTreeAsList(locations, currentNode.right)
            
        return locations

    def InOrderRecursion(self, startKey=None, endKey=None, debug=True):
        keyList = []
        currentNode = self.root
        currentNode.InOrderRecursion(keyList, startKey, endKey, debug)
        return keyList
    
    def GetNumElementsBetweenRange(self, minKey, maxKey):
        totalElements = self.root.subtreeSize

        elementsLessThanMinKey = self.root.GetNumElementsLessThanKey(minKey)
        
        elementsGreaterThanMinKey =  self.root.GetNumElementsGreaterThanKey(maxKey)

        return totalElements-elementsGreaterThanMinKey-elementsLessThanMinKey
    
    def BalanceTree(self, currentNode):


        while currentNode is not None:

            leftHeight, rightHeight = currentNode.GetLeftRightHeight()

            if(abs(rightHeight - leftHeight)>1):
                # This node is not balanced!!
                currentNode = self.CorrectUnbalancedNode(currentNode)

            currentNode = currentNode.parent

            
    def CorrectUnbalancedNode(self, currentNode):

        leftHeight, rightHeight = currentNode.GetLeftRightHeight()

        # The following rule applies
        if(rightHeight > leftHeight):
            # if right child is heavy
            lchildHeight, rchildHeight = currentNode.right.GetLeftRightHeight()
            if(rchildHeight > lchildHeight):
                # If the right child is right heavy or balanced
                # Do a left rotate of the root of the tree provided
                self.LeftRotate(currentNode)
            else:
                # Do a right rotation of the right child
                self.RightRotate(currentNode.right)
                # Followed by a left rotate of the root
                currentNode = self.LeftRotate(currentNode)
                
        else:
            # if left child is heavy
            lchildHeight, rchildHeight = currentNode.left.GetLeftRightHeight()
            if(lchildHeight > rchildHeight):
                # If the left child is left heavy or balanced
                # Do a right rotate of the root of the tree provided
                currentNode = self.RightRotate(currentNode)
            else:
                # Do a left rotation of the left child
                self.LeftRotate(currentNode.left)
                # Followed by a right rotate of the root
                currentNode = self.RightRotate(currentNode)
                
        return currentNode
            
                
    def RightRotate(self, currentNode):
        """ Performs a right rotation

            input is x
            st = subtree
        
                 p---              
                 |                      p---                 
                 x                      |                    
              /     \                   y                    
             /       \               /     \                 
            y        st             /       \                
          /   \      C    ===>     st        x       
         /     \                   A       /   \             
        st     st                         /     \            
        A       B                        st     st           
                                         B      C    

        
        The annoying part is handling the Nones

        """

        x        = currentNode
        y        = currentNode.left
        subtreeC = currentNode.right
        subtreeBSize = 0
        subtreeCSize = 0

        if y is not None:
            subtreeA = y.left
            subtreeB = y.right

        # Start swapping
        if(currentNode.parent is not None):
            if(currentNode.parent.left == currentNode):
                currentNode.parent.left = y 
            else:
                currentNode.parent.right = y

        y.parent = x.parent
        y.right = x
        y.left = subtreeA
        y.subtreeSize = x.subtreeSize

       
        x.parent = y
        x.left = subtreeB
        x.right = subtreeC
        x.height -= 2
        
        if(subtreeA is not None):
            subtreeA.parent = y
        if(subtreeB is not None):
            subtreeB.parent = x
            subtreeBSize = subtreeB.subtreeSize
        if(subtreeC is not None):
            subtreeC.parent = x
            subtreeCSize = subtreeC.subtreeSize

        x.subtreeSize = 1 + subtreeCSize + subtreeBSize
            
        if(x==self.root):
            self.root = y
            
        return y

    def LeftRotate(self, currentNode):
        """ Performs a left rotation
            input is x

            st = subtree
             p---                            p---
             |                               |
             x                               y
          /     \                         /     \ 
         /       \                       /       \
        st        y       ====>         x        st
        A       /   \                 /   \      C
               /     \               /     \
              st     st             st     st
              B       C             A       B

        
        The annoying part is handling the Nones

        """
        
        
        x        = currentNode
        y        = currentNode.right
        subtreeA = currentNode.left
        subtreeASize = 0
        subtreeBSize = 0

        
        if(y is not None):
            subtreeB = y.left
            subtreeC = y.right

        # Start swapping
        if(currentNode.parent is not None):
            if(currentNode.parent.left == currentNode):
                currentNode.parent.left = y 
            else:
                currentNode.parent.right = y

        y.parent = x.parent
        y.left = x
        y.right = subtreeC
        y.subtreeSize = x.subtreeSize
        
        x.parent = y
        x.left = subtreeA
        x.right = subtreeB
        x.height -= 2
        
        if(subtreeA is not None):
            subtreeA.parent = x
            subtreeASize = subtreeA.subtreeSize
        if(subtreeB is not None):
            subtreeB.parent = x
            subtreeBSize = subtreeB.subtreeSize
        if(subtreeC is not None):
            subtreeC.parent = y

        x.subtreeSize = 1 + subtreeASize + subtreeBSize
            
        if(x==self.root):
            self.root = y
            
        return y

        


