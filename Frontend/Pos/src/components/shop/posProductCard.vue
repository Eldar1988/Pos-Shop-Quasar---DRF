<template>
  <q-card
    class="grey-border full-width border-radius-6 product-card relative-position"
  >
    <!--    Add to wish button   -->
    <q-btn
      icon="favorite"
      style="position: absolute; top:10px; right:10px;z-index:30"
      flat round
    >
      <q-tooltip>Добавить в избранное</q-tooltip>
    </q-btn>
    <!--    xxxxx   -->
    <router-link :to="`/product/${product.slug}/`">
      <!--      Image   -->
      <q-img
        :src="product.image"
        contain
        class="product-card-image"
        title="Подробнее"
      >
        <template v-slot:loading>
          <q-skeleton class="product-card-image full-width"/>
        </template>
        <!--      Sale      -->
        <q-btn
          v-if="product.old_price"
          color="accent"
          round
          :size="this.$q.platform.is.mobile ? 'sm' : 'md'"
          unelevated
          class="q-ma-sm"
        >
          {{ getSalePercent }}
          <q-tooltip>Размер скидки</q-tooltip>
        </q-btn>
        <!--      Rating   -->
        <div class="rating-wrapper">
          <q-rating v-model="product.rating" color="orange" size="18px" readonly/>
        </div>
      </q-img>
    </router-link>
    <div class="product-meta">
      <!--      Product title   -->
      <router-link :to="`/product/${product.slug}/`" title="Подробнее">
        <p class="product-card-title text-center">
          {{ product.title }}
        </p>
      </router-link>

      <!--      Product price   -->
      <div class="product-card-price-wrapper text-center text-secondary">
        <p class="text-weight-bold product-card-price">
          {{ product.price|formatPrice }}
          <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
          <span class="old-price text-grey"> {{ product.old_price|formatPrice }} </span>
        </p>
      </div>

      <!--      Actions   -->
      <div class="product-card-actions">
        <q-btn
          label="В 1 клик"
          color="negative"
          icon="done_outline"
          size="sm"
          class="text-bold full-width border-radius-6"
          unelevated
        />
        <q-btn
          color="negative"
          size="sm"
          icon="add_shopping_cart"
          class="text-bold full-width border-radius-6"
          unelevated outline
        />
      </div>
    </div>

  </q-card>
</template>

<script>
import formatPrice from "src/filters/format_price";

export default {
  name: "posProductCard",
  props: {
    product: {
      type: Object,
      default: null
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
  }

}
</script>

<style lang="sass">
.product-card-image
  height: 300px

.product-card
  position: relative
  min-height: 100%
  transition: .5s all
  box-shadow: none

  &:hover
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px


.product-meta
  padding: 5px 5px 35px

.product-card-title
  font-size: 18px

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
    height: 200px

  .scroll-x-products .product-card-image
    height: 300px !important
  .product-card-title
    font-size: 14px


</style>
