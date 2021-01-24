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
    let price = 2000
    return store.dispatch('fetchBrandData', currentRoute.params.slug)
  },
  meta() {
    let brand = this.$store.getters.getBrandDetail
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `${brand.title} | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: brand.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: `${brand.title} | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/brand/${brand.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: brand.description,
        },
        ogImage: {
          property: "og:image",
          content: brand.image
        }
      }
    }
  }
}
</script>

<style lang="sass">
.category-full_description
  text-transform: none
  text-align: left
</style>
