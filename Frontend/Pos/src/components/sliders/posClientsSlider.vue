<template>
  <section class="q-py-md section bg-white" v-if="clients.length > 5">
    <pos-section-title title="Наши клиенты" class="q-mb-md"/>
    <div class="brands-slide-grid">
      <div
        v-for="client in clients"
        :key="client.id"
      >
        <div class="brand-wrapper">
          <article>
            <div class="q-pa-sm border-radius-6">
              <q-img :src="client.logo" height="50px" contain :title="client.title" no-default-spinner>
                <template v-slot:loading><q-skeleton class="full-width" height="50px"/></template>
              </q-img>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import PosSectionTitle from "components/service/posSectionTitle";

export default {
  name: "posClientsSlider",
  components: {PosSectionTitle},
  computed: {
    clients() {
      return this.$store.getters.getClients
    }
  }
}
</script>

<style lang="sass">
.brands-slide-grid
  display: flex
  justify-content: center
  align-items: center
  flex-wrap: wrap

  .brand-wrapper
    min-width: 150px
    width: 150px
    padding: 5px

//@media screen and (max-width: 1444px)
//  .brands-slide-grid
//    grid-template-columns: repeat(5, 1fr)
//
//@media screen and (max-width: 1400px)
//  .brands-slide-grid
//    grid-template-columns: repeat(4, 1fr)
//
//@media screen and (max-width: 1100px)
//  .brands-slide-grid
//    grid-template-columns: repeat(3, 1fr)

@media screen and (max-width: 992px)
  .brands-slide-grid
    flex-wrap: nowrap
    overflow-x: scroll
    justify-content: start
    margin-left: 5px

    .brand-wrapper
      min-width: 150px
      width: 150px
      padding: 5px
</style>
