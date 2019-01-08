import java.util.*;

abstract class Node implements Comparable<Node> {
    // the frequency of this tree
    public  int frequency;
    public  char data;
    public  Node left, right; 
    
    public Node(int freq) {
        frequency = freq;
    }
 
    // compares on the frequency
    public int compareTo(Node tree) {
        return frequency - tree.frequency;
    }
}

class HuffmanLeaf extends Node {
    public HuffmanLeaf(int freq, char val) {
        super(freq);
        data = val;
    }
}

class HuffmanNode extends Node {
    public HuffmanNode(Node l, Node r) {
        super(l.frequency + r.frequency);
        left = l;
        right = r;
    }
}

class Decoding {
    void decode(String s, Node root) {
        int len = s.length();
        if (len < 1 || root == null)
            return;

        Node temp = root;
        char c;
        int i = 0;
        while (i <= len) {
            if (temp instanceof HuffmanLeaf) {
                System.out.print(temp.data);
                temp = root;
            }
            
            if (i == len)
                return;
            
            c = s.charAt(i);
            if (c == '0') 
                temp = temp.left;
            else if (c == '1')
                temp = temp.right;
            // 'c' is an unrecognized character
            else
                return;
            
            i++;
        }
    }
}