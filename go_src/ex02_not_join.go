package main

import "fmt"

func main() {
	// Goroutine(ゴルーチン/ゴールーチン)は、ここでは、おおよそスレッドと同じものを考えて問題ないです
	go func() {
		fmt.Println("Hello from Goroutine")
	}()

	// 先にMainGoroutineが終了してしまう(可能性が高い)
	fmt.Println("Hello from Main Goroutine")
	fmt.Println("Main done")
}