<template>
  <q-page>
    <pos-page-header :title="pageData.title"/>
    <section class="info-page">
      <div v-html="pageData.body" class="border-radius-6 q-px-md q-py-md grey-border"></div>
    </section>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";

export default {
  name: "InfoPage",
  components: {PosPageHeader},
  computed: {
    pageData() {
      return this.$store.getters.getPageData
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchPageData', currentRoute.params.slug)
  },
  meta() {
    let data = this.$store.getters.getPageData
    return {
      title: data.title,
      meta: {
        description: {
          name: "description",
          content: data.description,
        }
      }
    }
  }

}
</script>

<style scoped>

</style>
