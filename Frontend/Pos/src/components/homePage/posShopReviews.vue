<template>
  <section class="q-pa-sm q-py-xl bg-grey-2" v-if="reviews.length > 2">
    <pos-section-title
      title="Отзывы наших покупателей"
      class="q-pb-lg"
    />
    <splide :options="options">
      <splide-slide
        v-for="review in reviews"
        :key="review.id"
      >
        <article>
          <q-card
            class="border-radius-6 grey-border shadow-0 text-center q-py-md q-px-sm"
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
      </splide-slide>
    </splide>
  </section>
</template>

<script>

import PosSectionTitle from "components/service/posSectionTitle";
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide';
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';

export default {
  name: "posShopReviews",
  components: {PosSectionTitle, Splide, SplideSlide},
  computed: {
    reviews() {
      return this.$store.getters.getShopReviews
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
        pagination: false,
        autoplay: true,
        perPage: 4,
        breakpoints: {
          1400: {
            perPage: 4
          },
          1280: {
            perPage: 3
          },
          1000: {
            perPage: 2
          },
          650: {
            perPage: 1
          }
        }
      },
    }
  },
}
</script>

<style scoped>

</style>
