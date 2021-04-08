<template>
  <q-page>
    <div id="page-header"></div>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el label="Магазин"/>
    </q-breadcrumbs>
    <pos-page-header :title="category.title" />
    <!--    Category description   -->
    <section class="q-pa-sm" v-if="category.description">
      <q-card
        square
        class="bg-white shadow-0 q-px-sm q-pt-md q-pb-sm"
      >
        <p class="text-center q-pb-sm">{{ category.description }}</p>
        <q-expansion-item
          v-if="category.full_description"
          label="Подробнее"
          class="text-center text-bold text-uppercase"
        >
          <q-card>
            <div
              class="text-weight-regular category-full_description q-pa-sm"
              v-html="category.full_description"
            ></div>
          </q-card>
        </q-expansion-item>
      </q-card>
    </section>
    <!--    xxxxx   -->

<!--    filters   -->
    <div class="flex justify-between" style="align-items: center">
      <pos-filters
        :filters="category.characteristic_types"
        @filtration="setFilters"
        @resetFilters="resetFilters"
      />
      <div class="q-px-sm text-right">
        <pos-current-page :current-page="currentPage" :products-count="productsData ? productsData.count : 0"/>
      </div>
    </div>
<!--    xxxxx   -->
    <div v-if="productsData && productsData.results.length > 0" class="products-section">
      <!--    Products   -->
      <section class="q-pa-sm q-mt-md" id="shop-products">
        <pos-products-wrapper :products="productsData ? productsData.results : []"/>
      </section>
      <div class="pagination q-px-sm q-mt-md flex flex-center">
        <div class="">
          <q-pagination
            v-model="currentPage"
            :max="productsData ? +(Math.ceil(productsData.count/30)) : 0"
            direction-links
            :max-pages="5"
            @click="scrollToTop"
            unelevated
          />
        </div>
      </div>
      <!--    xxxxx   -->
    </div>

    <div v-else class="q-pa-sm">
      <q-card
        square
        class="shadow-0 full-width bg-white q-py-xl q-px-md text-center"
      >
        <p>Извините, товаров не найдено.</p>
      </q-card>
    </div>

    <!--    Banners   -->
    <section class="q-pt-xl">
      <pos-banners/>
    </section>
    <!--    xxxxx   -->

    <!--    Latest Products   -->
    <section class="q-py-xl">
      <pos-section-title title="Новинки"/>
      <pos-products-slide-x :products="latestProducts" class="q-mt-md"/>
    </section>
    <!--    xxxxx   -->

    <pos-section-title title="Смотрите также" class="q-mt-lg"/>
    <pos-categories class="q-mt-md q-pa-sm" :categories="this.$store.getters.getCategories"/>
    <pos-brands-slider class="q-mt-xl"/>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosCategories from "components/shop/posCategories";
import PosBanners from "components/shop/posBanners";
import PosSectionTitle from "components/service/posSectionTitle";
import PosBrandsSlider from "components/sliders/posBrandsSlider";
import PosProductsSlideX from "components/sliders/posProductsSlideX";
import PosCurrentPage from "components/shop/utils/posCurrentPage";
import PosFilters from "components/shop/utils/posFilters";

export default {
  name: "Shop",
  components: {
    PosFilters,
    PosCurrentPage,
    PosProductsSlideX,
    PosBrandsSlider,
    PosSectionTitle, PosBanners, PosCategories, PosProductsWrapper, PosPageHeader
  },
  data() {
    return {
      currentPage: 1,
      filters: ''
    }
  },
  computed: {
    category() {
      return this.$store.getters.getCategoryDetail
    },
    latestProducts() {
      return this.$store.getters.getLatestProducts
    },
    productsData() {
      return this.$store.getters.getShopProductsData
    }
  },
  created() {
    this.loadProductData()
  },
  watch: {
    '$route'() {
      this.loadProductData()
    },
    currentPage() {
      this.$store.dispatch('fetchShopProducts', `category_slug=${this.$route.params.slug}&page=${this.currentPage}&${this.filters}`)
    },
    filters() {
      this.$store.dispatch('fetchShopProducts', `category_slug=${this.$route.params.slug}&page=${this.currentPage}&${this.filters}`)
    }
  },
  methods: {
    setFilters(characteristics, minPrice, maxPrice, orderBy) {
      this.currentPage = 1
      this.filters = `characteristics=${characteristics}&price_min=${minPrice}&price_max=${maxPrice}&order_by=${orderBy}`
    },
    loadProductData() {
      this.$store.dispatch('fetchShopProducts', `category_slug=${this.$route.params.slug}`)
    },
    scrollToTop() {
      setTimeout(() => {
        document.querySelector('#q-app').scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        })
      },200)
    },
    resetFilters() {
      this.filters = ''
      this.currentPage = 1
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchCategoryData', currentRoute.params.slug)
  },


  meta() {
    let category = this.$store.getters.getCategoryDetail
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `${category.title} | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: category.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: `${category.title} | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/shop/${category.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: category.description,
        },
        ogImage: {
          property: "og:image",
          content: category.image
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
