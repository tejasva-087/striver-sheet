#include <iostream>
using namespace std;

// HOW ARE FUNCTION STORED IN MEMORY?
// There are two types of memory in system:
// 1. STACK -> static allocation
// 2. HEAP -> dynamic allocation

// All our function are stored in stack.


// syntax
// returnType functionName(type parameter, ...) {
//    code
// }

void printHello() {
  cout << "Hello world" << endl;
}

int add(int a, int b) {
  return a + b;
}

int minOfTwo(int a, int b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}

int main() {

  cout << min(101, 12) << endl;

  return 0;
}