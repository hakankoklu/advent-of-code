package main

import (
	"fmt"
	"strconv"
	"strings"
)

func absDiffInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func move(head, tail point, direction string, distance int, visited map[point]bool) (point, point) {
	if direction == "R" {
		for i := 0; i < distance; i++ {
			head = point{head.x + 1, head.y}
			tail = moveTail(head, tail)
			visited[tail] = true
		}
	}
	if direction == "L" {
		for i := 0; i < distance; i++ {
			head = point{head.x - 1, head.y}
			tail = moveTail(head, tail)
			visited[tail] = true
		}
	}
	if direction == "U" {
		for i := 0; i < distance; i++ {
			head = point{head.x, head.y + 1}
			tail = moveTail(head, tail)
			visited[tail] = true
		}
	}
	if direction == "D" {
		for i := 0; i < distance; i++ {
			head = point{head.x, head.y - 1}
			tail = moveTail(head, tail)
			visited[tail] = true
		}
	}
	//fmt.Println(head, tail)
	//fmt.Println(visited)
	return head, tail
}

func moveTail(head, tail point) point {
	xd := absDiffInt(head.x, tail.x)
	yd := absDiffInt(head.y, tail.y)
	if xd <= 1 && yd <= 1 {
		return tail
	} else if xd == 2 {
		tail.x = (tail.x + head.x) / 2
		if yd == 2 {
			tail.y = (tail.y + head.y) / 2
		} else {
			tail.y = head.y
		}
	} else if yd == 2 {
		tail.y = (tail.y + head.y) / 2
		if xd == 2 {
			tail.x = (tail.x + head.x) / 2
		} else {
			tail.x = head.x
		}
	} else {
		panic("head and tail has diverged!")
	}
	return tail
}

func moveKnots(knots []point, direction string, distance int, visited map[point]bool) []point {
	fmt.Println(direction, distance)
	head := knots[0]
	if direction == "R" {
		for i := 0; i < distance; i++ {
			head = point{head.x + 1, head.y}
			knots[0] = head
			for j := 1; j < len(knots); j++ {
				tail := knots[j]
				tail = moveTail(knots[j - 1], tail)
				knots[j] = tail
				visited[knots[len(knots) - 1]] = true
			}
		}
	}
	if direction == "L" {
		for i := 0; i < distance; i++ {
			head = point{head.x - 1, head.y}
			knots[0] = head
			for j := 1; j < len(knots); j++ {
				tail := knots[j]
				tail = moveTail(knots[j - 1], tail)
				knots[j] = tail
				visited[knots[len(knots) - 1]] = true
			}
		}
	}
	if direction == "U" {
		for i := 0; i < distance; i++ {
			head = point{head.x, head.y + 1}
			knots[0] = head
			for j := 1; j < len(knots); j++ {
				tail := knots[j]
				tail = moveTail(knots[j - 1], tail)
				knots[j] = tail
				visited[knots[len(knots) - 1]] = true
			}
		}
	}
	if direction == "D" {
		for i := 0; i < distance; i++ {
			head = point{head.x, head.y - 1}
			knots[0] = head
			for j := 1; j < len(knots); j++ {
				tail := knots[j]
				tail = moveTail(knots[j - 1], tail)
				knots[j] = tail
				visited[knots[len(knots) - 1]] = true
			}
		}
	}
	fmt.Println(knots)
	fmt.Println(visited)
	return knots
}


func day09() {
	lines := getLines("day09.txt")
	visited := make(map[point]bool)
	head := point{0, 0}
	tail := point{0, 0}
	for _, line := range lines {
		cmd := strings.Split(line, " ")
		distance, _ := strconv.Atoi(cmd[1])
		head, tail = move(head, tail, cmd[0], distance, visited)
	}
	fmt.Println(len(visited))
}

func day09_p2() {
	lines := getLines("day09.txt")
	visited := make(map[point]bool)
	var knots []point
	for i := 0; i < 10; i++ {
		knots = append(knots, point{0, 0})
	}
	for _, line := range lines {
		cmd := strings.Split(line, " ")
		distance, _ := strconv.Atoi(cmd[1])
		knots = moveKnots(knots, cmd[0], distance, visited)
	}
	fmt.Println(len(visited))
}