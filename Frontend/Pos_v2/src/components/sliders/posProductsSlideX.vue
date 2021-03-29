<template>
<div class="q-pa-sm" v-if="products">
  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide
      v-for="product in products"
      :key="product.id"
    >
      <pos-product-card :product="product"/>
    </swiper-slide>
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
        spaceBetween: 7,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
          disableOnInteraction: true,
        },
        // freeMode: true,
        breakpoints: {
          1600: {
            slidesPerView: 7.5,
          },
          1400: {
            slidesPerView: 6.5,
          },
          1279: {
            slidesPerView: 5.6,
          },
          1000: {
            slidesPerView: 4.3,
          },
          750: {
            slidesPerView: 4.3,
          },
          330: {
            slidesPerView: 2.3,
          }
        }
      }
    }
  },


}
</script>

<style lang="sass">
</style>
