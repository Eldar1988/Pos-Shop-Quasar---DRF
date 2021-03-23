<template>
<section>
  <pos-products-slider :products="products" />
</section>
</template>

<script>
import PosProductsSlider from "components/shop/posProductsSlider";
export default {
  name: "posRecommentedProducts",
  components: {PosProductsSlider},
  data() {
    return {
      products: []
    }
  },
  created() {
    this.loadProducts()
  },
  methods: {
    async loadProducts() {
      this.products = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_future_products/`)
      .then(({ data }) => {
        return data.results
      })
    }
  }
}
</script>

<style scoped>

</style>
