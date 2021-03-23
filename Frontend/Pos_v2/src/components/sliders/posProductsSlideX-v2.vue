<template>
  <div>
    <div class="products-slide-grid">
      <div
        v-for="product in products"
        :key="product.id"
      >
        <div class="card-wrapper">
          <pos-product-card :product="product"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PosProductCard from "components/shop/posProductCard";

export default {
  name: "posProductsSlideX-v2",
  components: {PosProductCard},
  props: {
    products: {
      type: Array,
      default: null
    }
  },
}
</script>

<style lang="sass">
.products-slide-grid
  display: grid
  grid-template-columns: repeat(6, 1fr)
  grid-gap: 10px
  padding: 10px

@media screen and (max-width: 1444px)
  .products-slide-grid
    grid-template-columns: repeat(5, 1fr)

@media screen and (max-width: 1400px)
  .products-slide-grid
    grid-template-columns: repeat(4, 1fr)

@media screen and (max-width: 1100px)
  .products-slide-grid
    grid-template-columns: repeat(3, 1fr)

@media screen and (max-width: 992px)
  .products-slide-grid
    display: flex
    flex-wrap: nowrap
    overflow-x: scroll
    justify-content: start
    margin-left: 5px
    padding: 0
    grid-gap: 0

    .card-wrapper
      min-width: 220px
      width: 220px
      padding: 5px
</style>
