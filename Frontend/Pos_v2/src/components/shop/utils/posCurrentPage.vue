<template>
  <div class="q-px-sm text-right">
    <small>{{ `Страница ${currentPage} из ${(Math.ceil(productsCount/30))}`  }}</small>
  </div>
</template>

<script>
export default {
  name: "posCurrentPage",
  props: {
    currentPage: {
      type: Number,
      default: 0
    },
    productsCount: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style scoped>

</style>
