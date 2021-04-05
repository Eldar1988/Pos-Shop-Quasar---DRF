<template>
  <div>
    <div class="products-filters flex justify-between q-px-sm q-mt-md">
      <div>
        <q-btn
          label="Фильтры"
          color="dark"
          class="q-px-md text-bold"
          unelevated outline no-caps stretch
          icon="tune"
          @click="filtersCard = !filtersCard"
        />
        <q-btn
          v-if="resetFiltersBtn"
          label="Сбросить фильтры"
          flat stretch dense no-caps
          class="q-ml-sm"
          icon="close"
          color="accent"
          size="sm"
          @click="resetFilters(true)"
        />
      </div>
    </div>

      <q-dialog
        v-model="filtersCard"
        class="q-pa-sm">
      <q-card
        square
        style="width: 700px; max-width: 100%"
        class="shadow-0"
      >
        <q-toolbar class="bg-dark text-white">
          <q-toolbar-title>Фильры</q-toolbar-title>
          <q-btn icon="close" flat dense v-close-popup/>
        </q-toolbar>
        <q-card-section>
        <div class="row">
          <div
            class="col-12"
          ><p class="text-bold">Цена:</p>
            <div class="row q-mt-sm">
              <div class="col-6 q-pa-sm">
                <q-input v-model="minPrice" outlined square label="От" type="number"/>
              </div>
              <div class="col-6 q-pa-sm">
                <q-input v-model="maxPrice" outlined square label="До" type="number"/>
              </div>
            </div>

          </div>
          <div
            v-for="filter in filters"
            :key="filter.id"
            class="col-sm-6 col-12 q-mt-md"
          >
            <p class="text-bold">{{ filter.title }}:</p>
            <q-checkbox
              v-model="SelectedCharacteristics"
              v-for="characteristic in filter.characteristics"
              :key="characteristic.id"
              :val="characteristic.value"
              :label="characteristic.value"
              color="dark"
            />
          </div>

        </div>
          <div class="text-right">
          <q-btn
            label="Применить фильры"
            color="accent"
            class="q-mt-lg q-pa-sm"
            icon-right="tune"
            unelevated no-caps
            @click="filtration"
          />
          </div>
        </q-card-section>
      </q-card>
      </q-dialog>
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
  },
  data() {
    return {
      filtersCard: false,
      SelectedCharacteristics: [],
      minPrice: null,
      maxPrice: null,
      resetFiltersBtn: false
    }
  },
  watch: {
    '$route'() {
      this.resetFilters(false)
    }
  },
  methods: {
    filtration() {
      this.$emit('filtration', this.SelectedCharacteristics.join(','), this.minPrice ? this.minPrice : '', this.maxPrice ? this.maxPrice : '')
      this.resetFiltersBtn = true
      this.filtersCard = false
    },
    resetFilters(reloadProducts) {
      this.resetFiltersBtn = false
      this.SelectedCharacteristics = []
      this.minPrice = null
      this.maxPrice = null
      if (reloadProducts) this.$emit('resetFilters')
    }
  }
}
</script>

<style scoped>

</style>
