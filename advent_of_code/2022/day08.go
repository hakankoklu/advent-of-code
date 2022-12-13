package main

import (
	"fmt"
	"strconv"
)

type point struct {
	x int
	y int
}

func printTrees(trees [][]int, withInd bool) {
	for ind, stack :=  range trees {
		if withInd {
			fmt.Printf("%d: %v\n", ind+1, stack)
		} else {
			fmt.Println(stack)
		}
	}
}

func day08_p1() {
	lines := getLines("day08.txt")
	var trees [][]int
	for _, line := range lines {
		var newTreeLine []int
		for _, l := range line {
			t, _ := strconv.Atoi(fmt.Sprintf("%c",l))
			newTreeLine = append(newTreeLine, t)
		}
		trees = append(trees, newTreeLine)
	}
	visible := make(map[point]bool)
	// left
	for i := 0; i < len(trees); i++ {
		mmax := trees[i][0]
		for j := 0; j < len(trees[0]); j++ {
			if j == 0 {
				visible[point{i, j}] = true
				fmt.Println(i, j, trees[i][j], mmax)
			} else if trees[i][j] > mmax {
				fmt.Printf("%d is bigger than %d\n", trees[i][j], mmax)
				visible[point{i, j}] = true
				mmax = trees[i][j]
				fmt.Println(i, j, trees[i][j], mmax)
			}
		}
	}
	// right
	for i := 0; i < len(trees); i++ {
		mmax := trees[i][len(trees[0]) - 1]
		for j := len(trees[0]) - 1; j >= 0; j-- {
			if j == len(trees[0]) - 1 {
				visible[point{i, j}] = true
				fmt.Println(i, j, trees[i][j], mmax)
			} else if trees[i][j] > mmax {
				fmt.Printf("%d is bigger than %d\n", trees[i][j], mmax)
				visible[point{i, j}] = true
				mmax = trees[i][j]
				fmt.Println(i, j, trees[i][j], mmax)
			}
		}
	}
	// top
	for j := 0; j < len(trees[0]); j++ {
		mmax := trees[0][j]
		for i := 0; i < len(trees); i++ {
			if i == 0 {
				visible[point{i, j}] = true
				fmt.Println(i, j, trees[i][j], mmax)
			} else if trees[i][j] > mmax {
				visible[point{i, j}] = true
				mmax = trees[i][j]
				fmt.Println(i, j, trees[i][j], mmax)
			}
		}
	}
	// bottom
	for j := 0; j < len(trees[0]); j++ {
		mmax := trees[len(trees) - 1][j]
		for i := len(trees) - 1; i >= 0; i-- {
			if i == len(trees) - 1 {
				visible[point{i, j}] = true
				fmt.Println(i, j, trees[i][j], mmax)
			} else if trees[i][j] > mmax {
				visible[point{i, j}] = true
				mmax = trees[i][j]
				fmt.Println(i, j, trees[i][j], mmax)
			}
		}
	}
	fmt.Println(trees)
	fmt.Println(visible)
	fmt.Println(len(visible))
}

func day08_p2() {
	lines := getLines("day08.txt")
	var trees [][]int
	for _, line := range lines {
		var newTreeLine []int
		for _, l := range line {
			t, _ := strconv.Atoi(fmt.Sprintf("%c",l))
			newTreeLine = append(newTreeLine, t)
		}
		trees = append(trees, newTreeLine)
	}
	var scenicScore [][]int
	fmt.Println("the trees")
	printTrees(trees, false)
	// to left
	for i := 0; i < len(trees); i++ {
		curScore := 0
		scoreLimits := make(map[int]int)
		var curScenicLine []int
		for j := 0; j < len(trees[0]); j++ {
			if j == 0 {
				curScore = 0
			} else if trees[i][j] > trees[i][j - 1] {
				if lastP, ok := scoreLimits[trees[i][j]]; ok {
					curScore = j - lastP
				} else {
					curScore = j
				}
			} else {
				curScore = 1
			}
			for k := 0; k <= trees[i][j]; k++ {
				scoreLimits[k] = j
			}
			//fmt.Println(i, j, trees[i][j], curScore)
			curScenicLine = append(curScenicLine, curScore)
		}
		scenicScore = append(scenicScore, curScenicLine)
	}
	fmt.Println("after left")
	printTrees(scenicScore, false)
	// to right
	for i := 0; i < len(trees); i++ {
		curScore := 0
		scoreLimits := make(map[int]int)
		for j := len(trees[0]) - 1; j >= 0; j-- {
			if j == len(trees[0]) - 1 {
				curScore = 0
			} else if trees[i][j] > trees[i][j + 1] {
				if lastP, ok := scoreLimits[trees[i][j]]; ok {
					curScore = lastP - j
				} else {
					curScore = len(trees[0]) - j - 1
				}
			} else {
				curScore = 1
			}
			for k := 0; k <= trees[i][j]; k++ {
				scoreLimits[k] = j
			}
			//fmt.Println(i, j, trees[i][j], curScore)
			scenicScore[i][j] = scenicScore[i][j] * curScore
		}
	}
	fmt.Println("after right")
	printTrees(scenicScore, false)
	// towards top
	for j := 0; j < len(trees[0]); j++ {
		curScore := 0
		scoreLimits := make(map[int]int)
		for i := 0; i < len(trees); i++ {
			if i == 0 {
				curScore = 0
			} else if trees[i][j] > trees[i - 1][j] {
				if lastP, ok := scoreLimits[trees[i][j]]; ok {
					curScore = i - lastP
				} else {
					curScore = i
				}
			} else {
				curScore = 1
			}
			for k := 0; k <= trees[i][j]; k++ {
				scoreLimits[k] = i
			}
			//fmt.Println(i, j, trees[i][j], curScore)
			scenicScore[i][j] = scenicScore[i][j] * curScore
		}
	}
	fmt.Println("after top")
	printTrees(scenicScore, false)
	// bottom
	for j := 0; j < len(trees[0]); j++ {
		curScore := 0
		scoreLimits := make(map[int]int)
		for i := len(trees) - 1; i >= 0; i-- {
			if i == len(trees) - 1 {
				curScore = 0
			} else if trees[i][j] > trees[i + 1][j] {
				if lastP, ok := scoreLimits[trees[i][j]]; ok {
					curScore = lastP - i
				} else {
					curScore = len(trees) - i - 1
				}
			} else {
				curScore = 1
			}
			for k := 0; k <= trees[i][j]; k++ {
				scoreLimits[k] = i
			}
			//fmt.Println(i, j, trees[i][j], curScore)
			scenicScore[i][j] = scenicScore[i][j] * curScore
		}
	}
	highest := scenicScore[0][0]
	for i := 0; i < len(trees[0]); i++ {
		for j := 0; j < len(trees[0]); j++ {
			if scenicScore[i][j] > highest {
				highest = scenicScore[i][j]
			}
		}
	}
	fmt.Println("final")
	printTrees(scenicScore, false)
	fmt.Println(highest)
}
