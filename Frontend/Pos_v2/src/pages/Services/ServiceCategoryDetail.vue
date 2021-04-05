<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el
        :label="serviceCategory.title"
      />
    </q-breadcrumbs>
    <section>
      <pos-page-header :title="serviceCategory.title"/>
      <div class="q-px-sm">
        <div class="q-px-sm q-py-md bg-white">
          <div style="max-width: 100%; width: 500px; margin: auto">
            <p class="text-center">{{ serviceCategory.description }}</p>
          </div>
        </div>
      </div>
    </section>
    <div class="q-pa-sm">
      <section>
        <pos-services-wrapper :services="serviceCategory.services"/>
      </section>
    </div>
    <pos-banners/>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosServicesWrapper from "components/services/posServicesWrapper";
import PosBanners from "components/shop/posBanners";

export default {
  name: "posServiesCategoryDetail",
  components: {PosBanners, PosServicesWrapper, PosPageHeader},
  computed: {
    serviceCategory() {
      return this.$store.getters.getServiceCategoryDetail
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchServiceCategoryDetail', currentRoute.params.slug)
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    let serviceCategory = this.$store.getters.getServiceCategoryDetail
    return {
      title: `${serviceCategory.title} | ${siteTitle}`
    }
  }
}
</script>

<style scoped>

</style>
