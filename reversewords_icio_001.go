package main
import (
	"fmt"
)
func main() {
	const sentence string = "i live and code"
	result := reverseWords(sentence)
	fmt.Println(result)
}

func reverseWords(sentence string) string {
	// O(N) time (linear scan through sentence) 
	// O(N) space (stored result)
	// N being the number of characters in the sentence string

	var result string
	end := len(sentence)
	for i := end - 1; i >= 0; i-- {
		if string(sentence[i]) == " " {
			result += sentence[i+1:end] + " "
			end = i
		}
	}
	return result + sentence[:end]
}
