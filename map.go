// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {

	animals := make(map[string]string)
	animals["cat"] = "gato"
	animals["dog"] = "perro"

	fmt.Println(animals)

	fruits := map[string]string{
		"apple":  "manzana",
		"banana": "platano",
	}

	fmt.Println(fruits)

	delete(fruits, "banana")
	fmt.Println(fruits)

}
