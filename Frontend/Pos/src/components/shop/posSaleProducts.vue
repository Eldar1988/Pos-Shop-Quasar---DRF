<template>
<div>
  <pos-products-wrapper :products="products" />
</div>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
export default {
  name: "posSaleProducts",
  components: {PosProductsWrapper},
  computed: {
    products() {

      return this.$store.getters.getSaleProducts
    }
  },
  created() {
    this.$store.dispatch('loadSaleProducts')
  }
}
</script>

<style scoped>

</style>
