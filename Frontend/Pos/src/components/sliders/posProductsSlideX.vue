<template>
<div class="q-pa-sm">
  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide
      v-for="product in products"
      :key="product.id"
    >
      <pos-product-card :product="product"/>
    </swiper-slide>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
</div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import PosProductCard from "components/shop/posProductCard";

export default {
  name: "posProductsSlideX",
  components: {
    PosProductCard,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      swiperOptions: {
        slidesPerView: 3,
        spaceBetween: 10,
        // freeMode: true,
        breakpoints: {
          1600: {
            slidesPerView: 6.5,
          },
          1400: {
            slidesPerView: 4.5,
          },
          1279: {
            slidesPerView: 3.6,
          },
          1000: {
            slidesPerView: 3.3,
          },
          750: {
            slidesPerView: 3.3,
          },
          330: {
            slidesPerView: 1.8,
          }
        }
      }
    }
  },


}
</script>

<style lang="scss">
</style>
