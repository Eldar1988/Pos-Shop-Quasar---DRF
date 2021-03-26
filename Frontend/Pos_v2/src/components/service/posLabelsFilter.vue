<template>
  <div>

  </div>
</template>

<script>
export default {
  name: "posLabelsFilter",
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      labels: []
    }
  },
  async mounted() {
    // Получение меток из продуктов
    let labels = []
    setTimeout(() => {
      this.products.forEach(item => {
        item.labels.forEach(item => {
          labels.push(item.title)
        })
      })
      let labelsSet = new Set(labels)
      let labelsCleanArr = Array.from(labelsSet)
      this.labels = labelsCleanArr
    }, 1000)
  }
}
</script>

<style lang="sass">

</style>
