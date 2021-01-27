<template>
  <section class="q-pa-sm section" v-if="brands.length > 5">
    <splide :options="options">
        <splide-slide
          v-for="brand in brands"
          :key="brand.id"
        >
          <router-link :to="`/brand/${brand.slug}`">
          <article>
            <div class="q-pa-sm border-radius-6">
              <q-img :src="brand.image" height="50px" contain no-default-spinner>
                <template v-slot:loading><q-skeleton class="full-width" height="50px" /></template>
              </q-img>
            </div>
          </article>
          </router-link>
        </splide-slide>
    </splide>
  </section>
</template>

<script>
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide';
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';

export default {
  name: "posBrandsSlider",
  components: {Splide, SplideSlide},
  computed: {
    brands() {
      return this.$store.getters.getBrands
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
        navigation: false,
        pagination: false,
        autoplay: true,
        perPage: 7,
        breakpoints: {
          1600: {
            perPage: 6
          },
          1400: {
            perPage: 5
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

<style scoped>

</style>
