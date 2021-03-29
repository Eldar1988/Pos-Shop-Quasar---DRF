<template>

    <q-card
      square
      class="shadow-0 bg-white"
      style="min-height: 100%"
    >
      <article>
      <router-link :to="`/service/${service.id}`">
        <q-img
          :src="service.miniature"
          height="250px"
        >
          <template v-slot:loading>
            <q-skeleton class="full-width" height="250px" square/>
          </template>
        </q-img>
        <div class="q-pa-sm">
          <h3 class="service-card-title">{{ service.title }}</h3>
          <p class="ellipsis-2-lines q-pt-sm">{{ service.description }}</p>
        </div>
      </router-link>
      </article>
    </q-card>

</template>

<script>
export default {
  name: "posServiceCard",
  props: {
    service: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.service-card-title
  font-size: 18px
  font-weight: 700

@media screen and (max-width: 800px)
  .service-card-title
    font-size: 14px
</style>
