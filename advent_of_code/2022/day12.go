package main

import (
	"fmt"
	"strings"
)

func day12() {
	lines := getLines("day12.txt")
	abc := "abcdefghijklmnopqrstuvwxyz"
	var heightmap [][]int
	var as []point
	var start point
	var end point

	for i, line := range lines {
		var row []int
		for j, let := range line {
			if let == 'S' {
				start = point{i, j}
				let = 'a'
			}
			if let == 'E' {
				end = point{i, j}
				let = 'z'
			}
			height := strings.Index(abc, string(let))
			row = append(row, height)
		}
		heightmap = append(heightmap, row)
	}
	printTrees(heightmap, false)
	fmt.Println(start)
	fmt.Println(end)

	graph := make(map[point][]point)

	for i, row := range heightmap {
		for j, height := range row {
			var conns []point
			// up
			if i >= 1 {
				if heightmap[i-1][j]-1 <= height {
					conns = append(conns, point{i - 1, j})
				}
			}
			// down
			if i < len(heightmap)-1 {
				if heightmap[i+1][j]-1 <= height {
					conns = append(conns, point{i + 1, j})
				}
			}
			// left
			if j >= 1 {
				if heightmap[i][j-1]-1 <= height {
					conns = append(conns, point{i, j - 1})
				}
			}
			// right
			if j < len(heightmap[0])-1 {
				if heightmap[i][j+1]-1 <= height {
					conns = append(conns, point{i, j + 1})
				}
			}
			graph[point{i, j}] = conns
			if height == 0 {
				as = append(as, point{i, j})
			}
		}
	}
	fmt.Println(graph)
	for _, a := range as {
		start = a
	queue := []point{start}
	visited := make(map[point]bool)
	added := make(map[point]bool)
	steps := 0
	found := false
	for len(queue) != 0 {
		toCheck := len(queue)
		//fmt.Printf("will check %d nodes\n", toCheck)
		for i := 0; i < toCheck; i++ {
			visited[queue[i]] = true
			for _, p := range graph[queue[i]] {
				if _, ok := visited[p]; ok {
					continue
				}
				if p == end {
					fmt.Printf("got to end in %d steps\n", steps)
					found = true
					break
				} else {
					if _, ok := added[p]; ok {
						continue
					}
					queue = append(queue, p)
					added[p] = true
				}
			}
			if found {
				break
			}
		}
		if found {
			break
		}
		queue = queue[toCheck:]
		//fmt.Println("queue:")
		//fmt.Println(queue)
		//fmt.Println("visited:")
		//fmt.Println(visited)
		steps++
	}
}
}
