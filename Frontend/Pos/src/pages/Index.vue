<template>
  <q-page class="">
    <pos-page-header :title="companyInfo.title" />
    <pos-slider />
    <pos-banners />
    <pos-product-tabs />
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosSlider from "components/homePage/posSlider";
import PosProductTabs from "components/homePage/posProductTabs";
import PosBanners from "components/shop/posBanners";
export default {
  name: 'PageIndex',
  components: {PosBanners, PosProductTabs, PosSlider, PosPageHeader},
  computed: {
    companyInfo() {
      return this.$store.getters.getCompanyInfo
    }
  }
}
</script>
