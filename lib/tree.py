class Tree:
    # the constructor initialises the tree with a root node
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def dfs(node):  # The dfs function is defined inside get_element_by_id to perform a recursive depth-first search starting from the given node
            if node is None:
                return None
            if node.get('id') == id: #If the current node's id matches the target id, return the current node.
                return node
            
            #Iterate through the node's children (if any) and recursively call dfs on each child. If a match is found (result is not None), return the result.
            for child in node.get('children', []):
                result = dfs(child)
                if result is not None:
                    return result
            return None  #If no match is found in the current node or any of its children, return None

        return dfs(self.root) #The get_element_by_id method starts the search from the root node and uses the dfs function to look for the node with the specified id.

    
    
 
    


    

    
