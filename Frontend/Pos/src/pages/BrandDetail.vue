<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el :label="brand.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="`Товары от производителя ${brand.title}`"/>
    <!--    Brand description   -->
    <section class="q-pa-sm">
      <q-card class="border-radius-6 grey-border shadow-0 q-px-sm q-pt-md q-pb-sm">
        <p class="text-center q-pb-sm">{{ brand.description }}</p>
      </q-card>
    </section>
    <!--    xxxxx   -->
    <!--    Products   -->
    <section class="q-pa-sm q-mt-md">
      <pos-products-wrapper :products="brand.products"/>
    </section>
    <!--    xxxxx   -->
    <section>
      <pos-banners/>
    </section>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosBanners from "components/shop/posBanners";

export default {
  name: "BrandDetail",
  components: {PosBanners, PosProductsWrapper, PosPageHeader},
  computed: {
    brand() {
      return this.$store.getters.getBrandDetail
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchBrandData', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.category-full_description
  text-transform: none
  text-align: left
</style>
