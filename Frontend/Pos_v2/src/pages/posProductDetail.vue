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
    <script type="application/ld+json" v-html="schema"></script>
    <script type="application/ld+json" v-html="navigationSchema"></script>
    <!--    Product Detail   -->
    <article>
      <div class="product-detail-wrapper q-mt-sm">
        <div class="q-pa-sm">
          <!--          Slider   -->
          <pos-product-detail-images-slider
            :images="productData.product.images"
            :image="productData.product.full_image"
            :title="productData.product.title"
            :first-image-contain="productData.product.image_contain"
          />
          <!--          xxxxx   -->

        </div>
        <div class="q-pa-sm">
          <div class="flex justify-between" style="align-items: center">
            <!--            Title   -->
            <h1 class="product-header-text q-mt-sm">{{ productData.product.title }}</h1>
            <!--          Rating   -->
            <div v-if="productData.product.rating" class="q-mt-sm">
              <q-rating v-model="productData.product.rating" size="28px" color="orange" readonly
                        style="text-shadow: none !important;"/>
            </div>
          </div>
          <!--          Product price   -->
          <div v-if="productData.product.price" class="product-info-section">
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
          <!--          Shipping detail   -->
          <div class="product-info-section">
            <!--            <q-icon name="local_shipping" size="22px" class="q-mr-sm"/>-->
            <div class="text-bold" v-html="productData.product.shipping_detail">
            </div>
          </div>
          <!--          Article  -->
          <div v-if="productData.product.article" class="product-info-section">
            <p class="text-bold">
              Артикул: <span class="text-weight-regular">{{ productData.product.article }}</span>
            </p>
          </div>
          <!--            xxxxx   -->
          <!--          Actions   -->
          <div v-if="productData.product.in_stock_quantity > 0" class="row q-mt-md">
            <!--        Quantity   -->
            <div class="full-width flex justify-center q-mb-md">
              <div class="q-mt-sm">
                <div class="quantity-wrapper q-mt-sm">
                  <q-btn
                    icon="remove"
                    class=""
                    outline  dense
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
                    outline  dense
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
                @click="selfAddToCart(productData.product, quantity, true)"
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
                  @click="selfAddToCart(productData.product, quantity, false)"
                />
                <q-btn
                  color="accent"
                  @click="addToWishList(productData.product)"
                  text-color="accent"
                   unelevated flat
                  :icon="productInWishList ? 'favorite' : 'favorite_border'"
                />
              </div>
            </div>
            <!--            Kaspi button   -->
            <div v-if="this.$store.state.kaspiButton" class="q-mt-sm q-ml-sm" id="dynamic"></div>
            <!--            xxxxx   -->
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
          <!--          xxxxx   -->
          <!--           Category  Labels   -->
          <div class="">
            <!--          Category   -->
            <div class="q-pa-sm">
              <!--          Category   -->
              <div class="flex">
                <div class="flex product-info-section" style="align-items: center">
                  <q-btn
                    color="accent"
                    :label="productData.product.category.title"
                    size="sm" outline no-caps
                    class="text-bold"
                    :to="`/shop/${productData.product.category.slug}`"
                  />
                </div>
                <!--          Labels   -->
                <div v-if="productData.product.labels.length > 0" class="flex product-info-section"
                     style="align-items: center">
                  <q-btn
                    v-for="label in productData.product.labels"
                    :key="label.id"
                    :label="label.title"
                    size="sm" outline no-caps
                    class="q-ml-sm text-bold"
                    :to="`/label/${label.slug}`"
                  />
                </div>
              </div>
              <!--          xxxxx   -->
              <!--          xxxxx   -->
            </div>
            <!--          xxxxx   -->
          </div>
          <!--       Brand & Share  -->
          <div class="flex justify-between q-pr-sm q-pa-sm q-mt-sm" style="align-items: center">
            <div class="">
              <!--          Brand   -->
              <div v-if="productData.product.brand" class="product-info-section text-left">
                <router-link :to="`/brand/${productData.product.brand.slug}`">
                  <q-img :src="productData.product.brand.image" height="50px" width="150px" contain class=""
                         position="left" style="margin-top: -7px"/>
                </router-link>
              </div>
            </div>
            <!--            Share   -->
            <div class="">
              <pos-share
                class="" :description="productData.product.description"
                :image="productData.product.image"
              />
            </div>
          </div>
          <!--          xxxxx   -->
        </div>
      </div>

    </article>
    <!--    xxxxx   -->
    <!--          Reviews - Characters - More info   -->
    <div class="q-pa-sm">
      <q-tabs
        v-model="tab"
        align="justify"
        narrow-indicator
        class="q-mb-md home-tabs bg-white q-mt-sm"
        active-bg-color=""
        active-color="accent"
        indicator-color="accent"
      >
        <q-tab class="text-dark" name="reviews"
               :label="`Отзывы (${productData.product.reviews.length})`"
               icon="chat_bubble_outline"
        />
        <q-tab
          v-if="productData.product.characteristic"
          class="text-dark"
          name="characters"
          label="Характеристики"
          icon="tune"
        />
        <q-tab
          v-if="productData.product.info"
          class="text-dark"
          name="more"
          label="Подробнее"
          icon="search"
        />
      </q-tabs>
      <q-tab-panels
        swipeable
        v-model="tab"
        animated
        transition-prev="scale"
        transition-next="scale"
        class="bg-grey-2"
      >
        <q-tab-panel name="reviews">
          <pos-product-reviews :reviews="productData.product.reviews" :productId="`${productData.product.id}`"/>
        </q-tab-panel>

        <q-tab-panel name="characters">
          <q-card square>
            <q-card-section class="text-weight-regular text-left">
              <div
                v-html="productData.product.characteristic"
                style="overflow-x:scroll"
              >
              </div>
            </q-card-section>
          </q-card>
        </q-tab-panel>

        <q-tab-panel name="more">
          <q-card square>
            <q-card-section class="text-weight-regular text-left">
              <div
                v-html="productData.product.info"
                style="overflow-x:scroll"
              >
              </div>
            </q-card-section>
          </q-card>
        </q-tab-panel>
      </q-tab-panels>
    </div>
    <!--          xxxxx   -->
    <!--    Videos   -->
    <section v-if="productData.product.video" class="q-mt-lg">
      <div class="q-py-sm">
        <pos-section-title title="Видео обзор товара"/>
      </div>
      <div class="q-pa-sm">
        <q-video
          :ratio="this.$q.platform.is.mobile ? 16/10 : 16/6"
          :src="`https://www.youtube.com/embed/${productData.product.video}`"
          class="shadow-5"
        />
        <div
          v-for="video in productData.product.videos"
          :key="video.id"
        >
          <q-video
            :ratio="16/9"
            :src="`https://www.youtube.com/embed/${video.video}`"
            class="border-radius-6 q-mt-md"
          />
        </div>
      </div>

    </section>
    <!--    xxxxx   -->
    <!--    More products   -->
    <section v-if="productData.products.length > 0" class="q-py-xl bg-grey-2">
      <pos-section-title title="Смотрите также:" class="q-mt-md"/>
      <pos-products-slide-x :products="productData.products" class="q-mt-md"/>
    </section>
    <!--    xxxxx   -->
    <!--    Last sean products   -->
    <section v-if="lastSeanProducts" class="q-py-lg">
      <pos-section-title title="Вы недавно смотрели:"/>
      <pos-products-slide-x :products="lastSeanProducts" class="q-mt-md"/>
    </section>
    <!--    Banners   -->
    <pos-banners/>
    <!--   xxxxx   -->
    <!--    Latest Products   -->
    <section class="q-mt-xl">
      <pos-section-title title="Новинки"/>
      <pos-products-slide-x :products="this.$store.getters.getLatestProducts" class="q-mt-md"/>
    </section>
    <!--    xxxxx   -->
    <!--    Brands   -->
    <pos-brands-slider class="q-mt-xl"/>

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
import PosBanners from "components/shop/posBanners";
import addToCart from "src/functions/add_to_cart";
import PosAddedToCartDialog from "components/cart/posAddedToCartDialog";
import addToWishListFunc from "src/functions/add_to_wishlist";
import PosProductReviews from "components/shop/posProductReviews";
import PosShare from "components/service/posShare";
import PosBrandsSlider from "components/sliders/posBrandsSlider";
import PosProductsSlideX from "components/sliders/posProductsSlideX";

export default {
  name: "posProductDetail",
  components: {
    PosProductsSlideX,
    PosBrandsSlider,
    PosShare,
    PosProductReviews,
    PosAddedToCartDialog, PosBanners, PosSectionTitle, PosProductDetailImagesSlider
  },
  filters: {formatPrice},
  data() {
    return {
      lastSeanProducts: [],
      quantity: 1,
      cartDialog: false,
      productInWishList: false,
      tab: ''
    }
  },
  computed: {
    productData() {
      return this.$store.getters.getProductDetailData
    },
    getSaleSum: function () {
      let sum = this.productData.product.old_price - this.productData.product.price
      return `экономия ${sum} тенге`
    },
    navigationSchema() {
      return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
          "@type": "ListItem",
          "position": 1,
          "name": this.$store.getters.getProductDetailData.product.category.title,
          "item": `${this.$store.getters.getCompanyInfo.site_url}/shop/${this.$store.getters.getProductDetailData.product.category.slug}`
        },
          {
            "@type": "ListItem",
            "position": 2,
            "name": this.$store.getters.getProductDetailData.product.title,
            "item": `${this.$store.getters.getCompanyInfo.site_url}/product/${this.$store.getters.getProductDetailData.product.slug}`
          }]
      }
    },
    schema() {
      return {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": this.$store.getters.getProductDetailData.product.title,
        "image": [
          this.$store.getters.getProductDetailData.product.full_image
        ],
        "description": this.$store.getters.getProductDetailData.product.description,
        "sku": this.$store.getters.getProductDetailData.product.article,
        "mpn": "",
        "brand": {
          "@type": "Brand",
          "name": this.$store.getters.getProductDetailData.product.brand ? this.$store.getters.getProductDetailData.product.brand : this.$store.getters.getCompanyInfo.name
        },
        "review": {
          "@type": "Review",
          "reviewRating": {
            "@type": "Rating",
            "ratingValue": this.$store.getters.getProductDetailData.product.reviews[0] !== undefined ? this.$store.getters.getProductDetailData.product.reviews[0].rating : '5',
            "bestRating": "5"
          },
          "author": {
            "@type": "Person",
            "name": this.$store.getters.getProductDetailData.product.reviews[0] !== undefined ? this.$store.getters.getProductDetailData.product.reviews[0].name : 'Александр'
          }
        },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": this.$store.getters.getProductDetailData.product.rating,
          "reviewCount": this.$store.getters.getProductDetailData.product.reviews.length
        },
        "offers": {
          "@type": "Offer",
          "url": `${this.$store.getters.getCompanyInfo.site_url}/product/${this.productData.product.slug}`,
          "priceCurrency": "KZT",
          "price": this.$store.getters.getProductDetailData.product.price,
          "itemCondition": "https://schema.org/UsedCondition",
          "availability": "https://schema.org/InStock"
        }
      }
    }
  },

  mounted() {
    this.getLastSeanProducts()
    this.checkWishList()
    if (this.$store.state.kaspiButton) this.kaspiButton()
  },
  beforeUpdate() {
    this.setLastSeanProducts()
  },
  watch: {
    async productData() {
      await this.checkWishList()
      await this.getLastSeanProducts()
      if (this.$store.state.kaspiButton) this.kaspiButton()
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
        }, 4000)
      }
    },
    kaspiButton() {
      document.getElementById('dynamic').innerHTML = `<div class="ks-widget" data-template="button" data-merchant-sku="${this.productData.product.article}" data-merchant-code="Posshopkz" data-city="750000000" ></div>`
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
          if (item.id === this.productData.product.id) {
            this.productInWishList = true
          }
        })
      }
    },
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchProductDetailData', currentRoute.params.id)
  },
  meta() {
    let data = this.$store.getters.getProductDetailData.product
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `${data.title} | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: data.description,
        },
        ogType: {
          property: "og:type",
          content: "product",
        },
        ogTitle: {
          property: "og:title",
          content: `${data.title} | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/product/${this.productData.product.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: data.description,
        },
        ogImage: {
          property: "og:image",
          content: data.full_image
        }
      }
    }
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
  margin-top: 7px

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

.q-rating__icon
  text-shadow: none !important

@media screen and (max-width: 1210px)
  .product-detail-wrapper
    grid-template-columns: 1fr

@media screen and (max-width: 650px)
  .product-header-text
    font-size: 16px
</style>
