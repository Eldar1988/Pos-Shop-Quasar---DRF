<template>
  <div>
    <div class="products-filters flex justify-between q-px-sm q-mt-md">
      <div>
        <q-btn
          label="Фильтры"
          color="dark"
          class="q-px-md text-bold"
          unelevated outline no-caps
          icon="tune"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "posFilters",
  props: {
    filters: {
      type: Array,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
