package main
import (
	"fmt"
	"bytes"
	"strings"
)
func main() {
	const sentence string = "i live and code"
	result := reverseWords(sentence)
	fmt.Println(result)
	result = reverseWords_BytesBuffer(sentence)
	fmt.Println(result)
	result = reverseWords_StringBuilder(sentence)
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

func reverseWords_BytesBuffer(sentence string) string {
	// More efficient way to concantinate strings than reverseWords
	// instead of `result +=` which creates strings everytime
	// we instead should use bytes buffer
	var result bytes.Buffer
	end := len(sentence)
	for i := end - 1; i >= 0; i-- {
		if string(sentence[i]) == " " {
			result.WriteString(sentence[i+1:end])
			result.WriteString(" ")
			end = i
		}
	}
	result.WriteString(sentence[:end])
	return result.String()
}

func reverseWords_StringBuilder(sentence string) string {
	// Also a more efficient way to concantinate strings than reverseWords
	// instead of `result +=` which creates strings everytime
	// we instead should use strings.Builder (for Go 1.10+)
	var result strings.Builder
	end := len(sentence)
	for i := end - 1; i >= 0; i-- {
		if string(sentence[i]) == " " {
			result.WriteString(sentence[i+1:end])
			result.WriteString(" ")
			end = i
		}
	}
	result.WriteString(sentence[:end])
	return result.String()
}