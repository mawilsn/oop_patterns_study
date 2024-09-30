package abstractfactory

type Nike struct {
}

func (a *Nike) makeShoe() IShoeProduct {
    return &NikeShoe{

        Shoe: Shoe{
            logo: "aidas",
            size: 14,
        },
    }
}

func (a *Nike) makeShirt() IShirtProduct{
        return &NikeShirt{
        Shirt: Shirt{
            logo: "adidas",
            size: 14,
        },
    }
}
