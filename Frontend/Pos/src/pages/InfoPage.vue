<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el :label="pageData.title"/>
    </q-breadcrumbs>
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
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `${data.title} | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: data.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: data.title,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/info/${data.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: data.description,
        },
        ogImage: {
          property: "og:image",
          content: `${this.$store.getters.getCompanyInfo.logo}`
        }
      }
    }
  }

}
</script>

<style scoped>

</style>
