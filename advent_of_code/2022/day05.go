package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func parseCommand(line string) []int {
	r, _ := regexp.Compile("[0-9]+")
	matches :=  r.FindAllString(line, -1)
	var result []int
	for _, match := range matches {
		cmdInt, _ := strconv.Atoi(match)
		result = append(result, cmdInt)
	}
	return result
}

func processCommand(stacks [][]string, params []int) {
	fromStack := stacks[params[1] - 1]
	toStack := stacks[params[2] - 1]
	toMove := params[0]
	//if len(fromStack) <= toMove {
	//	toMove = len(fromStack)
	//}
	for i := 0; i < toMove; i++ {
		x := fromStack[len(fromStack) - 1]
		fromStack = fromStack[:len(fromStack) - 1]
		toStack = append(toStack, x)
	}
	stacks[params[1] - 1] = fromStack
	stacks[params[2] - 1] = toStack
}

func processCommand2(stacks [][]string, params []int) {
	fromStack := stacks[params[1] - 1]
	toStack := stacks[params[2] - 1]
	toMove := params[0]
	//if len(fromStack) <= toMove {
	//	toMove = len(fromStack)
	//}
	partialStack := fromStack[len(fromStack) - toMove: len(fromStack)]
	fromStack = fromStack[:len(fromStack) - toMove]
	for i := 0; i < len(partialStack); i++ {
		toStack = append(toStack, partialStack[i])
	}
	stacks[params[1] - 1] = fromStack
	stacks[params[2] - 1] = toStack
}

func trimStacks(stacks [][]string) {
	printStacks(stacks)
	for j, stack := range stacks {
		end := len(stacks[0])
		for i := 0; i < len(stack); i++ {
			if stack[i] == " " {
				end = i
				break
			}
		}
		stack := stack[:end]
		stacks[j] = stack
	}
}

func printStacks(stacks [][]string) {
	for ind, stack :=  range stacks {
		fmt.Printf("%d: %v\n", ind + 1, stack)
	}
}

func day05_p1() {
	lines := getLines("day05.txt")
	var stacks [][]string
	for i := 0; i < 9; i++ {
		stack := make([]string, 8)
		stacks = append(stacks, stack)
	}
	for ind, line := range lines {
		if ind < 8 {
			for i := 0; i < 9; i++ {
				stacks[i][7 - ind] = string(line[4 * (i + 1) - 3])
			}
		}
		if ind == 8 {
			trimStacks(stacks)
		}
		if ind >= 10 {
			cmd := parseCommand(line)
			fmt.Println(line)
			fmt.Println(cmd)
			printStacks(stacks)
			fmt.Println("before:")
			fmt.Printf("%d: %v\n", cmd[1], stacks[cmd[1] - 1])
			fmt.Printf("%d: %v\n", cmd[2], stacks[cmd[2] - 1])
			processCommand2(stacks, cmd)
			fmt.Println("after:")
			fmt.Printf("%d: %v\n", cmd[1], stacks[cmd[1] - 1])
			fmt.Printf("%d: %v\n", cmd[2], stacks[cmd[2] - 1])
			fmt.Println("")
		}
	}
	printStacks(stacks)
}
