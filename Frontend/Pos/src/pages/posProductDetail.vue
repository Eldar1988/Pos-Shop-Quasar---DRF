<template>
  <q-page>
    <section>
      <q-breadcrumbs class="q-pa-sm q-mt-md">
        <q-breadcrumbs-el icon="home" to="/"/>
        <q-breadcrumbs-el :to="`/shop/${productData.product.category.slug}`"
                          :label="productData.product.category.title"/>
        <q-breadcrumbs-el :label="productData.product.title"/>
      </q-breadcrumbs>
    </section>

    <!--    Product Detail   -->
    <article>
      <div class="product-detail-wrapper q-mt-sm">
        <div class="q-pa-sm">
          <!--          Slider   -->
          <pos-product-detail-images-slider
            :images="productData.product.images"
            :image="productData.product.image"
            :title="productData.product.title"
          />
          <!--          xxxxx   -->
        </div>
        <div class="q-pa-sm">
          <!--            Title   -->
          <h1 class="product-header-text">{{ productData.product.title }}</h1>
          <!--          Rating   -->
          <div class="product-info-section">
            <q-rating v-model="productData.product.rating" size="28px" color="orange" readonly/>
          </div>
          <!--          Product price   -->
          <div class="product-info-section">
            <p class="product-detail-price text-positive text-bold">
              {{ productData.product.price|formatPrice }}
              <q-icon name="mdi-currency-kzt" class="icon-wrapper" size="24px"/>
              <span v-if="productData.product.old_price" class="product-detail-old-price text-grey-5 q-ml-sm">
                {{ productData.product.old_price|formatPrice }}
              </span>
              <q-badge
                v-if="productData.product.old_price"
                color="positive"
                class="q-ml-sm"
                style="padding-bottom: 3px">{{ getSaleSum }}
              </q-badge>
            </p>
          </div>
          <!--          Short description  -->
          <div class="product-info-section">
            <p>{{ productData.product.description }}</p>
          </div>
          <!--          Article  -->
          <div class="product-info-section">
            <p class="text-bold">
              Артикул: {{ productData.product.article }}
            </p>
          </div>
          <!--          Actions   -->
          <div class="row q-my-lg">
            <q-separator inset=""/>
            <!--            Quantity   -->
            <div class="full-width flex justify-center">
              <div class="q-mt-md">
                <p class="text-bold text-center">Количество:</p>
                <div class="quantity-wrapper q-mt-sm">
                  <q-btn
                    icon="remove"
                    class="border-radius-6"
                    outline
                    color="dark"
                    size="sm"
                    @click="quantity > 1 ? quantity -- : null"
                  />
                  <q-input v-model="quantity" type="tel" class="border-radius-6"
                           input-class="text-center text-bold text-dark"/>
                  <q-btn
                    icon="add"
                    class="border-radius-6"
                    outline
                    color="dark"
                    size="sm"
                    @click="quantity ++"
                  />
                </div>
              </div>
            </div>
            <!--            xxxxx   -->
            <div class="col-12 col-md-6 q-pa-sm q-mt-sm">
              <q-btn
                label="Купить в 1 клик"
                color="negative"
                class="border-radius-6 full-width red-shadow q-py-sm text-bold"
                icon-right="forward"
                @click="selfAddToCart(productData.product, quantity, true)"
              />
            </div>
            <div class="col-12 col-md-6 q-pa-sm q-mt-sm">
              <div class="buttons-grid">
              <q-btn
                label="В корзину"
                color="negative"
                outline
                class="border-radius-6 full-width q-py-sm text-bold"
                icon-right="add_shopping_cart"
                @click="selfAddToCart(productData.product, quantity, false)"
              />
                <q-btn
                  color="accent"
                  @click="addToWishList(productData.product)"
                  flat outline
                  :icon="productInWishList ? 'favorite' : 'favorite_border'"
                  class="border-radius-6"
                />
              </div>
            </div>
            <div class="q-mt-sm q-ml-sm" id="dynamic"></div>
            <q-separator inset="" class="q-mt-sm"/>
          </div>
          <!--          xxxxx   -->
          <!--          Category   -->
          <div class="product-info-section flex" style="align-items: center">
            <p class="text-bold">Категория: </p>
            <router-link :to="`/shop/${productData.product.category.slug}`">
              <span class="q-ml-sm"> {{ productData.product.category.title }}</span>
            </router-link>
          </div>
          <!--          xxxxx   -->
          <!--          Labels   -->
          <div class="product-info-section flex">
            <p class="text-bold">Метки: </p>
            <q-btn
              v-for="label in productData.product.labels"
              :key="label.id"
              :label="label.title"
              size="sm" outline
              class="border-radius-6 q-ml-sm text-bold"
              :to="`/label/${label.slug}`"
            />
          </div>
          <!--          xxxxx   -->
          <!--          Brand   -->
          <div class="product-info-section flex" style="align-items: center">
            <p class="text-bold">Бренд: </p>
            <router-link :to="`/brand/${productData.product.brand.slug}`">
              <q-img :src="productData.product.brand.image" height="30px" contain width="100px" class="q-ml-sm"/>
            </router-link>
          </div>
          <!--          xxxxx   -->

          <!--          Characters   -->
          <div v-if="productData.product.characteristic" class="q-mt-lg">
            <q-expansion-item
              dense-toggle
              expand-separator
              icon="tune"
              label="Характеристики"
              class="grey-border border-radius-6 text-center text-bold"
            >
              <q-card>
                <q-card-section class="text-weight-regular text-left">
                  <div
                    v-html="productData.product.characteristic"
                    style="overflow-x:scroll"
                  >
                  </div>
                </q-card-section>
              </q-card>
            </q-expansion-item>
          </div>
          <!--          xxxxx   -->
          <!--          Info   -->
          <div v-if="productData.product.info" class="product-info-section">
            <q-expansion-item
              dense-toggle
              expand-separator
              icon="search"
              label="Подробнее"
              class="grey-border border-radius-6 text-center text-bold"
            >
              <q-card>
                <q-card-section class="text-weight-regular text-left">
                  <div
                    v-html="productData.product.info"
                    style="overflow-x:scroll"
                  >
                  </div>
                </q-card-section>
              </q-card>
            </q-expansion-item>
          </div>
          <!--          xxxxx   -->
        </div>
      </div>
    </article>
    <q-separator inset="" class="q-mt-xl"/>
    <!--    xxxxx   -->
    <section v-if="productData.product.video" class="section q-pa-sm">
      <pos-section-title title="Видео обзор"/>
      <q-video
        :ratio="this.$q.platform.is.mobile ? 16/9 : 16/6"
        :src="`https://www.youtube.com/embed/${productData.product.video}`"
        class="border-radius-6 q-mt-lg"
      />
    </section>
    <!--    More products   -->
    <section v-if="productData.products.length > 0" class="q-mt-xl q-py-lg bg-grey-2">
      <pos-section-title title="Смотрите также:"/>
      <pos-products-scroll-x :products="productData.products"/>
    </section>
    <!--    xxxxx   -->
    <!--    Last sean products   -->
    <section class="q-mt-xl q-py-lg">
      <pos-section-title title="Вы недавно смотрели:"/>
      <pos-products-scroll-x :products="lastSeanProducts"/>
    </section>
    <!--    xxxxx   -->
    <!--    Banners   -->

    <pos-banners/>
    <!--   xxxxx   -->
    <!--    Cart dialog  -->
    <q-dialog v-model="cartDialog" position="top" seamless>
      <pos-added-to-cart-dialog :product="productData.product"/>
    </q-dialog>
    <!--    xxxxx   -->
  </q-page>
</template>

<script>
import PosProductDetailImagesSlider from "components/shop/posProductDetailImagesSlider"
import formatPrice from "src/filters/format_price";
import PosSectionTitle from "components/service/posSectionTitle";
import PosProductsScrollX from "components/shop/posProductsScrollX";
import PosBanners from "components/shop/posBanners";
import addToCart from "src/functions/add_to_cart";
import PosAddedToCartDialog from "components/cart/posAddedToCartDialog";
import addToWishList from "src/functions/add_to_wishlist";

export default {
  name: "posProductDetail",
  components: {PosAddedToCartDialog, PosBanners, PosProductsScrollX, PosSectionTitle, PosProductDetailImagesSlider},
  filters: {formatPrice},
  data() {
    return {
      lastSeanProducts: [],
      quantity: 1,
      cartDialog: false,
      productInWishList: false
    }
  },
  computed: {
    productData() {
      return this.$store.getters.getProductDetailData
    },
    getSaleSum: function () {
      let sum = this.productData.product.old_price - this.productData.product.price
      return `экономия ${sum} тенге`
    }
  },
  mounted() {
    this.setLastSeanProducts()
    this.getLastSeanProducts()
    this.kaspiButton()
    this.checkWishList()
  },
  watch: {
    async productData() {
      await this.setLastSeanProducts()
      await this.getLastSeanProducts()
      await this.checkWishList()
      await this.kaspiButton()
    }
  },
  methods: {
    setLastSeanProducts() {
      // Push self product to last sean products
      let productInLasts = false
      let lastProducts = []
      if (localStorage.getItem('lastProducts') !== null) {
        lastProducts = JSON.parse(localStorage.getItem('lastProducts'))
        lastProducts.forEach((product) => {
          if (product.id === this.productData.product.id) {
            productInLasts = true
          }
        })
        if (!productInLasts) {
          lastProducts.push(this.productData.product)
          localStorage.setItem('lastProducts', JSON.stringify(lastProducts))
        }
      } else {
        lastProducts.push(this.productData.product)
        localStorage.setItem('lastProducts', JSON.stringify(lastProducts))
      }
    },
    getLastSeanProducts() {
      this.lastSeanProducts = JSON.parse(localStorage.getItem('lastProducts'))
    },
    selfAddToCart(product, quantity, redirect) {
      addToCart(product, quantity)
      this.$root.$emit('updateCart')
      if (redirect) this.$router.push('/cart')
      else {
        this.cartDialog = true
        setTimeout(() => {
          this.cartDialog = false
        }, 5000)
      }
    },
    kaspiButton() {
      document.getElementById('dynamic').innerHTML = `<div class="ks-widget" data-template="button" data-merchant-sku="${this.productData.product.article}" data-merchant-code="Posshopkz" data-city="750000000" ></div>`
      // you should run this method to recheck buttons in DOM:
      ksWidgetInitializer.reinit()
    },
    addToWishList(product) {
      addToWishList(product)
      this.productInWishList = true
      this.$root.$emit('updateWishList')
    },
    checkWishList() {
      this.productInWishList = false
      if (localStorage.getItem('wishList') !== null) {
        let wishList = JSON.parse(localStorage.wishList)
        wishList.forEach((item) => {
          if (item.id === this.productData.product.id) {
            this.productInWishList = true
          }
        })
      }
      console.log(this.productInWishList)
    },
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchProductDetailData', currentRoute.params.slug)
  }

}
</script>

<style lang="sass">
.product-detail-wrapper
  display: grid
  grid-template-columns: 1fr 1fr

.product-header-text
  font-size: 22px
  font-weight: 700
  text-align: left

.product-info-section
  margin-top: 10px

.product-detail-price
  font-size: 30px

.product-detail-old-price
  font-size: 18px
  text-decoration: line-through

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


@media screen and (max-width: 1210px)
  .product-detail-wrapper
    grid-template-columns: 1fr

@media screen and (max-width: 650px)
  .product-header-text
    font-size: 16px
</style>
