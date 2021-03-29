<template>
<div class="services-grid q-mt-md q-pa-sm">
  <div
    v-for="service in services"
    :key="service.id"
  >
    <pos-service-card :service="service"/>
  </div>
</div>
</template>

<script>
import PosServiceCard from "components/services/posServiceCard";
export default {
  name: "posServicesWrapper",
  components: {PosServiceCard},
  props: {
    services: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.services-grid
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 15px

@media screen and (max-width: 1440px)
  .services-grid
    grid-template-columns: repeat(3, 1fr)

@media screen and (max-width: 992px)
  .services-grid
    grid-template-columns: repeat(2, 1fr)

@media screen and (max-width: 650px)
  .services-grid
    grid-template-columns: repeat(1, 1fr)
</style>
