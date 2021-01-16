<template>
<div>
  <pos-products-wrapper v-if="!productsUnloaded" :products="products" />
  <pos-skeleton-products v-else />
</div>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosSkeletonProducts from "components/service/posSkeletonProducts";
export default {
  name: "posSaleProducts",
  components: {PosSkeletonProducts, PosProductsWrapper},
  data() {
    return {
      products: [],
      productsUnloaded: false
    }
  },
  mounted() {
    this.loadSaleProducts()
  },
  methods: {
    async loadSaleProducts() {
      try {
        this.products = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_sale_products/`)
        .then(({data}) => {
          return data.results
        })
      }
      catch (e) {
        this.productsUnloaded = true
      }
    },
    reloadSaleProducts() {
      let reload = setInterval(() => {
        this.productsUnloaded ? this.loadSaleProducts() : clearInterval(reload)
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
