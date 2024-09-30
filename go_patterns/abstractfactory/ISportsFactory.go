package abstractfactory

import "fmt"


type ISportsFactory interface {
    makeShoe() IShoeProduct
    makeShirt() IShirtProduct
}

func GetSportsFactory(brand string) (ISportsFactory, error){

    if brand == "adidas" {
        return &Adidas{}, nil
    }

    if brand == "nike" {
        return &Nike{}, nil
    }


    return nil, fmt.Errorf("Wrong Brand")

}
