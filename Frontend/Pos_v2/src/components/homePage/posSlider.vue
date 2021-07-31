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
      class="home-slider shadow-lt"
    >
      <q-carousel-slide
        v-for="(slide, index) in slider.slides"
        :key="index"
        :name="index"
      >
        <router-link :to="slide.url">
        <q-img
          :src="slide.image"
          :contain="slide.contain"
          class="home-slider"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width home-slider" square/>
          </template>
          <div v-if="slide.title || slide.btn_text" class="slider-meta">
            <div class="text-center slider-meta-content">
              <h2 v-if="slide.title" class="q-mb-md" style="line-height: .5">
              <span class="slider-meta-content-text">
              {{ slide.title }}
                </span>
              </h2>
              <q-btn
                v-if="slide.btn_text"
                :label="slide.btn_text"
                color="accent"
                class="q-px-lg text-bold"
                :to="slide.url"
                unelevated
                no-caps
              />
            </div>
          </div>
        </q-img>
        </router-link>
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
  height: 70vh
.q-carousel .q-carousel__thumbnail
  height: 30px !important
.slider-meta
  position: absolute
  bottom: 0
  left: 0
  right: 0

.slider-meta-content
  background: rgba(0,0,0,.7)
  padding: 15px 5px

.slider-meta-content-text
  color: white
  font-size: 22px
  font-weight: 700
  line-height: 1.1 !important


@media screen and (max-width: 1280px)
  .home-slider
    height: 60vh

@media screen and (max-width: 650px)
  .home-slider
    height: 250px

  .slider-meta-content
    background: rgba(0,0,0,.7)

  .slider-meta-content-text
    font-size: 14px
    font-weight: 700
</style>
