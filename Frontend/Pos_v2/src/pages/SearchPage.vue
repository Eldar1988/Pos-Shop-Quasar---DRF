<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el label="Страница поиска"/>
    </q-breadcrumbs>
    <pos-page-header title="Поиск по магазину"/>
    <q-card
      square
      class="q-pa-md shadow-0"
      style="width: 500px; max-width: 90%; margin: auto"
    >
      <q-input v-model="search" label="Введите запрос" class="q-mt-md"/>
      <small v-if="search.length < 3" class="text-red">{{ errorText }}</small>
      <q-btn
        label="Поиск"
        class="q-mt-lg full-width q-py-sm text-bold"
        icon-right="search"
        color="accent"
        unelevated
        @click="startSearch"
      />
    </q-card>

    <section class="q-pa-sm q-mt-xl">

      <p class="text-subtitle1" v-if="products > 0">{{ `Результаты по запросу '${search}'` }}</p>
      <p class="text-bold text-center text-subtitle1">{{ searchText }}</p>
      <pos-products-wrapper class="q-mt-md" :products="products"/>
    </section>
    <div class="q-pa-sm q-mt-xl">
      <pos-categories/>
    </div>
    <pos-brands-slider class="q-mt-xl"/>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosProductsWrapper from "components/shop/posProductsWrapper";
import PosCategories from "components/shop/posCategories";
import PosBrandsSlider from "components/sliders/posBrandsSlider";

export default {
  name: "SearchPage",
  components: {PosBrandsSlider, PosCategories, PosProductsWrapper, PosPageHeader},
  data() {
    return {
      search: '',
      errorText: '',
      products: [],
      searchText: '',
      loading: false
    }
  },
  methods: {
    async startSearch() {
      if (this.search.length < 3) {
        this.errorText = 'В запросе должно быть не менее 3 символов'
        return null
      }
      this.loading = true
      this.products = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/search/?search=${this.search}`)
        .then(({data}) => {
          if (data.length === 0) {
            this.searchText = 'Результатов по вашему запросу не найдено'
          } else {
            this.searchText = `Результаты поиска по запросу "${this.search}"`
            this.loading = false
            return data
          }
        })
    }
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Поиск по магазину | ${siteTitle}`
    }
  }
}
</script>

<style scoped>

</style>
