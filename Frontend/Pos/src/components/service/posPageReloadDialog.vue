<template>
  <section class="q-pa-sm" v-if="serverUnloadedStatus">
    <q-card class="bg-dark text-white flex flex-center text-center">
      <q-card-section>
        Извините, соединение с сервером не установлено. {{ }}<br>
        <q-btn
          label="Перезагрузите страницу"
          class="q-mt-md text-weight-bold"
          outline
          @click="reload"
        />
      </q-card-section>
    </q-card>
  </section>
</template>

<script>
export default {
  name: "posPageReloadDialog",
  data() {
    return {
      dialog: true
    }
  },
  computed: {
    serverUnloadedStatus() {
      return this.$store.getters.getServerStatus
    }
  },
  mounted() {
    this.autoReload()
  },
  methods: {
    async reload() {
      setTimeout(() => {
        location.reload()
      }, 300)
    },
    autoReload() {
      let reload = setInterval(() => {
        this.$store.getters.getServerStatus ? this.$store.dispatch('fetchMainData') : clearInterval(reload)
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
