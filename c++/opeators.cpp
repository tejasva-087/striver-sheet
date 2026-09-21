#include <iostream>
using namespace std;

int main() {
  // #########################
  // ###### ARITHMETIC #######
  int a = 5, b = 2;

  // cout << "SUM: " << a + b << endl;
  // cout << "DIFFERENCE: " << a - b << endl;
  // cout << "PRODUCT: " << a * b << endl;
  // cout << "MODULO (REMAINDER): " << a % b << endl;
  // cout << "DIVISION: " << a / b << endl;

  // *** DIVISION ***
  // The division operator works a bit differently

  // so 5 / 2 -> 2 not 2.5
  // This is because when and int value is divided by an int value we get int value as answer.
  // so int / int -> int

  // now if we have different datatype like 
  // int / float or float / int or double / float or double / int and like all such combinations
  // so here like 5.0 / 2 or 5 / 2.0 and like that
  // we get the result as the datatype which is bigger
  // so if int / float -> float, int / double -> double, double / int -> double

  double a_ = 5.0;
  int b_ = 2;
  // cout << "DIVISION OF double by int: " << a_ / b_ << endl;
  // cout << "RESULT SIZE: " << sizeof(a / b) << endl;
  // cout << "RESULT SIZE: " << sizeof(a_ / b_) << endl;

  // *** HERE WE CAN USE TYPECASTING ***
  // cout << "TYPECASTING TO DIVIDE AND GET REQUIRED RESULT: " << a / (float) b << endl;

  // #########################
  // ######### UNARY #########
  // These are basically the operators that require 
  // only one operand to does its calculations
  // instead of two.

  // ++ and --
  // ++ -> increment
  // -- -> decrement

  int val_a = 10, val_b;
  
  // FIRST DO THE WORK THEN DO THE WORK INCREMENT THE VALUE OF a
  val_b = val_a++;
  cout << val_b << endl;
  cout << val_a << endl;
  // FIRST INCREMENT THE VALUE OF a THEN DO THE WORK
  val_a = 10;
  val_b = ++val_a;
  cout << val_b << endl;
  cout << val_a << endl;


  // #########################
  // ###### RELATIONAL #######

  // ==, !=,  <= , >=, <, >

  // #########################
  // ######## LOGICAL ########

  // or -> ||
  // and -> &&
  // not -> !
  // cout << ((3 < 1) || (3 < 5)) << endl;

  return 0;
}