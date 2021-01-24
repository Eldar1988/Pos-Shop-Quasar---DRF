<template>
  <q-page class="flex flex-center column">
    <div class="text-center">
      <pos-page-header title="Спасибо!"/>
      <q-card
        class="border-radius-6 q-px-sm q-py-lg text-center bg-positive text-white green-shadow"
        style="width: 300px; max-width: 300px; margin: auto"
      >
        <div v-html="thanksText"></div>

      </q-card>
      <q-btn label="На главную" icon="home" color="accent" class="q-mt-xl q-px-md border-radius-6 text-bold" unelevated to="/"/>
    </div>
  </q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";

export default {
  name: "Thanks",
  components: {PosPageHeader},
  data() {
    return {
      thanksText: ''
    }
  },
  created() {
    if (this.$route.params.slug === 'callback') {
      this.thanksText = '<p>Ваша заявка принята<br>Мы свяжемся с Вами в ближайшее время</p>'
    } else {
      this.thanksText = '<p>Ваш заказ принят в обработку<br>Мы свяжемся с Вами в ближайшее время</p>'
    }
  },
  mounted() {
    window.scrollTo(0,0)
  },
  meta() {
    return {
      title: `Спасибо!`,
    }
  }
}
</script>

<style scoped>

</style>
