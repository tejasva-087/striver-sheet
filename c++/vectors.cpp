#include <iostream>
#include <vector>
using namespace std;

int sumOfUnique(vector<int>& nums) {
        
        int maxVal = nums[0];

        for (int num : nums) {
            
            maxVal = max(maxVal, num);
        }

        vector<int> hashMap(maxVal + 1, 0);

        for (int num : nums) {
            hashMap[num]++;
        }

        int sum = 0;
        for (int num : hashMap) {
            if (num == 1) {
                sum += num;
            }
        }

        return sum;   
    }

int main() {
  // Vectors are array like data structure but they are dynamic in nature
  // meaning they do not have a fixed size.

  // STL standard template library
  // Provides data structure to be used directly without implementing them.
  // Vector is one of the tool provided by STL

  // syntax
  // vector<type> variableName;
  // vector<type> variableName = {1, 2, 3}
  // vector<type> variableName(size, value)


  vector<int> vec;
  vec = {1, 2, 4};
  // cout << vec[0] << endl;

  vector<int> vec_1 = {1, 4, 2, 4, 5};

  // {0, 0, 0} basically vector of size 3 having values of 0
  vector<int> vec_2(3, 0);

  // traversing in vectors
  for (int num : vec_1) { // this is a for each loop
    // cout << num << endl;
  }

  // vector function
  // 1. size
  // cout << vec_1.size() << endl;

  // 2. push back just like append() in python
  vec_1.push_back(6);
  for (int num : vec_1) {
    // cout << num << " ";
  }
  // cout << endl;

  // 3. pop_back() just like pop() in python
  // vec_1.pop_back();

  // 4. front() gives the font value like the value at index 0
  // cout << vec_1.front() << endl;

  // 5. back() gives value at the last index
  // cout << vec_1.back() << endl;

  // 6. at() gives value at a given index
  // cout << vec_1.at(2) << endl;
  // cout << vec_1[2] << endl;

  vector<int> nums = {1, 4, 6, 2, 1, 9};
  sumOfUnique(nums);

  return 0;
}

