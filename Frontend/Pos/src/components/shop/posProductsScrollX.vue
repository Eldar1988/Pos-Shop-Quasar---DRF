<template>
  <section>
    <!--    Scroll controls   -->
    <div class="scroll-controls text-center q-mt-md">
      <q-btn
        @click="scrollLeft"
        icon="navigate_before"
        color="primary"
        class="border-radius-6"
        outline
        size="sm"
        :disable="position === 0"
      />
      <q-btn
        @click="scrollRight"
        icon="navigate_next"
        class="border-radius-6 q-ml-sm"
        outline
        size="sm"
        color="primary"
        :disable="disableRightScroll"
      />
    </div>
    <!--   xxxxx   -->
    <!--    Scroll Area   -->
    <q-scroll-area
      ref="refName"
      horizontal
      class="full-width q-mt-md scroll-x-products"
      :thumb-style="{ display: 'none' }"
    >
      <div class="row no-wrap">
        <div
          v-for="product in products"
          :key="product.id"
          class=""
          style="width: 250px; padding: 0 4px"
        >
          <pos-product-card :product="product" />
        </div>
      </div>
    </q-scroll-area>
    <!--   xxxxx   -->
  </section>
</template>

<script>
import PosProductCard from "components/shop/posProductCard";
export default {
  name: "posProductsScrollX",
  components: {PosProductCard},
  props: {
    products: {
      type: Array,
      default: null,
    },
    refName: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      position: 0,
      disableRightScroll: false
    }
  },
  methods: {
    // Скролл вправо
    scrollRight() {
      // Проверка: количество карточек * ширину экрана (98% ширина контейнера)
      if(this.position < this.products.length * 250 - (window.innerWidth * 0.99)) {
        this.position += 250
        this.$refs.refName.setScrollPosition(this.position, 300)
      } else {
        // Отключюение правого скролла
        this.disableRightScroll = true
      }
    },
    // Левый скролл
    scrollLeft() {
      if (this.position !== 0) {
        this.position = this.position - 250
        this.disableRightScroll = false
        this.$refs.refName.setScrollPosition(this.position, 300)
      }
    }
  }
}
</script>

<style lang="sass">
.scroll-x-products
  height: 450px

@media screen and (max-width: 800px)
  .scroll-x-products
    height: 420px
</style>
