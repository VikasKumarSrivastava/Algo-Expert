import java.util.*;

// Do not edit the class below except for the insertKeyValuePair,
// getValueFromKey, and getMostRecentKey methods. Feel free
// to add new properties and methods to the class.
class Program {
  static class LRUCache {
    int maxSize;
    class Node{
      Node next,prev;
      String key;
      int val;
      public Node(String _key,int _val){
        key = _key;
        val = _val;
      }
    }
    Node head = new Node("0",0),tail = new Node("0",0);
    Map<String,Node>map = new HashMap();
    
    public LRUCache(int maxSize) {
      this.maxSize = maxSize > 1 ? maxSize : 1;
      head.next = tail;
      tail.prev = head;  
    }


    public void insertKeyValuePair(String key, int value) {
      // Write your code here.
      if(map.containsKey(key)){
        remove(map.get(key));
      }
      if(maxSize==map.size()){
        remove(tail.prev);
      }
      insert(new Node(key,value));
    }

    public LRUResult getValueFromKey(String key) {
      // Write your code here.
      if(map.containsKey(key)){
        Node node = map.get(key);
        remove(node);
        insert(node);
        Program.LRUResult lru = new Program.LRUResult(true,node.val);
        return lru;
    }else{
         Program.LRUResult lru = new Program.LRUResult(false,-1);
        return lru;
      }
    }

    public String getMostRecentKey() {
      // Write your code here.
      return head.next.key;
    }

    private void remove(Node node){
      map.remove(node.key);
      node.prev.next = node.next;
      node.next.prev= node.prev;
    }

    private void insert(Node node){
      map.put(node.key,node);
      node.next = head.next;
      node.next.prev = node;
      head.next = node;
      node.prev = head;
    }
  }

  static class LRUResult {
    boolean found;
    int value;

    public LRUResult(boolean found, int value) {
      this.found = found;
      this.value = value;
    }
  }
}
