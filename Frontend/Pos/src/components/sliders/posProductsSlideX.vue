<template>
<div>
  <splide :options="options" :slides="products">
    <splide-slide v-for="product in products" :key="product.id" style="padding: 5px">
      <pos-product-card :product="product"/>
    </splide-slide>
  </splide>
</div>
</template>

<script>
import { Splide, SplideSlide } from '../../../node_modules/@splidejs/vue-splide';
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';
import PosProductCard from "components/shop/posProductCard";

export default {
  name: "posProductsSlideX",
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  components: {
    PosProductCard,
    Splide,
    SplideSlide,
  },
  data() {
    return {
      options: {
        type   : 'loop',
        perPage: 5.6,
        arrows: false,
        pagination: false,
        breakpoints: {
          1650: {
            perPage: 4.7
          },
          1400: {
            perPage: 3.7
          },
          1100: {
            perPage: 2.7
          },
          650: {
            perPage: 1.7
          }
        }
      }
    }
  },


}
</script>

<style lang="sass">
.p-splide__slide.is-active
  background: #13c59d
  border-color: #13c59d
</style>
