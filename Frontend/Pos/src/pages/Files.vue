<template>
  <q-page>
    <q-breadcrumbs class="q-pa-sm q-mt-md">
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el label="Файлы"/>
    </q-breadcrumbs>
    <pos-page-header title="Файлы"/>
    <section class="info-page">
      <div
        v-for="file in files"
        :key="file.id"
        class="border-radius-6 grey-border q-pa-sm q-mt-sm flex justify-between no-wrap"
        style="align-items: center"
      >
        <div>
        <p class="text-bold">{{ file.title }}</p>
          <small>{{ file.description }}</small>
        </div>
        <div class="flex no-wrap">
          <a :href="file.file">
            <q-btn
              label="Скачать"
              class="border-radius-6 text-bold"
              color="accent"
              unelevated
              size="sm"
              icon-right="cloud_download"
            />
          </a>
        </div>
      </div>
    </section>
    <!--    Empty wish list alert   -->
    <section
      v-if="files.length === 0"
      class="info-page"
    >
      <q-card
        class="bg-negative red-shadow q-px-sm q-py-xl flex flex-center q-mt-md"
      >
        <div class="text-center">
          <p class="text-subtitle1 text-white">
            Извините, файлов не найдено.
          </p>
          <q-btn
            label="вернуться в магазин"
            outline
            color="white"
            class="border-radius-6 q-mt-md text-bold"
            to="/"
          />
        </div>
      </q-card>
    </section>
    <!--    xxxxx   -->
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";

export default {
  name: "Files",
  components: {PosPageHeader},
  data() {
    return {
      files: [],
      showing: false
    }
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Файлы | ${siteTitle}`
    }
  },
  created() {
    this.loadFiles()
  },
  methods: {
    async loadFiles() {
      this.files = await this.$axios.get(`${this.$store.getters.getServerURL}/files/`)
        .then(({data}) => {
          return data
        })
    }
  }
}
</script>

<style scoped>

</style>
