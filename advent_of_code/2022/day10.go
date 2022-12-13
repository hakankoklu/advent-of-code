package main

import (
	"fmt"
	"strconv"
	"strings"
)

func getValue(regValue map[int]int, cycle int) int {
	for {
		if value, ok := regValue[cycle - 1];ok {
			return value
		}
		cycle--
	}
}

func getNewSprite(mid int) []string {
	var sprite []string
	for i := 0; i < 40; i++ {
		if mid - 1 <= i && i <= mid + 1 {
			sprite = append(sprite, "#")
		} else {
			sprite = append(sprite, ".")
		}
	}
	return sprite
}

func day10() {
	lines := getLines("day10.txt")
	regValue := make(map[int]int)
	curValue := 1
	curCycle := 0
	regValue[curCycle] = curValue
	for _, line := range lines {
		if line == "noop" {
			curCycle += 1
			regValue[curCycle] = curValue
		} else {
			cmd := strings.Split(line, " ")
			v, _ := strconv.Atoi(cmd[1])
			curCycle += 2
			curValue += v
			regValue[curCycle] = curValue
		}
	}
	cycles := []int{20, 60, 100, 140, 180, 220}
	total := 0
	for _, cycle := range cycles {
		total += cycle * getValue(regValue, cycle)
	}
	fmt.Println(total)
}

func day10_p2() {
	lines := getLines("day10.txt")
	regValue := make(map[int]int)
	curValue := 1
	curCycle := 0
	regValue[curCycle] = curValue
	for _, line := range lines {
		if line == "noop" {
			curCycle += 1
			regValue[curCycle] = curValue
		} else {
			cmd := strings.Split(line, " ")
			v, _ := strconv.Atoi(cmd[1])
			curCycle += 2
			curValue += v
			regValue[curCycle] = curValue
		}
	}
	var screen [][]string
	for i := 0; i < 6; i++ {
		var row []string
		for j := 0; j < 40; j++ {
			cycle := 40 * i + j + 1
			curSprite := getNewSprite(getValue(regValue, cycle))
			row = append(row, curSprite[j])
		}
		screen = append(screen, row)
	}
	for _, row := range screen {
		fmt.Println(row)
	}
}