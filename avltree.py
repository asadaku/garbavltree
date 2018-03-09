class avltree:
    def __init__(self, key=None, subtreeSize=0, height=0, predecessor=None, rightNode=None, leftNode=None):
        self.key = key
        self.subtreeSize = subtreeSize
        self.height = height
        self.predecessor = predecessor
        self.right = rightNode
        self.left = leftNode

    def Insert(self, key):
        if( self.key == None and self.predecessor == None):
            # This tree isn't initialized
            self.key = key
            self.subtreeSize += 1
            return
        else:
            # This tree is initialized
            # Perform BST Insertion
            glob = None
            if( key >= self.key ):
                # Go to the right node
                self.subtreeSize += 1
                # Are we at a leaf?
                if( self.right == None ):
                    # We are at a leaf
                    self.right = avltree(key, 0, 0, self)
                    self.UpdateHeights()
                    self.BalanceTree()
                    return self
                else:
                    # We are not at a leaf
                    self.right.Insert(key)

            else:
                # Go to the left node
                self.subtreeSize += 1;
                # Are we at a leaf?
                if( self.left == None ):
                    # We are at a leaf
                    self.left = avltree(key, 0, 0, self)
                    self.UpdateHeights()
                    self.BalanceTree()
                    return self
                else:
                    # We are not at a leaf
                    self.left.Insert(key)

        
        

    def UpdateHeights(self):
        if( self.left == None ):
            leftHeight = 0
        else:
            leftHeight = self.left.height

        if( self.right == None ):
            rightHeight = 0
        else:
            rightHeight = self.right.height

        if( self.height <= max(leftHeight, rightHeight) ):
            self.height += 1
            if(self.predecessor == None):
                return
            else:
                self.predecessor.UpdateHeights()
        else:
            # The heights are already fixed. We are done
            return

    def BalanceTree(self):

        leftHeight, rightHeight = self.GetLeftRightHeight()

        if(abs(rightHeight - leftHeight)<=1):
            # This node is balanced
            if(self.predecessor == None):
                # We have reached the root node
                return self
            else:
                self.predecessor.BalanceTree()
        else:
            # This node is not balanced!!
            locations = []
            print(self.DisplayTree(locations,0,0))
            updatedPointer = self.CorrectUnbalancedNode()
            print('After rotation')
            print(self.DisplayTree(locations,0,0))
            print('lulz?')
            
            updatedPointer.BalanceTree()
            

            
    def CorrectUnbalancedNode(self):
        # The following general rule applies
        leftHeight, rightHeight = self.GetLeftRightHeight()

        if(rightHeight > leftHeight):
            # if right child is heavy
            lchildHeight, rchildHeight = self.right.GetLeftRightHeight()
            if(rchildHeight > lchildHeight):
                # If the right child is right heavy or balanced
                # Do a left rotate of the root of the tree provided
                self.LeftRotate()
            else:
                # Do a right rotation of the right child
                self.right.RightRotate()
                # Followed by a left rotate of the root
                self.LeftRotate()
                
        else:
            # if left child is heavy
            lchildHeight, rchildHeight = self.left.GetLeftRightHeight()
            if(lchildHeight > rchildHeight):
                # If the left child is left heavy or balanced
                # Do a right rotate of the root of the tree provided
                self.RightRotate()
            else:
                # Do a right rotation of the left child
                self.right.LeftRotate()
                # Followed by a right rotate of the root
                self.RightRotate()
                
        return self.predecessor
            
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
                
    def RightRotate(self):
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
        
        x        = self
        y        = self.right
        subtreeA = self.left

        if(y is not None):
            subtreeB = y.left
            subtreeC = y.right

        # Start swapping
        if(self.predecessor is not None):
            if(self.predecessor.left == self):
                self.predecessor.left = y 
            else:
                self.predecessor.right = y

        y.predecessor = x.predecessor
        y.right = x
        y.left = subtreeA
        
        x.predecessor = y
        x.left = subtreeB
        x.right = subtreeC
        x.height -= 2
        
        if(subtreeA is not None):
            subtreeA.predecessor = y
        if(subtreeB is not None):
            subtreeB.predecessor = x
        if(subtreeC is not None):
            subtreeC.predecessor = x

    def LeftRotate(self):
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
        
        x        = self
        y        = self.right
        subtreeA = self.left

        if(y is not None):
            subtreeB = y.left
            subtreeC = y.right

        # Start swapping
        if(self.predecessor is not None):
            if(self.predecessor.left == self):
                self.predecessor.left = y 
            else:
                self.predecessor.right = y

        import pudb;pu.db
        y.predecessor = x.predecessor
        y.left = x
        y.right = subtreeC

        x.predecessor = y
        x.left = subtreeA
        x.right = subtreeB
        x.height -= 2
        
        if(subtreeA is not None):
            subtreeA.predecessor = x
        if(subtreeB is not None):
            subtreeB.predecessor = x
        if(subtreeC is not None):
            subtreeC.predecessor = y

        
        
    def DisplayTree(self, locations, xAxis, yAxis):
        locations.append([self.key, xAxis, yAxis])

        if(self.left):
            self.left.DisplayTree(locations, xAxis-1, yAxis-1)
        if(self.right):
            self.right.DisplayTree(locations, xAxis+1, yAxis-1)

            
        return locations

