<template>
  <div>
    <article>
      <q-card class="shadow-0 q-mb-sm q-pa-sm" square>
        <div class="cart-item-wrapper">
          <div class="cart-item-image" style="min-width: 70px;">
            <router-link :to="`/product/${product.id}`">
              <img height="70px" width="70px" :src="product.image || product.miniature_url" style="object-fit: cover; min-width: 70px"/>
            </router-link>
          </div>
          <div class="cart-item-title q-ml-md">
            <router-link :to="`/product/${product.id}`">
              <p class="text-primary">{{ product.title }}</p>
            </router-link>
            <span
              v-for="variation in product.variations"
              :key="variation.id"
              class="q-mr-md"
            >
              {{ variation.type }}: {{ variation.value }}
            </span>
            <p class="text-bold q-pt-sm">Цена: {{ product.price|formatPrice }}
              <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
            </p>
            <div class="cart-item-quantity">
              <div class="full-width flex justify-start">
                <div class="">
                  <div class="quantity-wrapper q-mt-sm">
                    <q-btn
                      icon="remove"
                      dense unelevated  outline
                      color="negative"
                      size="sm"
                      @click="quantityMinus(product.timeID)"
                    />
                    <p class="text-center text-bold" style="padding: 2px 5px 0">{{ product.quantity }}</p>
                    <q-btn
                      icon="add"
                      dense unelevated  outline
                      color="positive"
                      size="sm"
                      @click="quantityPlus(product.timeID)"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <q-btn
            icon="delete_forever"
            color="negative"
            outline unelevated no-caps flat
            size="sm"
            label="удалить"
            style="position: absolute; bottom: -5px; right: -5px"
            @click="delCartItem(product.timeID)"
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
        if (item.timeID === id) {
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
        if (item.timeID === id) {
          item.quantity++
        }
      })

      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },
    delCartItem(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.timeID === id) {
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
