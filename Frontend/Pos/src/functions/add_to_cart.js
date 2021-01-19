export default function addToCart(product= {}, quantity=1) {
  let productInCart = false
  product.quantity = quantity
  let cart = []
  if (localStorage.getItem('cart') === null) {
    cart.push(product)
    localStorage.setItem('cart', JSON.stringify(cart))
    return null
  }
  else {
    cart = JSON.parse(localStorage.cart)
    cart.forEach((item) => {
      if (item.title === product.title) {
        item.quantity += quantity
        productInCart = true
      }
    })
    if(!productInCart) {
      cart.push(product)
    }
    localStorage.setItem('cart', JSON.stringify(cart))
  }
}
