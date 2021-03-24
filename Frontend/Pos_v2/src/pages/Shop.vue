<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el
        v-if="category.parent"
        :label="category.parent.title"
        :to="`/shop/${category.parent.slug}`"
      />
      <q-breadcrumbs-el :label="category.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="category.title"/>
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
      <pos-categories
        :categories="category.child"
        class="q-mt-lg"
      />
    </section>
    <!--    xxxxx   -->
    <!--    Products   -->
    <section class="q-pa-sm q-mt-md">
      <pos-labels-filter :products="category.products"/>
      <pos-products-wrapper :products="category.products"/>
      <div
        v-for="child in category.child"
        :key="child.id"
      >
        <pos-section-title :title="child.title" class="bg-grey-3 q-py-sm"/>
        <pos-products-wrapper :products="child.products" class="q-mb-xl q-mt-lg"/>
      </div>

    </section>
    <!--    xxxxx   -->
    <!--    Banners   -->
    <section>
      <pos-banners/>
    </section>
    <!--    xxxxx   -->
    <!--    Latest Products   -->
    <section class="q-py-xl">
      <pos-section-title title="Новинки"/>
      <pos-products-slide-x :products="latestProducts" class="q-mt-md"/>
    </section>
    <!--    xxxxx   -->

    <pos-section-title title="Смотрите также" class="q-mt-lg" />
    <pos-categories class="q-mt-md q-pa-sm" :categories="this.$store.getters.getCategories" />
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
import PosLabelsFilter from "components/service/posLabelsFilter";

export default {
  name: "Shop",
  components: {
    PosLabelsFilter,
    PosProductsSlideX,
    PosBrandsSlider,
    PosSectionTitle, PosBanners, PosCategories, PosProductsWrapper, PosPageHeader
  },
  computed: {
    category() {
      return this.$store.getters.getCategoryDetail
    },
    latestProducts() {
      return this.$store.getters.getLatestProducts
    }
  },
  watch: {
    '$route' () {
      this.loadCategoryData()
    }
  },
  created() {
    this.loadCategoryData()
  },
  methods: {
    loadCategoryData() {
      return this.$store.dispatch('fetchCategoryData', this.$route.params.slug)
    }
  },
  // preFetch({store, currentRoute}) {
  //   return store.dispatch('fetchCategoryData', currentRoute.params.slug)
  // },
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
