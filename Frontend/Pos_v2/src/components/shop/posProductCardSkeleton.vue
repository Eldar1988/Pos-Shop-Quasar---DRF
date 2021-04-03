<template>
  <q-card
    square
    class="grey-border product-card"
  >
    <q-skeleton class="product-card-image" style="min-height: 200px" square/>
    <div class="product-meta">
      <!--      Product title   -->
      <p class="product-card-title text-center">
        <q-skeleton height="20px" square style="max-width: 80%; margin: 8px auto"/>
      </p>

      <!--      Product price   -->
      <div class=" ">
          <q-skeleton width="50%" height="22px" style="" />
      </div>
    </div>

  </q-card>
</template>

<script>
export default {
  name: "posProductCardSkeleton"
}
</script>

<style scoped>

</style>
