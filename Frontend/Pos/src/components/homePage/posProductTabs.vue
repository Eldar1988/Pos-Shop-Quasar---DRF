<template>
  <section class="section q-pa-sm q-mt-lg">
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-mb-lg bg-grey-4 border-radius-6 home-tabs"
      active-bg-color="dark"
      active-color="white"
      indicator-color="dark"
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
        class="bg-grey-1"
      >
        <q-tab-panel name="hits">
          <pos-products-wrapper v-if="serverStatus" :products="hitProducts" />
          <pos-skeleton-products v-else />
        </q-tab-panel>

        <q-tab-panel name="sales">
          <pos-sale-products />
        </q-tab-panel>

        <q-tab-panel name="future">
          <pos-future-products />
        </q-tab-panel>
      </q-tab-panels>

    </div>
  </section>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosSkeletonProducts from "components/service/posSkeletonProducts";
import PosSaleProducts from "components/shop/posSaleProducts";
import scrollTo from "src/functions/scroll_to";
import PosFutureProducts from "components/shop/posFutureProducts";

export default {
  name: "posProductTabs",
  components: {PosFutureProducts, PosSaleProducts, PosSkeletonProducts, PosProductsWrapper},
  data() {
    return {
      tab: 'hits'
    }
  },
  computed: {
    hitProducts() {
      return this.$store.getters.getHitProducts
    },
    serverStatus() {
      return !this.$store.getters.getServerStatus
    }
  },
  mounted() {

  },
  methods: {
    scrollTo
  }
}
</script>

<style scoped>

</style>
