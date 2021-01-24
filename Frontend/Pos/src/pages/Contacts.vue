<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el label="Контакты"/>
    </q-breadcrumbs>
    <pos-page-header :title="contacts.title"/>
    <section class="info-page">
      <p class="text-center text-bold q-pb-lg">{{ contacts.description }}</p>
      <div class="border-radius-6 q-px-md q-py-md grey-border">
        <p class="text-bold">Телефон: <a :href="`tel:${contacts.phone}`" class="text-weight-regular">{{ contacts.phone }}</a></p>
        <p class="text-bold q-pt-sm">Whatsapp: <a :href="`https://wa.me/${contacts.whatsapp}`" target="_blank" class="text-weight-regular">{{ contacts.whatsapp }}</a></p>
        <p class="text-bold q-pt-sm">Адрес: <span class="text-weight-regular">{{ contacts.address }}</span></p>
        <div v-html="contacts.body" class="q-mt-lg"></div>
        <pos-share class="q-mt-lg"/>
      </div>
      <div v-html="contacts.map_frame" class="q-mt-lg border-radius-6 shadow-lt"></div>
    </section>

  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosShare from "components/service/posShare";

export default {
  name: "Contacts",
  components: {PosShare, PosPageHeader},
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  },
  meta() {
    let data = this.$store.getters.getContacts
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
          content: `${data.title} | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/contacts`,
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

<style lang="sass">
iframe
  min-width: 100% !important
</style>
