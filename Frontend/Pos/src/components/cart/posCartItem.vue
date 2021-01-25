<template>
  <div>
    <article>
      <q-card class="border-radius-6 shadow-0 q-mb-sm q-pa-sm grey-border">
        <div class="cart-item-wrapper">
          <div class="cart-item-image" style="min-width: 70px;">
            <router-link :to="`/product/${product.slug}`">
              <img height="70px" width="70px" :src="product.image" style="object-fit: contain; min-width: 70px"/>
            </router-link>
          </div>
          <div class="cart-item-title q-ml-sm">
            <router-link :to="`/product/${product.slug}`">
              <p class="">{{ product.title }}</p>
            </router-link>
            <p class="ellipsis text-bold">Цена: {{ product.price|formatPrice }}
              <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
            </p>
            <div class="cart-item-quantity">
              <div class="full-width flex justify-start">
                <div class="">
                  <div class="quantity-wrapper q-mt-sm">
                    <q-btn
                      icon="remove"
                      class="border-radius-6"
                      outline
                      color="dark"
                      size="sm"
                      @click="quantityMinus(product.id)"
                    />
                    <p class="text-center text-bold">{{ product.quantity }}</p>
                    <q-btn
                      icon="add"
                      class="border-radius-6"
                      outline
                      color="dark"
                      size="sm"
                      @click="quantityPlus(product.id)"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <q-btn
            icon="delete_forever"
            color="negative"
            class="border-radius-6"
            outline unelevated no-caps
            size="sm"
            label="удалить"
            style="position: absolute; bottom: 0; right: 0"
            @click="delCartItem(product.id)"
          />
        </div>
      </q-card>
    </article>
  </div>
</template>

<script>
import formatPrice from "src/filters/format_price";

export default {
  name: "posCartItem",
  filters: {formatPrice},
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  methods: {
    quantityMinus(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          if (item.quantity > 1) {
            item.quantity--
          }
        }
      })
      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },
    quantityPlus(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          item.quantity++
        }
      })

      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },
    delCartItem(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          items.splice(items.indexOf(item), 1)
        }
      })
      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
      this.$q.notify({message: 'Товар удален из корзины', position: 'top'})
    }
  }
}
</script>

<style lang="sass">
.cart-item-wrapper
  display: flex
  align-items: center
  position: relative

.quantity-wrapper
  display: grid
  grid-template-columns: 2fr 2fr 2fr
  grid-gap: 5px
  max-width: 120px
  height: 25px
</style>
