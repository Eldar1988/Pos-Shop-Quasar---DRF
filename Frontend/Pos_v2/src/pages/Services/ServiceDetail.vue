<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el to="/services" label="Услуги"/>
      <q-breadcrumbs-el :to="`/service_category/${service.category.slug}`" :label="service.category.title"/>
      <q-breadcrumbs-el :label="service.title"/>
    </q-breadcrumbs>
    <section class="q-pa-sm">
      <article>
<!--        Service image   -->
        <q-img
          :src="service.image"
          class="service-detail-image"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width service-detail-image" square/>
          </template>
        </q-img>

<!--        Title   -->
        <pos-section-title :title="service.title" class="q-mt-lg"/>

<!--        Body   -->
        <div class="bg-white q-mt-lg q-px-md q-py-lg">
          <div v-html="service.body"></div>
          <pos-share :title="service.title" :image="service.image" class="q-mt-xl" />
        </div>

<!--        Benefits   -->
        <div class="service-benefits-wrapper q-mt-xl">
          <q-card
            v-for="benefit in service.benefits"
            :key="benefit.id"
            square dark
            class="shadow-0 service-benefit-card bg-primary q-pa-md text-center"
          >
            <p class="text-bold">{{ benefit.title }}</p>

          </q-card>
        </div>

      </article>
    </section>
  </q-page>
</template>

<script>
import PosSectionTitle from "components/service/posSectionTitle";
import PosShare from "components/service/posShare";
export default {
  name: "ServiceDetail",
  components: {PosShare, PosSectionTitle},
  computed: {
    service() {
      return this.$store.getters.getService
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchServiceDetail', currentRoute.params.id)
  },

  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    let title = this.$store.getters.getService.title
    return {
      title: `${title} | ${siteTitle}`
    }
  }
}
</script>

<style lang="sass">
.service-detail-image
  height: 60vh

.service-benefits-wrapper
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 10px

.service-benefit-card

@media screen and (max-width: 650px)
  .service-detail-image
    height: 250px
</style>
