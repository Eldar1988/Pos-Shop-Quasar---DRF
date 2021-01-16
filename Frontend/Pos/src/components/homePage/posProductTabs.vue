<template>
  <section class="section q-pa-sm q-mt-lg">
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-mb-lg bg-grey-3 border-radius-6"
      active-bg-color="primary"
      active-color="white"
      indicator-color="primary"
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
      >
        <q-tab-panel name="hits">
          <pos-products-wrapper v-if="serverStatus" :products="hitProducts" />
          <pos-skeleton-products v-else />
        </q-tab-panel>

        <q-tab-panel name="sales">

        </q-tab-panel>

        <q-tab-panel name="future">

        </q-tab-panel>
      </q-tab-panels>

    </div>
  </section>
</template>

<script>
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosSkeletonProducts from "components/service/posSkeletonProducts";
export default {
  name: "posProductTabs",
  components: {PosSkeletonProducts, PosProductsWrapper},
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
    // async LoadSaleProducts() {
    //   try {
    //
    //   }
    // }
  }
}
</script>

<style scoped>

</style>
