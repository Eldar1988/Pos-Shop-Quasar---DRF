<template>
  <section >
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
        // location.reload()
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
