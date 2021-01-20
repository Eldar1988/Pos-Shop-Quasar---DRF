<template>
  <div>
    <q-page>
      <pos-section-title class="q-mt-lg" title="Ваша корзина"/>
      <section v-if="products.length > 0" class="q-px-sm q-mt-lg">
        <div class="cart-wrapper">
          <div class="cart-items ">
            <pos-cart-item
              v-for="product in products"
              :key="product.id"
              :product="product"
            />
            <p class="text-subtitle1 text-bold q-pt-sm">Всего товаров: {{ cartLen }}</p>
            <p class="text-subtitle1 text-bold">На сумму: {{ cartSum|formatPrice }}
              <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
            </p>
          </div>
          <div class="cart-form">
            <pos-checkout-form :cartSum="cartSum" :cartLen="cartLen" :products="products"/>
          </div>
        </div>
      </section>
      <!--    Empty cart alert   -->
      <section
        v-if="products.length === 0"
        class="q-px-sm"
      >
        <q-card
          class="bg-negative red-shadow q-px-sm q-py-xl flex flex-center q-mt-lg"
        >
          <div class="text-center">
            <p class="text-subtitle1 text-white">
              Ваша корзина пуста.
            </p>
            <q-btn
              label="вернуться в магазин"
              outline
              color="white"
              class="border-radius-6 q-mt-md text-bold"
              to="/"
            />
          </div>
        </q-card>
      </section>
      <!--    xxxxx   -->
    </q-page>
    <pos-banners/>
  </div>
</template>

<script>
import PosCartItem from "components/cart/posCartItem";
import PosSectionTitle from "components/service/posSectionTitle";
import formatPrice from "src/filters/format_price";
import PosCheckoutForm from "components/cart/posCheckoutForm";
import PosBanners from "components/shop/posBanners";

export default {
  name: "Cart",
  components: {PosBanners, PosCheckoutForm, PosSectionTitle, PosCartItem},
  filters: {formatPrice},
  data() {
    return {
      products: [],
      cartSum: 0,
      cartLen: 0
    }
  },
  mounted() {
    this.getCartProducts()
    this.getCartSum()
    this.$root.$on('updateCart', () => {
      this.getCartProducts()
      this.getCartSum()
    })
  },
  methods: {
    getCartProducts() {
      this.products = JSON.parse(localStorage.cart)
    },
    getCartSum() {
      let sum = 0
      let cartLen = 0
      this.products.forEach((item) => {
        let itemSum = item.quantity * item.price
        sum += itemSum
        cartLen += item.quantity
      })
      this.cartSum = sum
      this.cartLen = cartLen
    }
  }
}
</script>

<style lang="sass">
.cart-wrapper
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 7px

@media screen and (max-width: 800px)
  .cart-wrapper
    grid-template-columns: 1fr
</style>
