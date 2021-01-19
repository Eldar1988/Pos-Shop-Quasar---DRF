<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el
        v-if="category.parent"
        :label="category.parent.title"
        :to="`/shop/${category.parent.slug}`"
      />
      <q-breadcrumbs-el :label="category.title"/>
    </q-breadcrumbs>
    <pos-page-header :title="category.title"/>
    <!--    Category description   -->
    <section class="q-pa-sm">
      <q-card
        class="border-radius-6 grey-border shadow-0 q-px-sm q-pt-md q-pb-sm"
      >
        <p class="text-center q-pb-sm">{{ category.description }}</p>
        <q-expansion-item
          v-if="category.full_description"
          label="Подробнее"
          class="text-center text-bold text-uppercase border-radius-6"
        >
          <q-card>
            <div
              class="text-weight-regular category-full_description q-pa-sm"
              v-html="category.full_description"
            ></div>
          </q-card>
        </q-expansion-item>
      </q-card>
      <pos-categories
        :categories="category.child"
        class="q-mt-lg"
      />
    </section>
    <!--    xxxxx   -->
    <!--    Products   -->
    <section class="q-pa-sm q-mt-md">
      <pos-products-wrapper :products="category.products"/>

      <pos-products-wrapper
        v-for="child in category.child"
        :key="child.id"
        :products="child.products"
      />
    </section>
    <!--    xxxxx   -->
    <section>
      <pos-banners/>
    </section>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosCategories from "components/shop/posCategories";
import PosBanners from "components/shop/posBanners";

export default {
  name: "Shop",
  components: {PosBanners, PosCategories, PosProductsWrapper, PosPageHeader},
  computed: {
    category() {
      return this.$store.getters.getCategoryDetail
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchCategoryData', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.category-full_description
  text-transform: none
  text-align: left
</style>
