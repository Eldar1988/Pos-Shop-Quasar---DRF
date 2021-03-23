<template>
  <section class="q-pa-sm q-py-xl" v-if="reviews.length > 2">
    <pos-section-title
      title="Отзывы наших покупателей"
      class="q-pb-lg"
    />
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="review in reviews"
        :key="review.id"
      >
        <div class="review-card-wrapper">
          <article>
            <q-card
              square
              class="shadow-0 text-center q-py-md q-px-md"
              style="height: 300px; overflow-y: scroll"
            >
              <q-img
                :src="review.avatar"
                height="100px"
                width="100px"
                class="block q-mx-auto" img-class="circle-image"
              >
                <template v-slot:loading>
                  <q-skeleton height="100px" width="100px" class="circle-image"/>
                </template>
              </q-img>
              <q-rating
                v-model="review.rating"
                color="orange"
                class="q-py-sm"
              />
              <p class="review-name text-bold">
                {{ review.name }}
              </p>
              <p class="review-text q-pt-sm">
                {{ review.text }}
              </p>
            </q-card>
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
  name: "posShopReviews",
  components: {
    PosSectionTitle,
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  computed: {
    reviews() {
      return this.$store.getters.getShopReviews
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
            slidesPerView: 4.5,
          },
          1400: {
            slidesPerView: 3.7,
          },
          1279: {
            slidesPerView: 3.6,
          },
          1000: {
            slidesPerView: 3.3,
          },
          750: {
            slidesPerView: 2.7,
          },
          330: {
            slidesPerView: 1.3,
          }
        }
      }
    }
  },
}
</script>

<style lang="sass">
.reviews-slide-grid
  display: flex
  justify-content: center
  align-items: center
  flex-wrap: wrap

  .review-card-wrapper
    min-width: 300px
    width: 300px
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
  .reviews-slide-grid
    flex-wrap: nowrap
    overflow-x: scroll
    justify-content: start

    .review-card-wrapper
      min-width: 250px
      width: 250px
      padding: 5px
</style>
