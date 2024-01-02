package RedBlack;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class RedBlackTree {

    /**
     * Root Node.
     */
    private Node root;

    /**
     * Constructor.
     */
    public RedBlackTree() {
        root = null;
    }

    /**
     * External insert method
     * @param data - Data to insert
     * @throws Exception - Duplicate data
     */
    public void insert(int data) throws Exception {
        if(root == null) {
            //Tree is empty. Create a new root node.
            root = new Node(data, null);
            root.setColor(1);
        }
        else {
            //Call the class's private insert function
            Node t = insert(root, data);
            //Re-balance the tree starting at the insertion point
            fixTree(t);
        }
    }

    /**
     * External remove method
     * @param data - Data to remove
     */
    public void remove(int data) throws Exception {
        root = remove(root, data);
        root.setColor(1);
    }

    /**
     * Finds the smallest value
     * @param n - Starting node
     * @return - Node with the smallest value
     */
    private Node findMin(Node n) {
        if(n.getLeft() == null) {
            //No left child
            return n;
        }
        else {
            //Recursively go down the left side
            return findMin(n.getLeft());
        }
    }

    /**
     * Rotates a node right (clockwise)
     * @param n - Current node
     */
    private void rotateRight(Node n) {
        Node temp = n.getLeft();                       //Get the left subtree
        n.setLeft(temp.getRight());                    //Set the left subtree to the temp node's right subtree

        if (n.getLeft() != null) {
            //New left subtree not empty
            n.getLeft().setParent(n);                  //This node is now the left node's parent
        }

        temp.setParent(n.getParent());                 //Copy the parent

        if (n.getParent() == null) {
            //No parent. This is now the root node
            root = temp;
        }
        else if (n == n.getParent().getLeft()) {
            //Node is its parent's left child
            n.getParent().setLeft(temp);               //Change it to the temp node (old left subtree)
        }
        else {
            //Node is its parent's right child
            n.getParent().setRight(temp);              //Change it to the temp node (old left subtree)
        }

        temp.setRight(n);                              //The original node is now the temporary nodes right child
        n.setParent(temp);                             //The temporary node is now the original node's parent
    }

    /**
     * Rotates a node left (counter-clockwise)
     * @param n - Current node
     */
    private void rotateLeft(Node n) {
        Node temp = n.getRight();                      //Get the right subtree
        n.setRight(temp.getLeft());                    //Set the right subtree to the temp node's left subtree

        if(n.getRight() != null) {
            //New right subtree not empty
            n.getRight().setParent(n);                 //This node is now the right node's parent
        }

        temp.setParent(n.getParent());                 //Copy the parent

        if(n.getParent() == null) {
            //No parent. This is now the root node
            root = temp;
        }
        else if(n == n.getParent().getLeft()) {
            //Node is its parent's left child
            n.getParent().setLeft(temp);               //Change it to the temp node (old right subtree)
        }
        else {
            //Node is its parent's right child
            n.getParent().setRight(temp);              //Change it to the temp node (old right subtree)
        }

        temp.setLeft(n);                               //The original node is now the temporary nodes left child
        n.setParent(temp);                             //The temporary node is now the original node's parent
    }

    /**
     * Rebalances/recolors a tree, starting from where a new node was inserted
     * @param n - Current node
     */
    private void fixTree(Node n) {
        Node p = null;            //Temporary reference for a node's parent
        Node gp = null;           //Temporary reference for a node's grandparent

        //As long as the current node (n) is not the root, is red, and its parent is red...
        while (n != root && n.getColor() == 0  && n.getParent().getColor() == 0) {
            p = n.getParent();
            gp = n.getParent().getParent();


            if (p == gp.getLeft()) {
                //The parent of the current node is left child of its parent
                Node o = gp.getRight();   //Temporary reference to the current node's ommer

                //Ommer is present and is red
                if (o != null && o.getColor() == 0) {
                    gp.setColor(0);              //Update colors
                    p.setColor(1);
                    o.setColor(1);
                    n = gp;                      //Moving up the tree
                }
                else {
                    //If the node is right child of its parent
                    if (n == p.getRight()) {
                        rotateLeft(p);           //Rotation needed for the parent
                        n = p;                   //Moving up the tree
                        p = n.getParent();       //Moving up the tree
                    }
                    else {
                        //The node is left child of its parent
                        rotateRight(gp);         //Rotation needed for the parent's parent
                        swapColors(p, gp);       //Swap the parent and grandparent's colors
                        n = p;                   //Moving up the tree
                    }
                }
            }
            else {
                //The parent of the node is right child of its parent
                Node o = gp.getLeft();                  //Temporary reference for a node's ommer

                //Ommer is present and is red
                if (o != null && o.getColor() == 0) {
                    gp.setColor(0);                     //Update colors
                    p.setColor(1);
                    o.setColor(1);
                    n = gp;                             //Moving up the tree
                }
                else {
                    //If the node is the left child of its parent
                    if (n == p.getLeft()) {
                        rotateRight(p);                 //Rotation needed for the parent
                        n = p;                          //Moving up the tree
                        p = n.getParent();              //Moving up the tree
                    }
                    else {
                        //The node is the right child of its parent
                        rotateLeft(gp);                 //Rotation needed for the parent's parent
                        swapColors(p, gp);              //Swap the parent and parent's parent's colors
                        n = p;                          //Moving up the tree
                    }
                }
            }
        }
        root.setColor(1);                                //Ensure the root node is black
    }

    /**
     * Helper function to swap the colors of two nodes
     * @param n1 First node
     * @param n2 Second node
     */
    private void swapColors(Node n1, Node n2) {
        int c = n1.getColor();
        n1.setColor(n2.getColor());
        n2.setColor(c);
    }

    /**
     * Private function to recursively insert a node
     * @param n - Current node
     * @param data - Data to insert
     * @return - Current node
     * @throws Exception - Duplicate data
     */
    private Node insert(Node n, int data) throws Exception {
        if(data > n.getData()) {
            //Needs to be inserted down the right branch
            if(n.getRight() != null) {
                //A right child is present
                return insert(n.getRight(), data);             //Continue down the right side
            }
            else {
                //No right child. Add this new node there.
                n.setRight(new Node(data, n));
                return n.getRight();
            }
        }
        else if(data < n.getData()) {
            //Needs to be inserted down the left branch
            if(n.getLeft() != null) {
                //A left child is present
                return insert(n.getLeft(), data);             //Continue down the left side
            }
            else {
                //No left child. Add this new node there
                n.setLeft(new Node(data, n));
                return n.getLeft();
            }
        }
        else {
            throw new Exception("Value already exists in the BST");   //Can't have duplicate values in the BST
        }
    }

    /**
     * Private function for recursively removing a node from the tree and
     * (if necessary) replaces it with a successor
     * @param n - Current node
     * @param data - data to be removed
     * @return -  Current node
     * @throws Exception -  data not in the tree
     */
    private Node remove(Node n, int data) throws Exception {
        if(n == null) {
            //Nothing to remove
            throw new Exception(data + " not in tree.");
        }
        else if(data < n.getData()) {
            //Go down left branch
            n.setLeft(remove(n.getLeft(), data));
        }
        else if(data > n.getData()) {
            //Go down right branch
            n.setRight(remove(n.getRight(), data));
        }
        else {
            //Found the value
            if(n.getLeft() == null && n.getRight() == null) {
                //NO children
                if(n == n.getParent().getRight()) {
                    //This node to remove is its parent's right child
                    n.getParent().setRight(null);
                }
                else if(n == n.getParent().getLeft()) {
                    //This node to remove is its parent's left child
                    n.getParent().setLeft(null);
                }
                //Set the reference to null
                n = null;
            }
            else if(n.getLeft() == null && n.getRight() != null) {
                //Has a RIGHT child, no NO LEFT child
                return n.getRight();
            }
            else if(n.getRight() == null && n.getLeft() != null) {
                //Has a LEFT child, but NO RIGHT child
                return n.getLeft();
            }
            else {
                //Has a LEFT AND RIGHT child
                Node t = findMin(n.getRight());                    //Find the successor (smallest value down the right branch)
                n.setData(t.getData());                            //Copy the successor's value
                n.setRight(remove(n.getRight(), t.getData()));     //Recursively update the right branch to find and delete the successor
            }
        }
        return n;                                               //Return the reference to the current node
    }

    /**
     * Iteratively performs a depth-first (preorder) traversal
     */
    public void depthFirst() {
        Stack<Node> s =  new Stack<Node>();
        if(root != null) {
            s.push(root);
        }
        while(!s.isEmpty()) {
            //Pop/remove the node at the top of the stack
            Node n = s.pop();
            System.out.println(n);
            //Add right child (if it exists) to the stack
            if(n.getRight() != null) {
                s.add(n.getRight());
            }
            //Add left child (if it exists) to the stack
            if(n.getLeft() != null) {
                s.add(n.getLeft());
            }
        }
    }

    /**
     * Iteratively performs a breadth-first traversal
     */
    public void breadthFirst() {
        Queue<Node> q = new LinkedList<Node>();
        if(root != null) {
            q.add(root);
        }
        else {
            return;
        }
        while(!q.isEmpty()) {
            //Add left child (if it exists) to the queue
            if(q.peek().getLeft() != null) {
                q.add(q.peek().getLeft());
            }
            //Add right child (if it exists) to the queue
            if(q.peek().getRight() != null) {
                q.add(q.peek().getRight());
            }
            //Pop/remove the node at the head of the queue
            System.out.println(q.remove());
        }
    }
}
