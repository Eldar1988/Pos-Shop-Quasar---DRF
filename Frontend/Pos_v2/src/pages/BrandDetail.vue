<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el :label="brand.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="`Товары от производителя ${brand.title}`"/>
    <!--    Brand description   -->
    <section class="q-pa-sm" v-if="brand.description">
      <q-card class="shadow-0 q-px-sm q-pt-md q-pb-sm" square>
        <p class="text-center q-pb-sm">{{ brand.description }}</p>
      </q-card>
    </section>
    <!--    xxxxx   -->
    <pos-current-page :current-page="currentPage" :products-count="productsData ? productsData.count : 0"/>
    <!--    Products   -->
    <section class="q-pa-sm q-mt-md">
      <pos-products-wrapper :products="productsData ? productsData.results: []"/>
    </section>
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
    <!--    xxxxx   -->
    <section class="q-mt-xl">
      <pos-banners/>
    </section>
    <!--    Latest Products   -->
    <section class="q-py-xl">
      <pos-section-title title="Новинки"/>
      <pos-products-slide-x :products="this.$store.getters.getLatestProducts" class="q-mt-md"/>
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
  name: "BrandDetail",
  components: {
    PosCurrentPage,
    PosProductsSlideX,
    PosSectionTitle, PosBrandsSlider, PosBanners, PosProductsWrapper, PosPageHeader},
  computed: {
    brand() {
      return this.$store.getters.getBrandDetail
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
      this.$store.dispatch('fetchShopProducts', `brand=${this.$route.params.slug}&page=${this.currentPage}`)
    }
  },
  created() {
    this.fetchProductsData()
  },
  methods: {
    fetchProductsData() {
      this.$store.dispatch('fetchShopProducts', `brand=${this.$route.params.slug}&page=${this.currentPage}`)
    },
    scrollToTop() {
      setTimeout(() => {
        document.querySelector('#q-app').scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        })
      },200)
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
