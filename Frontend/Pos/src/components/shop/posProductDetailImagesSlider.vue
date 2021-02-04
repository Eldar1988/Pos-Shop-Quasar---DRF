<template>
  <q-carousel
    navigation-position="top"
    animated
    v-model="slide"
    navigation
    swipeable
    control-color="primary"
    infinite
    autoplay
    :fullscreen.sync="fullscreen"
    transition-prev="slide-right"
    transition-next="slide-left"
    @mouseenter="autoplay = false"
    @mouseleave="autoplay = true"
    class="product-detail-slider border-radius-6 shadow-lt"
  >
    <q-carousel-slide
      :name="0"
    >
      <q-img
        :src="image"
        class="product-detail-slider"
        ratio="1:1"
        :contain="!firstImageContain"
        :title="title" :alt="`Фото: ${title}`"
      >
        <template v-slot:loading>
          <q-skeleton class="full-width product-detail-slider" />
        </template>
      </q-img>

    </q-carousel-slide>
    <q-carousel-slide
      v-for="(image, index) in images"
      :key="index + 1"
      :name="index + 1"
    >
      <q-img
        :src="image.image"
        class="product-detail-slider"
        :contain="!image.contain"
        :title="title" :alt="`Фото: ${title}`"
      >
        <template v-slot:loading>
          <q-skeleton class="full-width product-detail-slider" />
        </template>
      </q-img>
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
export default {
  name: "posProductDetailImagesSlider",
  props: {
    image: {
      type: String,
      default: null
    },
    firstImageContain: {
      type: Boolean,
      default: true
    },
    images: {
      type: Array,
      default: null
    },
    title: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      slide: 0,
      fullscreen: false
    }
  },

}
</script>

<style lang="sass">
.product-detail-slider
  height: 700px

@media screen and (max-width: 1410px)
  .product-detail-slider
    height: 500px

@media screen and (max-width: 1200px)
  .product-detail-slider
    height: 600px

@media screen and (max-width: 992px)
  .product-detail-slider
    height: 670px

@media screen and (max-width: 800px)
  .product-detail-slider
    height: 600px

@media screen and (max-width: 650px)
  .product-detail-slider
    height: 400px
</style>
