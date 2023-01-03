package main

import (
	"encoding/json"
	"fmt"
)

func checkSorted(line1, line2 string) bool {
	l1 := parseLine(line1)
	l2 := parseLine(line2)
	//fmt.Println(l1)
	//fmt.Println(l2)
	return comparison(l1, l2)
}

func comparison(l1, l2 []any) bool {
	smaller := false
	fmt.Printf("comparing \n%v \nvs \n%v\n", l1, l2)
	for i := 0; i < len(l1) && i < len(l2); i++ {
		//fmt.Printf("converting \n%v \nand \n%v\ninto lists\n", l1[i], l2[i])
		//fmt.Printf("first type is %s\n", reflect.TypeOf(l1[i]))
		//fmt.Printf("second type is %s\n", reflect.TypeOf(l1[i]))
		l1s, l1ok := l1[i].([]any)
		l2s, l2ok := l2[i].([]any)
		if !l1ok && !l2ok {
			fmt.Printf("checking %v vs %v\n", l1[i], l2[i])
			if l1[i].(float64) < l2[i].(float64) {
				smaller = true
			}
			if l1[i].(float64) > l2[i].(float64) {
				return false
			}
		} else if !l1ok {
			//fmt.Printf("first one is not a list\n")
			l1s = []any{l1[i]}
			//fmt.Printf("l1 became %v\n", l1s)
		} else if !l2ok {
			//fmt.Printf("second one is not a list\n")
			l2s = []any{l2[i]}
			//fmt.Printf("l2 became %v\n", l2s)
		}
		if (l1ok || l2ok) && !comparison(l1s, l2s) {
			return false
		}
	}
	fmt.Println(smaller)
	if len(l1) > len(l2) && !smaller {
		return false
	}
	return true
}

func parseLine(line string) []any {
	var v []any
	err := json.Unmarshal([]byte(line), &v)
	if err != nil {
		fmt.Println(err)
	}
	return v
}

func day13() {
	lines := getLines("day13-2.txt")
	var results []bool
	for i, _ := range lines {
		if i % 3 == 0 {
			fmt.Println(i / 3 + 1)
			results = append(results, checkSorted(lines[i], lines[i + 1]))
			fmt.Println("")
			fmt.Println("")
		}
	}
	total := 0
	for ind, result := range results {
		if result {
			fmt.Println(ind + 1, result)
			total += ind + 1
		}
	}
	fmt.Println(total)
}