<template>
  <q-card
    class="grey-border border-radius-6 product-card"
  >
    <q-skeleton class="product-card-image" />
    <div class="product-meta">
      <!--      Product title   -->
      <p class="product-card-title text-center">
        <q-skeleton height="20px" class="q-my-sm" />
      </p>

      <!--      Product price   -->
      <div class="product-card-price-wrapper text-center text-secondary">
        <p class="text-weight-bold product-card-price">
          <q-skeleton width="50%" height="22px" class="q-my-sm q-mx-auto" />
        </p>
      </div>

      <!--      Actions   -->
      <div class="product-card-actions">
        <q-skeleton height="26px"/>
        <q-skeleton height="26px"/>
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
