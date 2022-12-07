package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type FileType int

const (
	DIR FileType = iota
	FILE
)

type Node struct {
	space	int
	name	string
	filetype	FileType
	children	[]*Node
	parent	*Node
}

func (n *Node) addChild(childNode *Node) {
	n.children = append(n.children, childNode)
	childNode.parent = n
}

func (n *Node) getChild(childName string) *Node {
	for _, cn := range n.children {
		if cn.name == childName {
			return cn
		}
	}
	return nil
}

func (n *Node) getTotalSize() int {
	toVisit := []*Node{n}
	totalSize := 0
	for len(toVisit) != 0 {
		curNode := toVisit[0]
		toVisit = toVisit[1:]
		if curNode.filetype == FILE {
			totalSize += curNode.space
		} else {
			for _, cn := range curNode.children {
				toVisit = append(toVisit, cn)
			}
		}
	}
	return totalSize
}

func (n *Node) getAllDirs() []*Node {
	toVisit := []*Node{n}
	var allDirs []*Node
	for len(toVisit) != 0 {
		curNode := toVisit[0]
		toVisit = toVisit[1:]
		if curNode.filetype == DIR {
			allDirs = append(allDirs, curNode)
			for _, cn := range curNode.children {
				toVisit = append(toVisit, cn)
			}
		}
	}
	return allDirs
}

func day07() {
	lines := getLines("day07.txt")
	root := Node{0, "", DIR, []*Node{}, nil}
	curNode := &root
	for _, line := range lines {
		cmdParts := strings.Split(line, " ")
		switch cmdParts[0] {
		case "$":
			switch cmdParts[1] {
			case "cd":
				switch cmdParts[2] {
				case "/":
					fmt.Println("going up to the root")
					curNode = &root
				case "..":
					//fmt.Println("goint up one level")
					curNode = curNode.parent
				default:
					//fmt.Printf("getting into the directory %s\n", cmdParts[2])
					child := curNode.getChild(cmdParts[2])
					if child != nil {
						curNode = child
					} else {
						newNode := Node{0, cmdParts[2], DIR, nil, curNode}
						curNode.addChild(&newNode)
						curNode = &newNode
					}
				}
			case "ls":
				//fmt.Println("printing the contents")
			}
		case "dir":
			//fmt.Printf("need to add directory %s to current directory\n", cmdParts[1])
			child := curNode.getChild(cmdParts[1])
			if child == nil {
				newNode := Node{0, cmdParts[1], DIR, nil, curNode}
				curNode.addChild(&newNode)
			} else {
				fmt.Printf("directory %s already exists", cmdParts[1])
			}
		default:
			//fmt.Printf("need to add file %s to current directory\n", cmdParts[1])
			child := curNode.getChild(cmdParts[1])
			if child == nil {
				s, _ := strconv.Atoi(cmdParts[0])
				newNode := Node{s, cmdParts[1], FILE, nil, curNode}
				curNode.addChild(&newNode)
			} else {
				fmt.Printf("file %s already exists", cmdParts[1])
			}
	}
	}
	fmt.Println(root.getTotalSize())
	var sizes []int
	for _, d := range root.getAllDirs() {
		ss := d.getTotalSize()
		if ss >= 8381165 {
			sizes = append(sizes, ss)
		}
	}
	sort.Ints(sizes)
	fmt.Println(sizes)
}
