<template>
  <div>
    {{ inner }}
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
import { Splide, SplideSlide } from '../../../node_modules/@splidejs/vue-splide';
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';
import PosProductCard from "components/shop/posProductCard";

export default {
  name: "posHotProductsSlider",
  components: {
    PosProductCard,
    Splide,
    SplideSlide
  },
  data() {
    return {
      options: {
        rewind : true,
        width  : '100%',
        gap    : '5px',
        type: 'loop',
        focus: 'center',
        clones: 1,
        fixedWidth: '280px',
        arrows: false,
        perPage: 4,
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
  computed: {
    products() {
      return this.$store.getters.getHitProducts
    },
    inner() {
      return innerWidth
    }
  },
  created() {
    this.slidesPerPage()
  },
  methods: {
    slidesPerPage() {
      if (innerWidth < 1000 && innerWidth > 650)  {
        this.perPage = 2
        console.log('2')
        console.log(this.perPage)
      } else if (innerWidth < 650) {
        console.log('1')
        this.perPage = 1
      } else {
        this.perPage = 3
      }
    }
  }
}
</script>

<style lang="sass">

</style>
