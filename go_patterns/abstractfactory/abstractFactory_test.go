package abstractfactory

import "testing"



func TestShoe(t *testing.T){

    adidasFactory, _ := GetSportsFactory("adidas")
    adidasShoe := adidasFactory.makeShoe()

    if adidasShoe.getLogo() != "adidas" {

        t.Fatal("Expexted Logo: adidas, Recieved Logo: %s", adidasShoe.getLogo())
    }

    if adidasShoe.getSize() != 14{
        t.Fatal("Expexted Size: 14, Received Size: %s", adidasShoe.getSize())
    } 

}
