<template>
<q-page>
  <q-breadcrumbs class="q-pa-sm q-mt-md">
    <q-breadcrumbs-el icon="home" to="/"/>
    <q-breadcrumbs-el label="Политика конфиденциальности"/>
  </q-breadcrumbs>
  <pos-page-header :title="policy.title" />
  <section class="info-page">
    <div v-html="policy.body" class="q-px-md q-py-xl bg-white"></div>
  </section>
</q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
export default {
  name: "PrivacyPolicy",
  components: {PosPageHeader},
  data() {
    return {
      policy: {}
    }
  },
  created() {
    this.loadPolicy()
  },
  methods: {
    async loadPolicy() {
      this.policy = await this.$axios.get(`${this.$store.getters.getServerURL}/privacy_policy/`).then(({data}) => {
        return data
      })
    }
  },
  meta() {
    let data = this.$store.getters.getAboutShopInfo
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Политика конфиденциальности | ${siteTitle}`,
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
          content: `Политика конфиденциальности | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/privacy_policy`,
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
