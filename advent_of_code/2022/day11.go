package main

import (
	"fmt"
	"sort"
)

func day11_test() {
	itemLists := [][]int{
		[]int{79, 98},
		[]int{54, 65, 75, 74},
		[]int{79, 60, 97},
		[]int{74},
	}

	divisors := []int{23, 19, 13, 17}
	toMonkey := [][]int{
		[]int{2, 3},
		[]int{2, 0},
		[]int{1, 3},
		[]int{0, 1},
	}

	funcs := []monkeyFunc{
		func(x int) int { return x },
		func(x int) int { return x + 6 },
		func(x int) int { return x * x },
		func(x int) int { return x + 3 },
	}

	inspectCount := []int{0, 0, 0, 0, 0, 0, 0, 0}

	//fmt.Println(itemLists)
	rounds := 20
	for i := 0; i < rounds; i++ {
		for i, items := range itemLists {
			for _, item := range items {
				inspectCount[i] ++
				newItem := funcs[i](item) / 3
				if newItem%divisors[i] == 0 {
					itemLists[toMonkey[i][0]] = append(itemLists[toMonkey[i][0]], newItem)
				} else {
					itemLists[toMonkey[i][1]] = append(itemLists[toMonkey[i][1]], newItem)
				}
				itemLists[i] = []int{}
			}
		}
		fmt.Println(itemLists)
	}
	fmt.Println(inspectCount)
}

type monkeyFunc func(int) int


func day11() {
	itemLists := [][]int{
		[]int{65, 58, 93, 57, 66},
		[]int{76, 97, 58, 72, 57, 92, 82},
		[]int{90, 89, 96},
		[]int{72, 63, 72, 99},
		[]int{65},
		[]int{97, 71},
		[]int{83, 68, 88, 55, 87, 67},
		[]int{64, 81, 50, 96, 82, 53, 62, 92},
	}

	divisors := []int{19, 3, 13, 17, 2, 11, 5, 7}
	allDivisors := 1
	for _, i := range divisors {
		allDivisors *= i
	}
	toMonkey := [][]int{
		[]int{6, 4},
		[]int{7, 5},
		[]int{5, 1},
		[]int{0, 4},
		[]int{6, 2},
		[]int{7, 3},
		[]int{2, 1},
		[]int{3, 0},
	}

	funcs := []monkeyFunc{
		func(x int) int { return x * 7 },
		func(x int) int { return x + 4 },
		func(x int) int { return x * 5 },
		func(x int) int { return x * x },
		func(x int) int { return x + 1 },
		func(x int) int { return x + 8 },
		func(x int) int { return x + 2 },
		func(x int) int { return x + 5 },
	}

	inspectCount := []int{0, 0, 0, 0, 0, 0, 0, 0}

	//fmt.Println(itemLists)
	rounds := 10000
	for i := 0; i < rounds; i++ {
		for i, items := range itemLists {
			for _, item := range items {
				inspectCount[i] ++
				newItem := funcs[i](item) % allDivisors
				if newItem%divisors[i] == 0 {
					itemLists[toMonkey[i][0]] = append(itemLists[toMonkey[i][0]], newItem)
				} else {
					itemLists[toMonkey[i][1]] = append(itemLists[toMonkey[i][1]], newItem)
				}
				itemLists[i] = []int{}
				//fmt.Println(itemLists)
			}
		}
	}
	sort.Ints(inspectCount)
	fmt.Println(inspectCount)
	fmt.Println(inspectCount[len(inspectCount) - 1] * inspectCount[len(inspectCount) - 2])
}