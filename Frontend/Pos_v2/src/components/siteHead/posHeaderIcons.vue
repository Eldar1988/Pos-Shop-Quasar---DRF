<template>
  <div>
    <q-tabs align="center" shrink narrow-indicator active-bg-color="grey-2" indicator-color="grey-2" >
      <q-route-tab to="/" icon="roofing" class="small-tabs text-dark"/>
      <q-route-tab to="/search" icon="search" class="small-tabs hide-on-mobile text-dark"/>
      <q-route-tab to="/wishList" icon="favorite" class="small-tabs text-dark"><q-badge v-if="wishList" color="accent">{{ wishList }}</q-badge></q-route-tab>
      <q-route-tab to="/cart" icon="shopping_bag" class="small-tabs text-dark"><q-badge v-if="cartLen" color="accent">{{ cartLen }}</q-badge></q-route-tab>
    </q-tabs>
  </div>
</template>

<script>
export default {
  name: "posHeaderIcons",
  data() {
    return {
      cartLen: null,
      wishList: null
    }
  },
  mounted() {
    this.$root.$on('updateWishList', () => {
      this.getWishListLen()
    })
    this.$root.$on('updateCart', () => {
      this.getCartLen()
    })
    this.getCartLen()
    this.getWishListLen()
  },
  methods: {
    getCartLen() {
      if (localStorage.getItem('cart') !== null) {
        this.cartLen = JSON.parse(localStorage.cart).length
      } else {
        return null
      }
    },
    getWishListLen() {
      if (localStorage.getItem('wishList') !== null) {
        this.wishList = JSON.parse(localStorage.wishList).length
      } else {
        return null
      }
    }
  }
}
</script>

<style lang="sass">
.q-header .q-tab__content, .q-footer .q-tab__content
  min-width: 54px !important
</style>
