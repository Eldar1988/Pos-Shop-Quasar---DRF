import { Notify } from 'quasar'

export default function addToWishList(product= {}) {
  let productInWish = false
  let wishList = []
  if (localStorage.getItem('wishList') === null) {
    wishList.push(product)
    localStorage.setItem('wishList', JSON.stringify(wishList))
    return null
  }
  else {
    wishList = JSON.parse(localStorage.wishList)
    wishList.forEach((item) => {
      if (item.id === product.id) {
        productInWish = true
        wishList.splice(wishList.indexOf(item), 1)
        Notify.create({message: `Товар ${product.title.toLowerCase()} удален из избранного`})
      }
    })
    if(!productInWish) {
      wishList.push(product)
      Notify.create({message: `Товар ${product.title.toLowerCase()} добавлен в избранное`, color: 'positive'})
    }
    localStorage.setItem('wishList', JSON.stringify(wishList))
  }
}
