package main

import (
	"fmt"
	"testing"
)

func TestOptimus(t *testing.T) {
	tests := []struct {
		inputLines []string
		expected   string
	}{
		{
			[]string{
				"5 6",
				"######",
				"#@E $#",
				"# N  #",
				"#X   #",
				"######",
			},
			"SOUTH\nEAST\nNORTH\nEAST\nEAST\n",
		},
		{
			[]string{
				"10 10",
				"##########",
				"#        #",
				"#  S   W #",
				"#        #",
				"#  $     #",
				"#        #",
				"#@       #",
				"#        #",
				"#E     N #",
				"##########",
			},
			"SOUTH\nSOUTH\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\nNORTH\nNORTH\nNORTH\nNORTH\nNORTH\nNORTH\nWEST\nWEST\nWEST\nWEST\nSOUTH\nSOUTH\n",
		},
		{
			[]string{
				"10 10",
				"##########",
				"# @      #",
				"# B      #",
				"#XXX     #",
				"# B      #",
				"#    BXX$#",
				"#XXXXXXXX#",
				"#        #",
				"#        #",
				"##########",
			},
			"SOUTH\nSOUTH\nSOUTH\nSOUTH\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\n",
		},
		{
			[]string{
				"10 10",
				"##########",
				"#    I   #",
				"#        #",
				"#       $#",
				"#       @#",
				"#        #",
				"#       I#",
				"#        #",
				"#        #",
				"##########",
			},
			"SOUTH\nSOUTH\nSOUTH\nSOUTH\nWEST\nWEST\nWEST\nWEST\nWEST\nWEST\nWEST\nNORTH\nNORTH\nNORTH\nNORTH\nNORTH\nNORTH\nNORTH\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\nSOUTH\nSOUTH\n",
		},
		{
			[]string{
				"10 10",
				"##########",
				"#    1   #",
				"#        #",
				"#        #",
				"#        #",
				"#@       #",
				"#        #",
				"#        #",
				"#    1  $#",
				"##########",
			},
			"SOUTH\nSOUTH\nSOUTH\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\nEAST\nSOUTH\nSOUTH\nSOUTH\nSOUTH\nSOUTH\nSOUTH\nSOUTH\n",
		},
		{
			[]string{
				"5 5",
				"#####",
				"#   #",
				"# $ #",
				"# @ #",
				"#####",
			},
			"LOOP\n",
		},
	}

	for i, test := range tests {
		actual := getInstructionsForInput(test.inputLines)
		if actual != test.expected {
			t.Errorf("test #%d: instructions = %q; expected: %q", i+1, actual, test.expected)
		} else {
			fmt.Printf("Test #%d passed with output:\n%s\n", i+1, actual)
		}
	}
}
