<template>
<div>
  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide
      v-for="service in services"
      :key="service.id"
    >
      <pos-service-card :service="service"/>
    </swiper-slide>
  </swiper>

</div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import PosServiceCard from "components/services/posServiceCard";

export default {
  name: "posServicesSlider",
  components: {
    PosServiceCard,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  props: {
    services: {
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

<style scoped>

</style>
