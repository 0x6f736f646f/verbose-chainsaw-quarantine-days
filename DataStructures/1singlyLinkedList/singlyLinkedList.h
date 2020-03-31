#ifndef INT_LINKED_LIST
#define INT_LINKED_LIST

class IntNode{
    private:
        /* data */
    public:
        int info;
        IntNode *next;
        IntNode(int element, intNode *ptr = 0){
            info = element;
            next = ptr;
        }
};

class IntSinglyLinkedList
{
private:
    IntNode *head, *tail;
public:
    IntSinglyLinkedList(/* args */){
        head = tail = 0;
    }
    ~IntSinglyLinkedList();
    int isEmpty(){
        return head == 0;
    }
    void addToHead(int);
    void addToTail(int);
    int deleteFromHead();
    int deleteFromTail();
    void deleteNode();
    bool isInList(int) const;
};

#endif