// reverse C string c++

#include <iostream>

// do we return the reversed string, or nah?
void reverse(char* end){
	char* front = end;
	while (*front){ // go until hit null char
		front++;
	}
	front--; 
	// the swap
	while (front > end){
		char temp = *front;
		*front = *end;
		*end = temp;
		front--;
		end++;
	}
}

int main(){
    char word[] = "yes princess";
    reverse(word);
    std::cout << word;
    return 0;
}