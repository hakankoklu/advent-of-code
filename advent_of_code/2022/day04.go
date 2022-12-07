package main

import (
	"fmt"
	"strconv"
	"strings"
)

func fullOverlaps(first, second []int) bool {
	if (first[0] <= second[0] && first[1] >= second[1]) || (first[0] >= second[0] && first[1] <= second[1]) {
		return true
	}
	return false
}

func partialOverlaps(first, second []int) bool {
	if (first[0] < second[0] && first[1] < second[0]) || (first[0] > second[1] && first[1] > second[1]) {
		return false
	}
	return true
}

func day04() {
	lines := getLines("day04.txt")
	totalFull := 0
	totalPartial := 0
	fmt.Println(len(lines))
	for _, line := range lines {
		ranges := strings.Split(line, ",")
		range1s := strings.Split(ranges[0], "-")
		range2s := strings.Split(ranges[1], "-")
		range11, _ := strconv.Atoi(range1s[0])
		range12, _ := strconv.Atoi(range1s[1])
		range21, _ := strconv.Atoi(range2s[0])
		range22, _ := strconv.Atoi(range2s[1])
		range1 := []int{range11, range12}
		range2 := []int{range21, range22}
		if fullOverlaps(range1, range2) {
			fmt.Println(range1, range2)
			totalFull += 1
		}
		if partialOverlaps(range1, range2) {
			fmt.Println(range1, range2)
			totalPartial += 1
		}
	}
	fmt.Println(totalFull)
	fmt.Println(totalPartial)
}
