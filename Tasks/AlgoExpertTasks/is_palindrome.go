// Write a function that takes in a non-empty string and that returns a boolean
// representing whether the string is a palindrome.

// A palindrome is defined as a string that's written the same forward and
// backward. Note that single-character strings are palindromes.

// Sample Input:
// string = "abcdcba"

// Sample Output:
// True

package main

func isPalindrome(s string) bool {
	reversed := []rune(s)
	for i, j := 0, len(reversed)-1; i < j; i, j = i+1, j-1 {
		reversed[i], reversed[j] = reversed[j], reversed[i]
	}
	return s == string(reversed)
}