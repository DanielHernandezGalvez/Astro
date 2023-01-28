package main

import "fmt"

func main() {
  
  var a rune = -100
  
  var b rune = "a"
	c := uint16(a) + b
	var a bool = true
	_ := 234 //asi le digo que no la usaré ero no la borraré
	var _ string = "test" // igual que arriba
	
	var a string //el valor asignado es igual a 0
	
	fmt.Printf("Tipo: %T, value: %v", a, a)

  
}
