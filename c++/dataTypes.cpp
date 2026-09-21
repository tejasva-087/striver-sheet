#include <iostream>
using namespace std;

int main() {
  // #########################
  // ####### DATATYPES #######
  
  // INTEGERS (int)
  // int have size 4 i.e. 4 Bytes = 4 * 8bits
  // The numbers are converted to a binary nad then stored
  int a = 10;
  int b = 20;

  // sizeof tells the size of value in bytes
  // cout << sizeof(a + b) << endl;


  // CHARACTER (char)
  // The character are stored in the memory via first getting their 
  // ASCII value and then converting them into binary.
  // ASCII = American Standard Code for Information Interchange
  // A->65 Z->90 a->99 z->124
  char char_ = 'a';

  // cout << char_ << endl;
  // cout << sizeof(char_) << endl;

  // FLOATING (float)
  // They store decimal point values.
  // Floats uses 4 Bytes
  // Double uses 8 Bytes
  float price_double = 100.99; // if we dont use f in the end it makes it a double
  // so rn 100.99 is a double value tat will be converted to a float value
  float price_float = 100.99f; // to use a float we need to put f in the end
  float PI = 3.14;

  // cout << sizeof(price_double) << endl;
  // cout << sizeof(price_float) << endl;

  // BOOLEAN (bool)
  // true -> 1
  // false -> 0

  bool val = 1;
  // cout << val << endl;

  // #########################
  // #########################

  // #########################
  // #### TYPE CONVERSION ####
  // 1. TYPE CASTING: 
  // This process is dome by the programmer
  // so explicit process
  double price = 100.99;
  int new_price = (int)price; // 100 not 101 (so remove the decimal part basically)

  // cout << new_price << endl;

  // 2. TYPE CONVERSION: 
  // This is implicit process which the 
  // compiler does automatically
  char grade = 'A';
  int grade_val = grade; // this is implicit conversion form char to int

  // cout << grade_val << endl;

  // #########################
  // ######### INPUT #########

  int marks;
  cout << "Enter the marks: ";
  cin >> marks;
  cout << marks << endl;

  return 0;
}