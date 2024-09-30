package abstractfactory

type Adidas struct {
}

func (a *Adidas) makeShoe() IShoeProduct {
    return &AdidasShoe{

        Shoe: Shoe{
            logo: "aidas",
            size: 14,
        },
    }
}

func (a *Adidas) makeShirt() IShirtProduct{
        return &AdidasShirt{
        Shirt: Shirt{
            logo: "adidas",
            size: 14,
        },
   }
}
