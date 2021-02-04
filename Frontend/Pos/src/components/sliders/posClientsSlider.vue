<template>
  <section class="q-py-md section bg-white" v-if="clients.length > 5">
    <pos-section-title title="Наши клиенты" class="q-mb-md"/>
    <splide :options="options">
      <splide-slide
        v-for="client in clients"
        :key="client.id"
      >
          <article>
            <div class="q-pa-sm border-radius-6">
              <q-img :src="client.logo" height="50px" contain :title="client.title" no-default-spinner>
                <template v-slot:loading><q-skeleton class="full-width" height="50px"/></template>
              </q-img>
            </div>
          </article>
      </splide-slide>
    </splide>
  </section>
</template>

<script>
import {Splide, SplideSlide} from '../../../node_modules/@splidejs/vue-splide';
import '../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';
import PosSectionTitle from "components/service/posSectionTitle";

export default {
  name: "posClientsSlider",
  components: {PosSectionTitle, Splide, SplideSlide},
  computed: {
    clients() {
      return this.$store.getters.getClients
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
