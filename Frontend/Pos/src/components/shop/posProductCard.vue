<template>
  <q-card
    class="full-width border-radius-6 product-card relative-position"
    style="min-height: 100%"
  >
    <!--    Add to wish button   -->
    <q-btn
      :icon="productInWishList ? 'favorite' : 'favorite_border'"
      style="position: absolute; top:55px; right:8px;z-index:30"
      round flat
      color=""
      unelevated
      text-color="accent"
      @click="addToWishList(product)"
    >
      <q-tooltip>Добавить в избранное</q-tooltip>
    </q-btn>

    <q-btn
      color="accent"
      text-color="white"
      round
      icon="add_shopping_cart"
      unelevated
      @click="addToCart(product, 1, false)"
      style="position: absolute; z-index: 55; top:8px; right:8px;"
    >
      <q-tooltip>Добавить товар в корзину</q-tooltip>
    </q-btn>
    <!--    xxxxx   -->
    <router-link :to="`/product/${product.id}/`">
      <!--      Image   -->
      <div class="flex product-card-image" style="align-items: center;position: relative">
        <q-img
          :src="product.image"
          :contain="!product.image_contain"
          title="Подробнее"
          :height="`${this.$store.getters.getSiteSettings.productCardSettings.height}px` || `180`"
          style="max-height: 200px"
        >
          <template v-slot:loading>
            <q-skeleton class="product-card-image full-width"/>
          </template>
        </q-img>

        <!--      Rating   -->
        <div class="rating-wrapper">
          <q-rating v-model="product.rating" color="orange" size="18px" readonly/>
        </div>

        <!--      Sale      -->
        <q-btn
          v-if="product.old_price"
          color="primary"
          round
          :size="this.$q.platform.is.mobile ? 'sm' : 'md'"
          unelevated
          class="q-ma-sm"
          style="bottom: 0; position: absolute"
        >
          {{ getSalePercent }}
          <q-tooltip>Размер скидки</q-tooltip>
        </q-btn>
      </div>
    </router-link>
    <div class="product-meta">
      <!--      Product title   -->
      <router-link :to="`/product/${product.id}/`" title="Подробнее">
        <p class="product-card-title text-center ellipsis-2-lines">
          {{ product.title }}
        </p>
      </router-link>

      <!--      Product price   -->
      <div class="product-card-price-wrapper text-center text-positive">
        <p class="text-weight-bold product-card-price">
          {{ product.price|formatPrice }}
          <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
          <span class="old-price text-grey"> {{ product.old_price|formatPrice }} </span>
        </p>
      </div>
    </div>
  </q-card>
</template>

<script>
import formatPrice from "src/filters/format_price"
import addToCart from "src/functions/add_to_cart"
import addToWishListFunc from "src/functions/add_to_wishlist"
import addToWishList from "src/functions/add_to_wishlist";

export default {
  name: "posProductCard",
  props: {
    product: {
      type: Object,
      default: null,
    }
  },
  data() {
    return {
      productInWishList: false
    }
  },
  filters: {
    formatPrice
  },
  computed: {
    getSalePercent: function () {
      let percent = Math.round(100 - (this.product.price * 100 / this.product.old_price))
      return `-${percent}%`
    }
  },
  mounted() {
    this.$root.$on('updateWishList', () => {
      this.productInWishList = false
      this.checkWishList()
    })
    this.checkWishList()
  },
  methods: {
    addToCart(product, quantity, redirect) {
      addToCart(product, quantity)
      this.$root.$emit('updateCart')
      if (redirect) this.$router.push('/cart')
      else {
        this.$q.notify({message: `Товар ${product.title.toLowerCase()} добавлен в корзину`, color: 'positive'})
      }
    },
    addToWishList(product) {
      addToWishListFunc(product)
      this.$root.$emit('updateWishList')
    },
    async checkWishList() {
      if (localStorage.getItem('wishList') !== null) {
        let wishList = JSON.parse(localStorage.wishList)
        wishList.forEach((item) => {
          if (item.id === this.product.id) {
            this.productInWishList = true
          }
        })
      }
    },
  }

}
</script>

<style lang="sass">
.product-card-image
  height: 250px

.product-card
  position: relative
  transition: .5s all
  box-shadow: none


.product-meta
  padding: 5px 5px 15px

.product-card-title
  font-size: 16px
  font-weight: 700


.product-card-price
  font-size: 18px

.old-price
  font-size: 15px
  text-decoration: line-through

.rating-wrapper
  position: absolute
  bottom: 0
  left: 0
  right: 0
  text-align: center

.product-card-actions
  position: absolute
  bottom: 0
  left: 0
  right: 0
  padding: 5px
  display: grid
  grid-template-columns: 4fr 1fr
  grid-gap: 2px


@media screen and (max-width: 800px)
  .product-card-image
    height: 220px

  .scroll-x-products .product-card-image
    height: 300px !important
  .product-card-title
    font-size: 14px


</style>
