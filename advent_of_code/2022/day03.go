package main

import (
	"fmt"
	"strings"
)

func findOverlap(one, two, three string) string {
	overlaps := make(map[string]int)
	for _, let := range one {
		if strings.Contains(two, string(let)) {
			overlaps[string(let)] = 1
		}
	}
	for _, let := range three {
		if _, ok := overlaps[string(let)]; ok {
			return string(let)
		}
	}
	panic("no badge found")
}

func day03_p1() {
	lines := getLines("day03.txt")
	abc := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	abcMap := make(map[string]int)
	for i, let := range abc {
		abcMap[string(let)] = i + 1
	}
	var overlaps []string
	for _, line := range lines {
		firstPart :=  make(map[string]int)
		for i := 0; i < len(line); i++ {
			j := string(line[i])
			if i < len(line) / 2 {
				firstPart[j] = 1
			} else {
				if _, ok := firstPart[j]; ok {
					overlaps = append(overlaps, j)
					break
				}
			}
		}
	}
	total := 0
	for _, let := range overlaps {
		total += abcMap[let]
	}
	fmt.Println(total)
}


func day03_p2() {
	lines := getLines("day03.txt")
	abc := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	abcMap := make(map[string]int)
	for i, let := range abc {
		abcMap[string(let)] = i + 1
	}
	var overlaps []string
	for i := 0; i < len(lines) / 3; i++ {
		overlaps = append(overlaps, findOverlap(lines[3 * i], lines[3 * i + 1], lines[3 * i + 2]))
	}
	fmt.Println(overlaps)
	total := 0
	for _, let := range overlaps {
		total += abcMap[let]
	}
	fmt.Println(total)
}