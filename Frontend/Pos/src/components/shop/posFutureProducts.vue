<template>
<div>
  <pos-products-wrapper  v-if="!productsUnloaded" :products="products"/>
  <pos-skeleton-products v-else/>
</div>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosSkeletonProducts from "components/service/posSkeletonProducts";
export default {
  name: "posFutureProducts",
  components: {PosSkeletonProducts, PosProductsWrapper},
  data() {
    return {
      products: [],
      productsUnloaded: false
    }
  },
  mounted() {
    this.loadFutureProducts()
  },
  methods: {
    async loadFutureProducts() {
      try {
        this.products = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/future_products/`)
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
        this.productsUnloaded ? this.loadFutureProducts() : clearInterval(reload)
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
