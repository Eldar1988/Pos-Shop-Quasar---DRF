<template>
  <div>
    <div class="product-wrapper">
      <!--    Products   -->
      <article
        v-for="product in products"
        :key="product.id"
      >
        <pos-product-card :product="product"/>
      </article>
    </div>
  </div>
</template>

<script>
import PosProductCard from "components/shop/posProductCard";

export default {
  name: "posProductsWrapper",
  components: {PosProductCard},
  props: {
    products: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.product-wrapper
  display: grid
  grid-template-columns: repeat(6, 1fr)
  grid-gap: 10px
  overflow-y: hidden

@media screen and (max-width: 1455px)
  .product-wrapper
    grid-template-columns: repeat(6, 1fr)

@media screen and (max-width: 1380px)
  .product-wrapper
    grid-template-columns: repeat(5, 1fr)

@media screen and (max-width: 1100px)
  .product-wrapper
    grid-template-columns: repeat(4, 1fr)

@media screen and (max-width: 650px)
  .product-wrapper
    grid-template-columns: repeat(2, 1fr)
    grid-gap: 5px
</style>
