<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el
        label="Услуги"
      />
    </q-breadcrumbs>
    <pos-page-header title="Наши услуги"/>
    <div class="q-mt-lg">
      <section
        v-for="category in serviceCategories"
        :key="category.id"
      >
        <pos-section-title :title="category.title" class="bg-grey-3 q-py-sm"/>
        <div class="">
          <pos-services-wrapper :services="category.services"/>
        </div>
      </section>
    </div>
    <pos-banners />
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosSectionTitle from "components/service/posSectionTitle";
import PosServicesWrapper from "components/services/posServicesWrapper";
import PosBanners from "components/shop/posBanners";

export default {
  name: "AllServices",
  components: {PosBanners, PosServicesWrapper, PosSectionTitle, PosPageHeader},
  computed: {
    serviceCategories() {
      return this.$store.getters.getAllServices
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchAllServices')
  },

  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Наши услуги | ${siteTitle}`
    }
  }
}
</script>

<style scoped>

</style>
