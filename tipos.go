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
	//operadores de asignacón

	var a = 10
	fmt.Println(a)
	var b = 20
	b += 2
	fmt.Println(b)

	var c = 3
	c++

	fmt.Println(c)
	
	fmt.Printf("Tipo: %T, value: %v", a, a)

  	fmt.Println(4 == 4)
	fmt.Println(4 != 4)

	var age = 30
	fmt.Println(age >= 18 && age <= 60)
	fmt.Println("niño o viejo", age < 18 || age > 60)
	fmt.Println(!(3 == 3))
	
	fruit := "manzana"
	fmt.Printf("Tipo: %T, Valor: %v", fruit, fruit, &fruit)
	fruit := "manzana"
	var p *string
	p = &fruit
	fmt.Printf("Tipo: %T, Valor: %s, Direccion: %v", fruit, fruit, &fruit)
	fmt.Printf("Tipo: %T, Valor: %v", p, p)
	
	var food [3]string
	food[0] = "d"
	food[1] = "3"
	food[2] = "f"
	food[3] = "v"
	
	set := [7]string{"q", "d", "fd", "ds"...}

	
}
