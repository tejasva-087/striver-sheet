#include <iostream>
using namespace std;

int main() {
  // we can only one type of data in arrays.
  // syntax
  // type variableName[size] = {val1, val2, ...};

  // indexing starts from 0 to n - 1 (n being the length of the array)

  // each index stores 4 Bytes of memory
  // in here since the size of the array is 5 it stores 4 * 5 = 20 Bytes of memory
  // int marks[5] = {48, 32, 44, 12, 24};
  // cout << marks[0] << endl;

  // cout << sizeof(marks) << endl;
  // so a better way to get the size of the arrays is like this
  // const int arr_size = 5;
  // int arr[arr_size] = {1, 2, 3, 4, 5};
  // cout << arr_size << endl;

  // int nums[5] = {0};
  // for (int i = 0; i < 5; i++) {
    // cout << nums[i] << ' ';
  // }
  
  int arr[5] = {1, 2, 3, 4, 5};
  cout << size(arr) << endl;
  return 0;
}