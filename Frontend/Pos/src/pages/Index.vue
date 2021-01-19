<template>
  <q-page class="">
    <pos-page-header :title="companyInfo.title"/>
    <pos-slider/>
    <section class="section">
      <pos-section-title title="Новинки" />
      <pos-hot-products-slider class="q-mt-sm"/>
    </section>

    <pos-banners/>
    <pos-product-tabs/>
    <section class="q-mt-xl q-px-sm q-py-xl bg-grey-2">
      <pos-section-title title="Категории"/>
      <pos-categories :categories="categories" class="q-mt-lg"/>
    </section>
    <pos-shop-reviews />
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosSlider from "components/homePage/posSlider";
import PosProductTabs from "components/homePage/posProductTabs";
import PosBanners from "components/shop/posBanners";
import PosCategories from "components/shop/posCategories";
import PosSectionTitle from "components/service/posSectionTitle";
import PosHotProductsSlider from "components/homePage/posHotProductsSlider";
import PosShopReviews from "components/homePage/posShopReviews";

export default {
  name: 'PageIndex',
  components: {
    PosShopReviews,
    PosHotProductsSlider,
    PosSectionTitle, PosCategories, PosBanners, PosProductTabs, PosSlider, PosPageHeader
  },
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
