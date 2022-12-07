package main

import (
	"fmt"
	"sort"
	"strconv"
)

func day01() {
	fmt.Println("day 1 baby!!")
	lines := getLines("day01.txt")
	var elfInventory []int
	var curCalorie int
	for _, line := range lines {
		if line == "" {
			elfInventory = append(elfInventory, curCalorie)
			curCalorie = 0
		}
		newCalorie, _ := strconv.Atoi(line)
		curCalorie += newCalorie
	}
	elfInventory = append(elfInventory, curCalorie)
	// part1
	fmt.Println(getMax(elfInventory))
	// part2
	sort.Ints(elfInventory)
	numElves := len(elfInventory)
	fmt.Println(elfInventory[numElves -3] + elfInventory[numElves -2] + elfInventory[numElves -1])
}
