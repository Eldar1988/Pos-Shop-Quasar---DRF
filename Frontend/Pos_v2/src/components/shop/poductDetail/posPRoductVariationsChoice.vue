<template>
  <div>
    <q-btn-dropdown
      :label="label"
      class="full-width"
      color="dark"
      stretch no-caps unelevated
    >
      <q-list separator>
        <q-item
          v-for="(variation, index) in variations"
          :key="index"
          clickable v-close-popup
          @click="setVariation(variation)"
        >
          <q-item-section>
            <q-item-label>{{ variation.value }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
export default {
  name: "posPRoductVariationsChoice",
  props: {
    variations: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      label: `Выберите ${this.variations[0].type.toLowerCase()}`
    }
  },
  methods: {
    setVariation(variation) {
      this.label = variation.type.toString() + ': ' + variation.value.toString()
      this.$emit('setVariation', variation)
    }
  }

}
</script>

<style scoped>

</style>
