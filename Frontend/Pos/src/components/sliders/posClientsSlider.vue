<template>
  <section class="q-py-md section bg-white" v-if="clients.length > 5">
    <pos-section-title title="Наши клиенты" class="q-mb-md"/>
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="client in clients"
        :key="client.id"
      >
        <div class="brand-wrapper">
          <article>
            <div class="q-pa-sm border-radius-6">
              <q-img :src="client.logo" height="50px" contain :title="client.title" no-default-spinner>
                <template v-slot:loading><q-skeleton class="full-width" height="50px"/></template>
              </q-img>
            </div>
          </article>
        </div>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </section>
</template>

<script>
import PosSectionTitle from "components/service/posSectionTitle";
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  name: "posClientsSlider",
  components: {
    PosSectionTitle,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  computed: {
    clients() {
      return this.$store.getters.getClients
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
            slidesPerView: 7.5,
          },
          1400: {
            slidesPerView: 5.5,
          },
          1279: {
            slidesPerView: 4.6,
          },
          1000: {
            slidesPerView: 4.3,
          },
          750: {
            slidesPerView: 3.7,
          },
          330: {
            slidesPerView: 2.8,
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
