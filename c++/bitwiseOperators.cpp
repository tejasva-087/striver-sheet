#include <iostream>
using namespace std;

int main() {
  // ####################
  // BITWISE and -> &
  // ####################
  // 0 & 0 -> 0
  // 0 & 1 -> 0
  // 1 & 0 -> 0
  // 1 & 1 -> 1

  int a = 4, b = 8;
  cout << (a & b) << endl;
  // so a = 0100 in binary and b = 1000
  // now on this binary value the & is performed
  // so
  // 0100
  // 1000
  // ||||
  // 0000
  // this 0000 when converted to decimal gives 0
  // so our answer is 0


  // ####################
  // BITWISE or -> |
  // ####################
  // 0 | 0 -> 0
  // 0 | 1 -> 1
  // 1 | 0 -> 1
  // 1 | 1 -> 1

  cout << (a | b) << endl;

  // ####################
  // BITWISE xor -> ^
  // ####################
  // if same bits then 0 else 1
  // 0 ^ 0 -> 1
  // 0 ^ 1 -> 0
  // 1 ^ 0 -> 0
  // 1 ^ 1 -> 1

  cout << (a ^ b) << endl;

  // ########################################
  // BITWISE left shift  -> <<
  // ########################################
  // syntax 
  // number << places

  // so basically we shift the bits to left by the 
  // given places nad fill the empty ones with 0

  // eg: 4 << 1
  // so 4 = 100 in binary
  // now we shift these bits by one place
  // it becomes 100_
  // no that last place we add 0
  // so it becomes 1000
  // now 1000 == 8 in decimal no system
  // so we get 8

  cout << (a << 3) << endl;

  // if we are performing this left shift operation like
  // a << b
  // we will get the answer as
  // a * 2**b i.e (a into 2 to the power b)



  // ########################################
  // BITWISE right shift -> >>
  // ########################################
  // syntax 
  // number >> places
  
  // so basically we shift the bits to right by the 
  // given places and fill the empty ones with 0

  // eg: 4 << 1
  // so 4 = 0100 in binary
  // now we shift these bits by one place
  // it becomes 010|0 <- this 0 gets out of the value because on the right we do not have any space for it
  // so it becomes _010
  // now 0010 == 2 in decimal no system
  // so we get 2
  
  cout << (a >> 1) << endl;

  // if we are performing this right shift operation like
  // a >> b
  // we will get the answer as
  // a / 2**b i.e (a divided by 2 to the power b)

  return 0;
}