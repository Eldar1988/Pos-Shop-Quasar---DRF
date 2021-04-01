<template>
  <div class="q-pa-sm">
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-mb-md home-tabs bg-white q-mt-sm"
      active-bg-color=""
      active-color="accent"
      indicator-color="accent"
    >
      <q-tab class="text-dark" name="reviews"
             :label="`Отзывы (${reviews.length})`"
             icon="chat_bubble_outline"
      />
      <q-tab
        v-if="product.characteristic"
        class="text-dark"
        name="characters"
        label="Характеристики"
        icon="tune"
      />
      <q-tab
        v-if="product.info"
        class="text-dark"
        name="more"
        label="Подробнее"
        icon="search"
      />
    </q-tabs>
    <q-tab-panels
      swipeable
      v-model="tab"
      animated
      transition-prev="scale"
      transition-next="scale"
      class="bg-grey-2"
    >
      <q-tab-panel name="reviews">
        <pos-product-reviews :reviews="product.reviews" :productId="`${product.id}`"/>
      </q-tab-panel>

      <q-tab-panel name="characters">
        <q-card square>
          <q-card-section class="text-weight-regular text-left">
            <div
              v-html="product.characteristic"
              style="overflow-x:scroll"
            >
            </div>
          </q-card-section>
        </q-card>
      </q-tab-panel>

      <q-tab-panel name="more">
        <q-card square>
          <q-card-section class="text-weight-regular text-left">
            <div
              v-html="product.info"
              style="overflow-x:scroll"
            >
            </div>
          </q-card-section>
        </q-card>
      </q-tab-panel>
    </q-tab-panels>
  </div>
</template>

<script>
import PosProductReviews from "components/shop/posProductReviews";
export default {
  name: "posProductDetailTabs",
  components: {PosProductReviews},
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  computed: {
    reviews() {
      return this.$store.getters.getProductDetailData.product.reviews.filter(item => item.public)
    }
  },
  data() {
    return {
      tab: ''
    }
  },
}
</script>

<style scoped>

</style>
