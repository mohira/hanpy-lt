package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	wg.Add(1)
	go func() {
		fmt.Println("（っ'-')╮  Hello from Goroutine")
		wg.Done()
	}()

	wg.Wait()

	fmt.Println("∠( ﾟдﾟ)／ Hello from Main Goroutine")
	fmt.Println("Main done")
}
