<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el :label="label.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="`Товары с меткой '${label.title}'`"/>
    <!--    Products   -->
    <pos-current-page :current-page="currentPage" :products-count="productsData ? productsData.count : 0"/>
    <section class="q-pa-sm q-mt-md">
      <pos-products-wrapper :products="productsData ? productsData.results: []"/>
      <div class="pagination q-px-sm q-mt-md flex flex-center">
        <div class="">
          <q-pagination
            v-model="currentPage"
            :max="productsData ? +(Math.ceil(productsData.count/30)) : 0"
            direction-links
            :max-pages="7"
            @click="scrollToTop"
            unelevated
          />
        </div>
      </div>
    </section>
    <!--    xxxxx   -->
    <section style="margin-top: 100px">
      <pos-banners/>
    </section>
    <!--    Latest Products   -->
    <section class="q-py-xl">
      <pos-section-title title="Новинки"/>
      <pos-products-slide-x :products="latestProducts" class="q-mt-md"/>
    </section>
    <!--    xxxxx   -->
    <pos-brands-slider class="q-mt-lg"/>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosBanners from "components/shop/posBanners";
import PosBrandsSlider from "components/sliders/posBrandsSlider";
import PosSectionTitle from "components/service/posSectionTitle";
import PosProductsSlideX from "components/sliders/posProductsSlideX";
import PosCurrentPage from "components/shop/utils/posCurrentPage";

export default {
  name: "LabelDetail",
  components: {
    PosCurrentPage,
    PosProductsSlideX, PosSectionTitle, PosBrandsSlider, PosBanners, PosProductsWrapper, PosPageHeader},
  computed: {
    label() {
      return this.$store.getters.getLabelDetail
    },
    latestProducts() {
      return this.$store.getters.getLatestProducts
    },
    productsData() {
      return this.$store.getters.getShopProductsData
    }
  },
  data() {
    return {
      currentPage: 1
    }
  },
  watch: {
    currentPage() {
      this.$store.dispatch('fetchShopProducts', `label=${this.$route.params.slug}&page=${this.currentPage}`)
    },
  },
  created() {
    this.$store.dispatch('fetchShopProducts', `label=${this.$route.params.slug}&page=${this.currentPage}`)
  },
  methods: {
    scrollToTop() {
      setTimeout(() => {
        document.querySelector('#q-app').scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        })
      }, 200)
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
