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
    <section style="margin-top: 100px">
      <pos-banners/>
    </section>
    <pos-brands-slider />
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosBanners from "components/shop/posBanners";
import PosBrandsSlider from "components/sliders/posBrandsSlider";

export default {
  name: "LabelDetail",
  components: {PosBrandsSlider, PosBanners, PosProductsWrapper, PosPageHeader},
  computed: {
    label() {
      return this.$store.getters.getLabelDetail
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchLabelData', currentRoute.params.slug)
  },
  meta() {
    let label = this.$store.getters.getLabelDetail
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `${label.title} | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: label.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: `${label.title} | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/brand/${label.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: label.description,
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

<style lang="sass">
.category-full_description
  text-transform: none
  text-align: left
</style>
