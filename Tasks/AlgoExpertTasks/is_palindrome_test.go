package main

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		given    string
		expected bool
	}{
		{"abcdcba", true},
		{"a", true},
		{"ab", false},
		{"aba", true},
		{"abb", false},
		{"abba", true},
		{"abcdefghhgfedcba", true},
		{"abcdefghihgfedcba", true},
	}
	for i, test := range tests {
		actual := isPalindrome(test.given)
		if actual != test.expected {
			t.Errorf("test #%d: actual = %v; expected: %v", i+1, actual, test.expected)
		}
	}
}
