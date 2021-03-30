<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el to="/services" label="Услуги"/>
      <q-breadcrumbs-el :to="`/service_category/${service.category.slug}`" :label="service.category.title"/>
      <q-breadcrumbs-el :label="service.title"/>
    </q-breadcrumbs>
    <section class="q-pa-sm info-page bg-white">
      <article>
        <!--        Service image   -->
        <q-img
          v-if="!service.video"
          :src="service.image"
          class="service-detail-image"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width service-detail-image" square/>
          </template>
        </q-img>
        <q-video
          :ratio="16/9"
          :src="`https://www.youtube.com/embed/${service.video}`"
          class="shadow-5"
        />
        <!--        Title   -->
        <pos-section-title :title="service.title" class="q-mt-lg"/>

        <!--        Body   -->
        <div class=" q-mt-lg q-px-md">
          <div v-html="service.body"></div>
        </div>

        <!--        Benefits   -->
        <div v-if="service.benefits" class="service-benefits-wrapper q-mt-xl">
          <q-card
            v-for="benefit in service.benefits"
            :key="benefit.id"
            square dark
            class="shadow-0 service-benefit-card bg-primary q-pa-md text-center"
          >
            <p class="text-bold q-pt-sm">{{ benefit.title }}</p>
            <p class="q-pt-md">{{ benefit.text }}</p>
          </q-card>
        </div>

        <!--        Slider   -->
        <div v-if="service.images && service.images.length > 0" class="q-mt-xl">
          <pos-service-detail-gallery-slider :images="service.images"/>
        </div>
        <pos-share :title="service.title" :image="service.image" class="q-mt-xl"/>
      </article>
    </section>
    <div class="q-mt-xl">
      <section class="info-page ">
        <pos-service-request-form :call-to-action-text="service.call_to_action" :btn-text="service.btn_text" :service-i-d="service.id"/>
      </section>
    </div>
  </q-page>
</template>

<script>
import PosSectionTitle from "components/service/posSectionTitle";
import PosShare from "components/service/posShare";
import PosServiceDetailGallerySlider from "components/services/posServiceDetailGallerySlider";
import PosServiceRequestForm from "components/services/posServiceRequestForm";

export default {
  name: "ServiceDetail",
  components: {PosServiceRequestForm, PosServiceDetailGallerySlider, PosShare, PosSectionTitle},
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
  height: 50vh

.service-benefits-wrapper
  display: grid
  grid-template-columns: repeat(3, 1fr)
  grid-gap: 10px

@media screen and (max-width: 650px)
  .service-detail-image
    height: 250px

  .service-benefits-wrapper
    grid-template-columns: repeat(1, 1fr)
</style>
