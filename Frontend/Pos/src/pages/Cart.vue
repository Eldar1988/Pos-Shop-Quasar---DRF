<template>
  <div>
    <q-page>
      <q-breadcrumbs class="q-pa-sm q-mt-md">
        <q-breadcrumbs-el icon="home" to="/"/>
        <q-breadcrumbs-el label="Корзина"/>
      </q-breadcrumbs>
      <pos-section-title class="q-mt-lg" title="Ваша корзина"/>
      <section v-if="products.length > 0" class="q-px-sm q-mt-lg">
        <div class="cart-wrapper">

          <!--          Cart items   -->
          <div class="cart-items q-mt-md">
            <pos-cart-item
              v-for="product in products"
              :key="product.id"
              :product="product"
            />
            <div class="bg-dark text-white q-px-md border-radius-6 q-py-md q-mt-md">
              <p class="text-subtitle1 text-bold">Всего товаров: {{ cartLen }}</p>
              <p class="text-subtitle1 text-bold">На сумму: {{ cartSum|formatPrice }}
                <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
              </p>
            </div>
          </div>
          <!--          xxxxx   -->
          <!--          Cart form   -->
          <div class="cart-form q-mt-md">
            <pos-checkout-form :cartSum="cartSum" :cartLen="cartLen" :products="products"/>
          </div>
          <!--          xxxxx   -->
        </div>
      </section>
      <!--    Empty cart alert   -->
      <section
        v-if="products.length === 0"
        class="q-px-sm"
      >
        <q-card
          class="bg-negative red-shadow q-px-sm q-py-xl flex flex-center q-mt-lg border-radius-6"
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
      <div class="q-pt-xl">
        <pos-banners class=""/>
      </div>

    </q-page>

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
      if (localStorage.getItem('cart') !== null) {
        this.products = JSON.parse(localStorage.cart)
      } else {
        return null
      }
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
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Корзина | ${siteTitle}`,
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
