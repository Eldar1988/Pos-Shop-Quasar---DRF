<template>
  <section class="q-py-md bg-white" v-if="brands.length > 3">
      <swiper class="swiper" :options="swiperOptions">
        <swiper-slide
          v-for="brand in brands"
          :key="brand.id"
        >
          <div>
          <router-link :to="`/brand/${brand.slug}`">
            <article>
              <div class="q-pa-sm border-radius-6">
                <q-img :src="brand.image" height="50px" contain no-default-spinner>
                  <template v-slot:loading>
                    <q-skeleton class="full-width" height="50px"/>
                  </template>
                </q-img>
              </div>
            </article>
          </router-link>
          </div>
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
  </section>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  name: "posBrandsSlider",
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  computed: {
    brands() {
      return this.$store.getters.getBrands
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

<style lang="sass">
.brands-slide-grid
  display: flex
  justify-content: center
  align-items: center
  flex-wrap: wrap

  .brand-wrapper
    min-width: 150px
    width: 150px
    padding: 5px

//@media screen and (max-width: 1444px)
//  .brands-slide-grid
//    grid-template-columns: repeat(5, 1fr)
//
//@media screen and (max-width: 1400px)
//  .brands-slide-grid
//    grid-template-columns: repeat(4, 1fr)
//
//@media screen and (max-width: 1100px)
//  .brands-slide-grid
//    grid-template-columns: repeat(3, 1fr)

@media screen and (max-width: 992px)
  .brands-slide-grid
    flex-wrap: nowrap
    overflow-x: scroll
    justify-content: start
    margin-left: 5px

    .brand-wrapper
      min-width: 150px
      width: 150px
      padding: 5px
</style>
