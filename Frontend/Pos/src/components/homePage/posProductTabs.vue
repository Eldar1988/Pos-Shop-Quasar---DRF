<template>
  <section class="section q-pa-sm q-mt-lg">
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-mb-lg border-radius-6 home-tabs"
      active-bg-color=""
      active-color="accent"
      indicator-color="accent"
    >
      <q-tab class="text-dark border-radius-6" name="hits" label="Хиты продаж" icon="mdi-alert-decagram" />
      <q-tab class="text-dark border-radius-6" name="sales" label="Скидки" icon="mdi-sale" />
      <q-tab class="text-dark border-radius-6" name="future" label="Рекомендуем" icon="loyalty" />
    </q-tabs>

    <div class="q-mt-lg">
      <q-tab-panels
        swipeable
        v-model="tab"
        animated
        transition-prev="scale"
        transition-next="scale"
        class="bg-grey-2"
      >
        <q-tab-panel name="hits">
          <pos-products-wrapper :products="hitProducts" />
        </q-tab-panel>

        <q-tab-panel name="sales">
          <pos-products-wrapper :products="saleProducts" />
        </q-tab-panel>

        <q-tab-panel name="future">
          <pos-products-wrapper :products="futureProducts" />
        </q-tab-panel>
      </q-tab-panels>

    </div>
  </section>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
import scrollTo from "src/functions/scroll_to";

export default {
  name: "posProductTabs",
  components: {PosProductsWrapper},
  data() {
    return {
      tab: 'hits'
    }
  },
  computed: {
    hitProducts() {
      return this.$store.getters.getHitProducts
    },
    saleProducts() {
      return this.$store.getters.getSaleProducts
    },
    futureProducts() {
      return this.$store.getters.getFutureProducts
    }
  },
  async mounted() {
    setTimeout(() => {
      this.$store.dispatch('fetchHitProducts')
      this.$store.dispatch('fetchSaleProducts')
      this.$store.dispatch('fetchFutureProducts')
    },3000)
  },
  methods: {
    scrollTo
  }
}
</script>

<style scoped>

</style>
