import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

// NOTE: a better solution than the one I came up with would be to use the 'tortoise and the hare' algorithm to detect the cycle.
// My algorithm is the naive one!

/*
 * Problem: A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
 * The function takes a pointer to a Node object named 'head' that points to the head of a linked list and
 * must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.
 */
public class Solution {
    static class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    static class SinglyLinkedList {
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;

        public SinglyLinkedList() {
            this.head = null;
            this.tail = null;
        }

        public void insertNode(int nodeData) {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null)
                this.head = node;
            else
                this.tail.next = node;

            this.tail = node;
        }
    }

    public static void printSinglyLinkedList(SinglyLinkedListNode node, String sep, BufferedWriter bufferedWriter) throws IOException {
        while (node != null) {
            bufferedWriter.write(String.valueOf(node.data));

            node = node.next;

            if (node != null)
                bufferedWriter.write(sep);
        }
    }
    
    /*
     * Note: If the list is empty, 'head' will be null.
     * Constraints: 0 <= list_size <= 1000 
     */
    static boolean hasCycle(SinglyLinkedListNode head) {
        // singly linked list is empty then obviously it has no cycles
        if (head == null)
            return false;
        
        int count = 1;
        Set<SinglyLinkedListNode> seenNodes = new HashSet<>();
        SinglyLinkedListNode temp = head.next;
        while (temp != null && count <= 1000) {
            // add returns false if the set already contains the element
            if (!(seenNodes.add(temp)))
                return true;
            
            count++;
            temp = temp.next;
        }
        return false;
    }
}