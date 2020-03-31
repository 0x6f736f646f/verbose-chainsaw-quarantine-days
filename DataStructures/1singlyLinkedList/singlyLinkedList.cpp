#include <iostream.h>
#include "1singlyLinkedList/singlyLinkedList.h"

IntSinglyLinkedList::~IntSinglyLinkedList(){
    for (IntNode *p; !isEmpty();){
        p = head->next;
        delete head;
        head = p;
    }
}

void IntSinglyLinkedList::addToHead(int element){
    head = new IntNode(element, head);
    if (tail == 0){
        tail = head;
    }
}

void IntSinglyLinkedList::addToTail(int element){

}

int IntSinglyLinkedList::deleteFromHead(){

}

int IntSinglyLinkedList::deleteFromTail(){

}

void IntSinglyLinkedList::deleteNode(){

}

bool IntSinglyLinkedList::isInList(int element) const {
    IntNode *tmp;
    for(tmp = head; tmp != 0 && !(tmp->info == element); tmp = tmp->next);
    return tmp != 0;
}
