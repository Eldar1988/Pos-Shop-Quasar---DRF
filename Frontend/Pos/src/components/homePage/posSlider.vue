<template>
  <section class="q-px-sm">
    <q-carousel
      v-if="!serverUnloadedStatus"
      navigation-position="top"
      animated
      swipeable
      v-model="slide"
      :navigation="slider.dots"
      infinite
      :autoplay="slider.autoplay"
      :arrows="slider.arrows"
      transition-prev="slide-right"
      transition-next="slide-left"
      @mouseenter="autoplay = false"
      @mouseleave="autoplay = true"
      class="home-slider border-radius-6 shadow-lt"
    >
      <q-carousel-slide
        v-for="(slide, index) in slider.slides"
        :key="index"
        :name="index"
      >
        <q-img
          :src="slide.image"
          :contain="slide.contain"
          class="home-slider"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width home-slider" />
          </template>
          <div class="slider-meta">
            <div class="text-center">
              <h2 v-if="slide.title" class="q-mb-md">
              <span class="slider-meta-content border-radius-6">
              {{ slide.title }}
                </span>
              </h2>
              <q-btn
                v-if="slide.btn_text"
                :label="slide.btn_text"
                color="accent"
                class="text-weight-bold q-my-sm q-px-md border-radius-6"
                icon-right="keyboard_arrow_right"
                :to="slide.url"
                unelevated
              />
            </div>
          </div>
        </q-img>

      </q-carousel-slide>
    </q-carousel>
    <q-skeleton
      v-if="serverUnloadedStatus"
      class="home-slider full-width"
    />
  </section>
</template>

<script>
export default {
  name: "posSlider",
  data() {
    return {
      slide: 0,
    }
  },
  computed: {
    slider() {
      return this.$store.getters.getHomeSlider
    },
    serverUnloadedStatus() {
      return this.$store.getters.getServerStatus
    }
  }
}
</script>

<style lang="sass">
.home-slider
  height: 50vh
.q-carousel .q-carousel__thumbnail
  height: 30px !important
.slider-meta
  position: absolute
  bottom: 10px
  left: 10px
  right: 10px

.slider-meta-content
  background: rgba(0,0,0,.7)
  color: white
  font-size: 22px
  font-weight: 700
  padding: 7px 25px

@media screen and (max-width: 1280px)
  .home-slider
    height: 400px

@media screen and (max-width: 650px)
  .home-slider
    height: 250px

  .slider-meta-content
    background: rgba(0,0,0,.7)
    color: white
    font-size: 14px
    font-weight: 700
    padding: 7px 25px
</style>
