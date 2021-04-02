<template>
  <div>
    <article style="padding: 5px">
      <q-card class="shadow-0 q-pa-sm" square>
        <div class="wish-item-wrapper">
          <div class="cart-item-image" style="min-width: 70px;">
            <router-link :to="`/product/${product.id}`">
            <img :src="product.image || product.miniature_url" style="object-fit: cover; width: 70px; height: 70px" />
            </router-link>
          </div>
          <div class="cart-item-title q-ml-sm">
            <router-link :to="`/product/${product.id}`">
            <p class="">{{ product.title }}</p>
            </router-link>
            <p class="text-bold q-pt-sm">Цена: {{ product.price|formatPrice }} <q-icon name="mdi-currency-kzt" class="icon-wrapper" /></p>
            <div class="wish-list-item-add-to-cart">
            </div>
            <q-btn
              label="Перейти к товару"
              size="sm"
              icon-right="arrow_right_alt"
              unelevated no-caps
              color="primary"
              class="q-mt-sm text-bold"
              :to="`/product/${product.id}`"
            />
          </div>
          <q-btn
            icon="delete_forever"
            color="negative"
            unelevated no-caps  flat dense
            size="sm"
            label="удалить"
            style="position: absolute; bottom: 0; right: 0"
            @click="delWishItem(product.id)"
          />
        </div>
      </q-card>
    </article>
  </div>
</template>

<script>
import formatPrice from "src/filters/format_price"
import addToCart from "src/functions/add_to_cart";

export default {
  name: "posWishListItem",
  filters: {
    formatPrice
  },
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  methods: {
    delWishItem(id) {
      let items = JSON.parse(localStorage.wishList)
      items.forEach((item) => {
        if (item.id === id) {
          items.splice(items.indexOf(item), 1)
        }
      })
      localStorage.setItem('wishList', JSON.stringify(items))
      this.$root.$emit('updateWishList')
      this.$q.notify({message: 'Товар удален из избранного', position: 'top'})
    }
  }
}
</script>

<style lang="sass">
.wish-item-wrapper
  display: flex
  align-items: center
  position: relative

</style>
