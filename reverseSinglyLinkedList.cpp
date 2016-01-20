/*
	Program to reverse a singly linked list
	January 19th, 2016
	
	Uses an iterative algorithm that saves the previous node pointer.
*/

#include <iostream>

using namespace std;

struct Node 
{
	Node* next;
	
	int value;

	Node(int value, Node* n)
	:value(value)
	{
		next = n;
	}
	Node(int value)
	:value(value)
	{
		next = NULL;
	}
	

};

// Prints the values of the linkedlist, for happy testing
void listPrinter(Node* beginning)
{
	Node* current = beginning;
	while ( current != NULL )
	{
		cout << current->value << endl;
		current = current->next;
	}
}

// reverses the linked list
void reverse(Node* n)
{
	Node* before = NULL;
	Node* current = n;
	Node* next = NULL;
	
	while (current)
	{
		next = current-> next;
		current->next = before;
		before = current;
		current = next;
	}
	
	n = before;
	
	listPrinter(n);
}


int main()
{
	cout << "Singly Linked List Reverser!\n";
	
	Node* d = new Node(4);
	Node* c = new Node(3, d);
	Node* b = new Node(2,c);
	Node* a = new Node(1, b);

	cout << "Original:" << endl;
	listPrinter(a);
	
	cout << "Reversed:" << endl;
	reverse(a);
	
	
	
	
	
}