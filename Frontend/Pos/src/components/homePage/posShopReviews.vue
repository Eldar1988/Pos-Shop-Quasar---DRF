<template>
<section class="q-pa-sm q-py-xl">

</section>
</template>

<script>

export default {
  name: "posShopReviews",
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
