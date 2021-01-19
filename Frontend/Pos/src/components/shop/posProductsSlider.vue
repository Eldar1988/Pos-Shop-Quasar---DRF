<template>
  <div class="q-pa-sm" v-if="products">
    <splide :options="options">
      <splide-slide
        v-for="product in products"
        :key="product.id"
      >
        <pos-product-card :product="product" />
      </splide-slide>
    </splide>
  </div>
</template>

<script>
import PosProductCard from "components/shop/posProductCard"
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide'
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css'

export default {
  name: "posProductsSlider",
  components: {PosProductCard, Splide, SplideSlide},
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      options: {
        rewind: true,
        width: '100%',
        gap: '5px',
        type: 'loop',
        arrows: false,
        perPage: 5,
        breakpoints: {
          1400: {
            perPage: 3
          },
          1000: {
            perPage: 3
          },
          650: {
            perPage: 2
          }
        }
      },
    }
  },
}
</script>

<style lang="sass">
.splide
  padding: 0

.splide__pagination
  bottom: -2em

.splide__pagination__page.is-active
  background: $accent
</style>
