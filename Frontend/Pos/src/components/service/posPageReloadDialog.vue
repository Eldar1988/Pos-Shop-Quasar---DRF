<template>
<q-dialog v-model="dialog">
  <q-card class="bg-red text-white flex flex-center text-center" style="width: 500px; max-width: 90%; height: 200px">
    <q-card-section>
      Извините, произошла ошибка сервера.<br>
      <q-btn
        label="Перезагрузите страницу"
        class="q-mt-md text-weight-bold"
        outline
        @click="reload"
      />
    </q-card-section>
  </q-card>
</q-dialog>
</template>

<script>
export default {
  name: "posPageReloadDialog",
  props: {
    dialog: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    async reload() {
      setTimeout(() => {
        location.reload()
      }, 300)
    }
  }
}
</script>

<style scoped>

</style>
