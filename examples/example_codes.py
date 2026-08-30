EXAMPLES = {
    "Python": {
        "name": "Python Binary Search",
        "code": '''def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Example usage:
# arr = [2, 3, 4, 10, 40]
# target = 10
# result = binary_search(arr, target)
'''
    },
    "C++": {
        "name": "C++ Two Sum",
        "code": '''#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numMap;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
        int complement = target - nums[i];
        if (numMap.count(complement)) {
            return {numMap[complement], i};
        }
        numMap[nums[i]] = i;
    }

    return {}; // No solution found
}
'''
    },
    "Java": {
        "name": "Java Fibonacci",
        "code": '''public class Fibonacci {
    public static int fib(int n) {
        if (n <= 1) {
            return n;
        }
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    public static void main(String[] args) {
        System.out.println(fib(10));
    }
}
'''
    },
    "JavaScript": {
        "name": "JavaScript Array Filtering",
        "code": '''function filterEvenNumbers(numbers) {
    let evenNumbers = [];
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i]);
        }
    }
    return evenNumbers;
}

// Example:
// const arr = [1, 2, 3, 4, 5, 6];
// console.log(filterEvenNumbers(arr));
'''
    }
}
