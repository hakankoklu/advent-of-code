package main

import (
	"fmt"
	"strings"
)

func gameResult(first int, second int) (int, int) {
	if first == second {
		return 3, 3
	} else if first == 1 {
		if second == 2 {
			return 0, 6
		}
		return 6, 0
	}  else if first == 2 {
		if second == 3 {
			return 0, 6
		}
		return 6, 0
	} else {
		if second == 1 {
			return 0, 6
		}
		return 6, 0
	}
}

func whatToPlay(score int, other int) int {
	if score == 3 {
		return other
	}
	if score == 6 {
		if other == 1 {
			return 2
		}
		if other == 2 {
			return 3
		}
		return 1
	}
	if score == 0 {
		if other == 1 {
			return 3
		}
		if other == 2 {
			return 1
		}
		return 2
	}
	return 2
}

func day02_p1() {
	lines := getLines("day02.txt")
	letterMap := map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
		"X": 1,
		"Y": 2,
		"Z": 3,
	}
	shapeMap := map[int]int{
		1: 1,
		2: 2,
		3: 3,
	}
	total := 0
	for _, line := range lines {
		inputs := strings.Split(line, " ")
		input1 := letterMap[inputs[0]]
		input2 := letterMap[inputs[1]]
		_, score2 := gameResult(input1, input2)
		total += score2 + shapeMap[input2]
	}
	fmt.Println(total)
}

func day02_p2() {
	lines := getLines("day02.txt")
	letterMap := map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
	}
	scoreMap := map[string]int{
		"X": 0,
		"Y": 3,
		"Z": 6,
	}
	total := 0
	for _, line := range lines {
		inputs := strings.Split(line, " ")
		input1 := letterMap[inputs[0]]
		input2 := scoreMap[inputs[1]]
		toPlay := whatToPlay(input2, input1)
		total += toPlay + input2
	}
	fmt.Println(total)
}
