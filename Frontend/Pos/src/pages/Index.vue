<template>
  <q-page class="">
    <pos-page-header :title="companyInfo.title" />
    <pos-slider />
    <pos-banners />
    <pos-product-tabs />
    <section class="q-mt-xl q-px-sm q-py-xl bg-grey-2">
      <pos-section-title title="Категории" />
      <pos-categories :categories="categories" class="q-mt-lg" />
    </section>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosSlider from "components/homePage/posSlider";
import PosProductTabs from "components/homePage/posProductTabs";
import PosBanners from "components/shop/posBanners";
import PosCategories from "components/shop/posCategories";
import PosSectionTitle from "components/service/posSectionTitle";
export default {
  name: 'PageIndex',
  components: {PosSectionTitle, PosCategories, PosBanners, PosProductTabs, PosSlider, PosPageHeader},
  computed: {
    companyInfo() {
      return this.$store.getters.getCompanyInfo
    },
      categories() {
        return this.$store.getters.getCategories
      }
  }
}
</script>
