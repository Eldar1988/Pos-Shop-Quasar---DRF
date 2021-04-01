<template>
<div>
<div
  v-if="sortedVariations.length > 0"
  class="q-mt-md"
>
  <div class="row">
    <div
      v-for="(variation, index) in sortedVariations"
      :key="index"
      class="col-md-6 col-12 q-pa-sm"
    >
      <pos-p-roduct-variations-choice :variations="variation" @setVariation="setVariation"/>
    </div>
  </div>
</div>
</div>
</template>

<script>
import PosPRoductVariationsChoice from "components/shop/poductDetail/posPRoductVariationsChoice";
export default {
  name: "posProductVariarions",
  components: {PosPRoductVariationsChoice},
  props: {
    variations: {
      type: Array,
      default: null,
    }
  },
  data() {
    return {
      sortedVariations: [],
      selectedVariations: []
    }
  },
  mounted() {
    this.getVariationCategories()
  },
  watch: {
    '$route'() {
      this.selectedVariations = []
      this.getVariationCategories()
    }
  },
  methods: {
    getVariationCategories() {
      // Получение всех тпиов вариаций в массив
      let types = []
      this.variations.forEach(item => {
        types.push(item.type)
      })
      // Массив с уникальными типами вариаций
      let typesSet = new Set(types)
      let uniqueTypes = Array.from(typesSet)
      let sortedVariations = []

      // Массив с сортрованными массивами вариаций
      uniqueTypes.forEach(type => {
        let sortedVariationsItem = []
        this.variations.forEach(item => {
          if (item.type === type) {
            sortedVariationsItem.push(item)
          }
        })
        sortedVariations.push(sortedVariationsItem)
      })
      this.sortedVariations = sortedVariations
    },
    setVariation(variation) {
      if(variation.price && variation.price > 0) this.$emit('setVariationPrice', variation.price)
      let variationTypeSelected = false
      if (this.selectedVariations.length === 0) {
        this.selectedVariations.push(variation)
        this.checkVariations(this.selectedVariations.length, this.sortedVariations.length)
        return
      }
      else {
        this.selectedVariations.forEach(item => {
          if (item.type === variation.type) {
            variationTypeSelected = true
          }
        })
      }
      if (!variationTypeSelected) this.selectedVariations.push(variation)
      this.checkVariations(this.selectedVariations.length, this.sortedVariations.length)
    },

    checkVariations(variations, selectedVariations) {
      if(variations === selectedVariations) this.$emit('setSelectedVariations', this.selectedVariations)
    }
  }
}
</script>

<style scoped>

</style>
