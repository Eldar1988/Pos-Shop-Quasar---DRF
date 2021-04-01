export default function addToCart(product = {}, quantity = 1, variations=[]) {
  let date = new Date
  product.timeID = date.getMilliseconds().toString() + date.getSeconds().toString()
  product.quantity = quantity
  product.variations = variations
  let cart = []
  if (localStorage.getItem('cart') === null) {
    localStorage.setItem('cart', JSON.stringify(cart))
  } else {
    cart = JSON.parse(localStorage.cart)
  }
  cart.push(product)
  localStorage.setItem('cart', JSON.stringify(cart))
}
