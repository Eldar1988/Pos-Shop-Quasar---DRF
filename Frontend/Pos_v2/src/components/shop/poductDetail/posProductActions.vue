<template>
  <div>
    <div v-if="product.in_stock_quantity > 0" class="row">
      <!--        Quantity   -->
      <div class="full-width flex justify-center q-mb-md">
        <div class="q-mt-sm">
          <div class="quantity-wrapper q-mt-sm">
            <q-btn
              icon="remove"
              class=""
              outline dense
              color="dark"
              size="sm"
              @click="quantity > 1 ? quantity -- : null"
            />
            <div style="height: 30px; overflow: hidden;">
              <q-input v-model="quantity" type="tel" class=""
                       input-class="text-center text-bold text-dark " input-style="max-height: 30px;"/>
            </div>
            <q-btn
              icon="add"
              outline dense
              color="dark"
              size="sm"
              @click="quantity ++"
            />
          </div>
        </div>
      </div>
      <!--        xxxxx   -->
      <div class="col-12 col-md-6 q-pa-sm">
        <q-btn
          label="Купить в 1 клик"
          color="accent"
          unelevated
          class="full-width q-py-sm text-bold"
          icon-right="forward"
          @click="selfAddToCart(product, quantity, true)"
        />
      </div>
      <div class="col-12 col-md-6 q-pa-sm">
        <div class="buttons-grid">
          <q-btn
            label="В корзину"
            color="positive"
            class="full-width q-py-sm text-bold"
            icon-right="add_shopping_cart"
            unelevated
            @click="selfAddToCart(product, quantity, false)"
          />
          <q-btn
            color="accent"
            @click="addToWishList(product)"
            text-color="accent"
            unelevated flat
            :icon="productInWishList ? 'favorite' : 'favorite_border'"
          />
        </div>
      </div>
      <div class="flex" style="align-items: center">
      <!--            Kaspi button   -->
      <div v-if="this.$store.state.kaspiButton" class="q-mt-sm q-ml-sm" id="dynamic" style="height: 50px"></div>
      <!--            xxxxx   -->
      </div>
      <!--      Google pay   -->
      <div v-if="googlePayMerchantId" style="height: 50px">
        <img src="../../../assets/Gpay.png" style="height: 50px; margin-top: 6px"
             @click="selfAddToCart(product, quantity, true)"
             class="cursor-pointer q-ml-md"
        />
      </div>
      <!--      xxxxx   -->
    </div>
    <div v-else>
      <q-card
        square
        class="bg-accent shadow-0 q-px-md q-py-lg q-mt-lg q-mb-md text-center"
        dark
      >
        Данного товара нет в наличии.<br>Ожидаем поступление.
      </q-card>
    </div>

    <!--    Cart dialog  -->
    <q-dialog v-model="cartDialog" position="top" seamless>
      <pos-added-to-cart-dialog :product="product"/>
    </q-dialog>
    <!--    xxxxx   -->
  </div>
</template>

<script>
import PosAddedToCartDialog from "components/cart/posAddedToCartDialog";
import addToCart from "src/functions/add_to_cart";
import addToWishListFunc from "src/functions/add_to_wishlist";
import notifier from "src/functions/notifier";

export default {
  name: "posProductActions",
  components: {PosAddedToCartDialog},
  props: {
    product: {
      type: Object,
      default: null
    },
    allVariationsSelected: {
      type: Boolean,
      default: false
    },
    selectedVariations: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      quantity: 1,
      cartDialog: false,
      productInWishList: false,
      googlePayMerchantId: null
    }
  },
  watch: {
    async product() {
      await this.checkWishList()
      if (this.$store.state.kaspiButton) this.kaspiButton()
    }
  },
  mounted() {
    this.checkWishList()
    this.googlePay()
    if (this.$store.state.kaspiButton) this.kaspiButton()
  },
  methods: {
    addProduct(selfVariations, product, quantity, redirect) {
      addToCart(product, quantity, selfVariations)
      this.$root.$emit('updateCart')
      if (redirect) this.$router.push('/cart')
      else {
        this.cartDialog = true
        setTimeout(() => {
          this.cartDialog = false
        }, 4000)
      }
    },
    selfAddToCart(product, quantity, redirect) {
      if (product.variations && product.variations.length > 0 && this.allVariationsSelected) {
        this.addProduct(this.selectedVariations, product, quantity, redirect)
      }
      else if (product.variations.length === 0){
        this.addProduct([], product, quantity, redirect)
      }
      else if (!product.variations){
        this.addProduct([], product, quantity, redirect)
      }
      else {
        notifier('Необходимо указать все вариации товара', 'negative')
      }
    },
    kaspiButton() {
      document.getElementById('dynamic').innerHTML = `<div class="ks-widget" data-template="button" data-merchant-sku="${this.product.article}" data-merchant-code="Posshopkz" data-city="750000000" ></div>`
      // you should run this method to recheck buttons in DOM:
      ksWidgetInitializer.reinit()
    },
    addToWishList(product) {
      addToWishListFunc(product)
      this.checkWishList()
      this.$root.$emit('updateWishList')
    },
    checkWishList() {
      this.productInWishList = false
      if (localStorage.getItem('wishList') !== null) {
        let wishList = JSON.parse(localStorage.wishList)
        wishList.forEach((item) => {
          if (item.id === this.product.id) {
            this.productInWishList = true
          }
        })
      }
    },
    async googlePay() {
      this.googlePayMerchantId = await this.$axios.get(`${this.$store.getters.getServerURL}/orders/google_pay_merchant/`)
        .then(({data}) => {
          return data.merchantId
        })
    }
  }
}
</script>

<style lang="sass">
.quantity-wrapper
  display: grid
  grid-template-columns: 2fr 2fr 2fr
  grid-gap: 5px
  max-width: 120px
  height: 25px

.buttons-grid
  display: grid
  grid-template-columns: 4fr 1fr
  grid-gap: 5px
</style>
