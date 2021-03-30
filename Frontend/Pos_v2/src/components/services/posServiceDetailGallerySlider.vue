<template>
<div>
  <q-carousel
    navigation-position="top"
    animated
    swipeable
    v-model="slide"
    navigation
    infinite
    :autoplay="true"
    arrows
    transition-prev="slide-right"
    transition-next="slide-left"
    @mouseenter="autoplay = false"
    @mouseleave="autoplay = true"
    class="shadow-lt service-slider-image"
  >
    <q-carousel-slide
      v-for="(image, index) in images"
      :key="index"
      :name="index"
      :img-src="image.image"
    />
  </q-carousel>
</div>
</template>

<script>
export default {
  name: "posServiceDetailGallerySlider",
  props: {
    images: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
@media screen and (max-width: 650px)
  .service-slider-image
    height: 270px
</style>
