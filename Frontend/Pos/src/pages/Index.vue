<template>
  <q-page class="">
    <script type="application/ld+json" v-html="schema"></script>
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
    <pos-brands-slider />
    <pos-shop-reviews class="section"/>
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
import PosBrandsSlider from "components/service/posBrandsSlider";

export default {
  name: 'PageIndex',
  components: {
    PosBrandsSlider,
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
