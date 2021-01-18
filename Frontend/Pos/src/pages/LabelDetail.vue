<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el :label="label.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="`Товары с меткой '${label.title}'`"/>
    <!--    Products   -->
    <section class="q-pa-sm q-mt-md">
      <pos-products-wrapper :products="label.products"/>
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
  name: "LabelDetail",
  components: {PosBanners, PosProductsWrapper, PosPageHeader},
  computed: {
    label() {
      return this.$store.getters.getLabelDetail
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchLabelData', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.category-full_description
  text-transform: none
  text-align: left
</style>
