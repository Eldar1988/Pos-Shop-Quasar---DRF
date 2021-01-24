<template>
  <div>
    <q-tabs align="center" shrink narrow-indicator active-bg-color="grey-2" indicator-color="grey-2">
      <q-route-tab to="/" icon="roofing" class="small-tabs"/>
      <q-route-tab to="/search" icon="search" class="small-tabs hide-on-mobile"/>
      <q-route-tab to="/wishList" icon="favorite" class="small-tabs"><q-badge v-if="wishList" color="accent">{{ wishList }}</q-badge></q-route-tab>
      <q-route-tab to="/cart" icon="shopping_bag" class="small-tabs"><q-badge v-if="cartLen" color="accent">{{ cartLen }}</q-badge></q-route-tab>
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
      this.cartLen = JSON.parse(localStorage.cart).length
    },
    getWishListLen() {
      this.wishList = JSON.parse(localStorage.wishList).length
    }
  }
}
</script>

<style scoped>

</style>
