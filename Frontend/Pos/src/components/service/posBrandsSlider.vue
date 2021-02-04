<template>
  <section class="q-pa-sm section bg-white" v-if="brands.length > 5">

  </section>
</template>

<script>

export default {
  name: "posBrandsSlider",
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
        perPage: 6,
        breakpoints: {
          1600: {
            perPage: 5
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
