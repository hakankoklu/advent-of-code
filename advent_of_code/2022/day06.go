package main

import "fmt"


func checkUniqueness(text string) bool {
	fmt.Printf("checking %s\n", text)
	lets := make(map[rune]bool)
	for _, let := range text {
		lets[let] = true
	}
	return len(lets) == len(text)
}


func day06() {
	lines := getLines("day06.txt")
	length := 14
	for i := 0; i < len(lines[0]) - length; i++ {
		if checkUniqueness(lines[0][i:i + length]) {
			fmt.Println(i + length)
			break
		}
	}
	fmt.Println("done")
}
