<template>
  <q-page class="">
    <script type="application/ld+json" v-html="schema"></script>
    <pos-page-header :title="companyInfo.title" style="margin-top: -60px" class="ellipsis"/>
    <pos-slider/>
    <section class="q-mt-xl">
      <pos-section-title title="Новинки"/>
        <pos-products-slide-x :products="this.$store.getters.getLatestProducts" class="q-mt-md"/>
    </section>
    <section class="q-px-sm q-mt-xl">
      <!--      <pos-section-title title="Категории"/>-->
      <pos-categories :categories="parentCategories"/>
    </section>
    <pos-banners/>

    <pos-product-tabs class="q-mt-xl"/>
    <pos-brands-slider class="q-mt-xl"/>
    <pos-shop-reviews class="q-mt-lg"/>
    <pos-clients-slider />
    <!--    BRANDS & REVIEWS   -->
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosSlider from "components/homePage/posSlider";
import PosProductTabs from "components/homePage/posProductTabs";
import PosBanners from "components/shop/posBanners";
import PosCategories from "components/shop/posCategories";
import PosSectionTitle from "components/service/posSectionTitle";
import PosShopReviews from "components/homePage/posShopReviews";
import PosBrandsSlider from "components/sliders/posBrandsSlider";
import PosClientsSlider from "components/sliders/posClientsSlider";
import PosProductsSlideX from "components/sliders/posProductsSlideX";

export default {
  name: 'PageIndex',
  components: {
    PosProductsSlideX,
    PosClientsSlider,
    PosBrandsSlider,
    PosShopReviews,
    PosSectionTitle, PosCategories, PosBanners, PosProductTabs, PosSlider, PosPageHeader
  },
  computed: {
    companyInfo() {
      return this.$store.getters.getCompanyInfo
    },
    categories() {
      return this.$store.getters.getCategories
    },
    parentCategories() {
      return this.$store.getters.getParentCategories
    }
  },
  data() {
    return {
      schema: {
        "@context": "https://schema.org",
        "@type": "Organization",
        "url": this.$store.getters.getCompanyInfo.site_url,
        "logo": this.$store.getters.getCompanyInfo.logo
      },
    }
  },
  meta() {
    let data = this.$store.getters.getCompanyInfo
    return {
      title: data.title,
      meta: {
        description: {
          name: "description",
          content: data.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: data.title,
        },
        ogUrl: {
          property: "og:url",
          content: this.$store.getters.getCompanyInfo.site_url,
        },
        ogDescription: {
          property: "og:description",
          content: data.description,
        },
        ogImage: {
          property: "og:image",
          content: data.logo
        }
      }
    }
  }
}
</script>
