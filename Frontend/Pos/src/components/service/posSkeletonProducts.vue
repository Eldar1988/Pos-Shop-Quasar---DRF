<template>
  <!--    Product skeletons   -->
  <div class="product-wrapper">
    <article
      v-for="i in quantity"
      :key="i"
    >
      <pos-product-card-skeleton />
    </article>
  </div>
</template>

<script>
import PosProductCardSkeleton from "components/shop/posProductCardSkeleton";
export default {
  name: "posSkeletonProducts",
  components: {PosProductCardSkeleton},
  props: {
    quantity: {
      type: Number,
      default: 20
    }
  }
}
</script>

<style scoped>

</style>
