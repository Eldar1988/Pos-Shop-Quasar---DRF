<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el label="Избранные товары"/>
    </q-breadcrumbs>
    <pos-page-header title="Избранные товары"/>
    <section v-if="products.length > 0">
      <div  class="row q-pa-sm">
        <div
          v-for="product in products"
          :key="product.id"
          class="col-12 col-sm-6 col-lg-4"
        >
          <q-slide-transition appear>
            <pos-wish-list-item :product="product"/>
          </q-slide-transition>
        </div>
      </div>
    </section>
    <!--    Empty wish list alert   -->
    <section
      v-if="products.length === 0"
      class="q-px-sm"
    >
      <q-card
        square
        class="bg-negative red-shadow q-px-sm q-py-xl flex flex-center q-mt-md"
      >
        <div class="text-center">
          <p class="text-subtitle1 text-white">
            Ваш список избранных товаров пуст.
          </p>
          <q-btn
            label="вернуться в магазин"
            outline
            color="white"
            class="q-mt-md text-bold"
            to="/"
          />
        </div>
      </q-card>
    </section>
    <!--    xxxxx   -->

    <pos-banners class="section"/>

    <section class="q-py-xl">
      <pos-section-title title="Новинки" class="q-mb-md"/>
      <pos-products-slide-x :products="this.$store.getters.getLatestProducts"/>
    </section>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosWishListItem from "components/wishList/posWishListItem";
import PosBanners from "components/shop/posBanners";
import PosSectionTitle from "components/service/posSectionTitle";
import PosProductsSlideX from "components/sliders/posProductsSlideX";

export default {
  name: "WishList",
  components: {PosProductsSlideX, PosSectionTitle, PosBanners, PosWishListItem, PosPageHeader},
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.$root.$on('updateWishList', () => {
      this.getWishProducts()
    })
    this.getWishProducts()
  },
  methods: {
    getWishProducts() {
      if (localStorage.getItem('wishList') !== null) {
        this.products = JSON.parse(localStorage.wishList)
      } else {
        return null
      }
    }
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Ваш список желаний | ${siteTitle}`,
    }
  }
}
</script>

<style lang="sass">

</style>
