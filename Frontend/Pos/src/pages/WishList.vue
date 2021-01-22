<template>
  <q-page>
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
            class="border-radius-6 q-mt-md text-bold"
            to="/"
          />
        </div>
      </q-card>
    </section>
    <!--    xxxxx   -->
    <q-separator class="q-mt-xl" inset=""/>
    <pos-banners class="q-mt-xl"/>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosWishListItem from "components/wishList/posWishListItem";
import PosBanners from "components/shop/posBanners";

export default {
  name: "WishList",
  components: {PosBanners, PosWishListItem, PosPageHeader},
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
      this.products = JSON.parse(localStorage.wishList)
    }
  }
}
</script>

<style lang="sass">

</style>
