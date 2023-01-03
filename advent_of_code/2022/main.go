package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
)

func getLines(filename string) []string {
	absPath, _ := filepath.Abs("./" + filename)
	readFile, err := os.Open(absPath)
	if err != nil {
		fmt.Println(err)
		return nil
	}
	defer func() {
		err = readFile.Close()
		if err != nil {
			fmt.Println(err)
		}
	}()

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	var lines []string
	for fileScanner.Scan() {
		lines = append(lines, fileScanner.Text())
	}
	return lines
}

func getMax(numbers []int) int {
	result := numbers[0]
	for _, elem := range numbers {
		if elem > result {
			result = elem
		}
	}
	return result
}

func main() {
	day13()
}