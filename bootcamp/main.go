package main

import "fmt"

//constantes
const string = "Curso Go"

func main() {

	var nombre string = "nombre"
	var edad int =25

	nombre2 := "nombre"
	edad2 := 5

	var altura = 1.67

	fmt.Println(nombre2, edad2, altura)
	fmt.Println(nombre2) 
	fmt.Println(edad2)
	fmt.Println(altura)

	fmt.Println("nombre:", nombre2, "edad:", edad2, "altura", altura)

	//variables multiples
	var nombre, apellido, pais string
	var nombre, apellido, pais = "daniel", "galvez", "mexico"
	nombre, apellido, pais := "daniel", "galvez", "mexico"
	edad, altura := 26, 1,69

	fmt.Println(nombre, apellido, pais, edad, alura)

	//constante se escribe dentro de la función
	fmt.Println(Curso)

	//Operadores Relacionales
	// <
	// >
	// >=
	// <=
	// ==
	// !=
	const pi = 3.1416

	fmt.Println(pi)
	var edad = 1
	var resultado = 5 > edad //bool
	
	var dog string
	dog = "perro"
	var gato string = "gato
	
	var ave, hamster string = "ave", 4
		
	persona := "persona
	
	// el := no sirve para reasignar el valor de la variable a menos que se agregue dentro de dos asignaciones siempre que una ya haya sido declarada

	fmt.Println(dog)
	fmt.Println(gato)
	fmt.Println(ave, hamster)
	fmt.Println(persona)

	fmt.Println(resultado)

}

// go build crea n archivo ejecutable
// para correr en terminal es go run main.go
