<template>
  <q-card
    class="full-width product-card relative-position bg-white"
    style="min-height: 100%"
    square
  >
    <!--    Add to wish button   -->
    <q-btn
      :icon="productInWishList ? 'favorite' : 'favorite_border'"
      style="position: absolute; top:0; right:0;z-index:30"
      round flat
      color=""
      unelevated
      text-color="accent"
      @click="addToWishList(product)"
    >
      <q-tooltip>Добавить в избранное</q-tooltip>
    </q-btn>

    <router-link :to="`/product/${product.id}/`">
      <!--      Image   -->
      <div
        :class="!product.image_contain ? `flex product-card-image q-pa-sm` : `flex product-card-image`"
        style="align-items: center;position: relative"
      >
        <q-img
          :src="product.image || product.miniature_url"
          :contain="!product.image_contain"
          title="Подробнее"
          :height="`${this.$store.getters.getSiteSettings.productCardSettings.height}px` || `200`"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width" height="170px" square/>
          </template>
        </q-img>
        <!--      Rating   -->
        <div class="rating-wrapper">
          <q-rating v-model="product.rating" color="orange" size="14px" readonly/>
        </div>
      </div>
    </router-link>
    <div class="product-meta">

      <!--      Sale      -->
      <q-btn
        v-if="product.old_price"
        color="accent"
        flat dense
        unelevated disable padding="0"
        class="q-ma-sm"
        style="bottom: -4px; left: 0; position: absolute"
      >
        {{ getSalePercent }}
        <q-tooltip>Размер скидки</q-tooltip>
      </q-btn>

      <!--      Product title   -->
      <router-link :to="`/product/${product.id}/`" title="Подробнее">
        <p class="product-card-title text-center ellipsis-2-lines">
          {{ product.title }}
        </p>
      </router-link>

      <!--      Product price   -->
      <div v-if="product.price" class="product-card-price-wrapper text-right text-positive">
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
import addToWishListFunc from "src/functions/add_to_wishlist"

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

.product-card
  position: relative
  transition: .3s all
  box-shadow: none
  &:hover
    z-index: 150
    box-shadow: 0px 0px 10px 0 rgba(0,0,0,.03)

.product-meta
  padding: 5px 5px 5px

.product-card-title
  font-size: 15px
  font-weight: 700
  height: 40px


.product-card-price
  font-size: 16px
  padding-top: 5px

.old-price
  font-size: 13px
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

  .product-card-title
    font-size: 13px

  .product-card-price
    font-size: 15px
    padding-top: 5px

  .old-price
    font-size: 11px
    text-decoration: line-through


</style>
