<template>
<q-page>
  <q-breadcrumbs class="q-pa-sm q-mt-md">
    <q-breadcrumbs-el icon="home" to="/"/>
    <q-breadcrumbs-el label="О магазине"/>
  </q-breadcrumbs>
  <script type="application/ld+json" v-html="schema"></script>
  <script type="application/ld+json" v-html="navigateSchema"></script>
  <pos-page-header title="О магазине" />
  <section class="info-page bg-white q-pa-md">
    <h2 class="text-bold text-center text-subtitle1">{{ shop.title }}</h2>
    <div class="q-mt-lg" v-html="shop.info"></div>
    <pos-share class="q-mt-lg" :image="this.$store.getters.getCompanyInfo.logo" :description="shop.description"/>
  </section>

  <pos-shop-reviews class="section"/>
  <pos-clients-slider />
</q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosShare from "components/service/posShare";
import PosShopReviews from "components/homePage/posShopReviews";
import PosClientsSlider from "components/sliders/posClientsSlider";
export default {
  name: "About",
  components: {PosClientsSlider, PosShopReviews, PosShare, PosPageHeader},
  computed: {
    shop() {
      return this.$store.getters.getAboutShopInfo
    },
    schema() {
      return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "url": `${this.$store.getters.getCompanyInfo.site_url}/about`,
        "logo": `${this.$store.getters.getCompanyInfo.logo}`
      }
    },
    navigateSchema() {
      return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
          "@type": "ListItem",
          "position": 1,
          "name": "О магазине",
          "item": `${this.$store.getters.getCompanyInfo.site_url}/about`
        }]
      }
    }
  },
  preFetch({ store }) {
    return store.dispatch('fetchAboutShopInfo')
  },
  data() {
    return {
    }
  },
  meta() {
    let data = this.$store.getters.getAboutShopInfo
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `О магазине | ${siteTitle}`,
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
          content: `О магазине | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/about`,
        },
        ogDescription: {
          property: "og:description",
          content: data.description,
        },
        ogImage: {
          property: "og:image",
          content: `${this.$store.getters.getCompanyInfo.logo}`
        }
      }
    }
  }

}
</script>

<style scoped>

</style>
