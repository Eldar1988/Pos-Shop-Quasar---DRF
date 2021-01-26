<template>
  <div>
    <article style="padding: 5px">
      <q-card class="border-radius-6 shadow-0 q-pa-sm grey-border">
        <div class="wish-item-wrapper">
          <div class="cart-item-image" style="min-width: 70px;">
            <router-link :to="`/product/${product.slug}`">
            <img height="70px" width="70px" :src="product.image" style="object-fit: contain; min-width: 70px" />
            </router-link>
          </div>
          <div class="cart-item-title q-ml-sm">
            <router-link :to="`/product/${product.slug}`">
            <p class="">{{ product.title }}</p>
            </router-link>
            <p class="text-bold q-pt-sm">Цена: {{ product.price|formatPrice }} <q-icon name="mdi-currency-kzt" class="icon-wrapper" /></p>
            <div class="wish-list-item-add-to-cart">
            </div>
            <q-btn
              label="Добавить в корзину"
              size="sm"
              unelevated
              color="positive"
              class="q-mt-sm border-radius-6 text-bold"
              @click="addToCart(product)"
            />
          </div>
          <q-btn
            icon="delete_forever"
            color="negative"
            class="border-radius-6"
            outline unelevated no-caps
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
    addToCart(product) {
      addToCart(product, 1)
      this.$root.$emit('updateCart')
      this.$q.notify({message: `Товар ${product.title.toLowerCase()} добавлен в корзину`, color: 'positive'})
      this.delWishItem(product.id)
    },
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
