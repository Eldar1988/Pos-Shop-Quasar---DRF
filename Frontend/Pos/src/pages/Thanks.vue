<template>
  <q-page class="flex flex-center column">
    <div class="text-center">
      <pos-page-header title="Спасибо!"/>
      <q-card
        class="border-radius-6 q-px-sm q-py-lg text-center bg-positive text-white green-shadow"
        style="width: 300px; max-width: 300px; margin: auto"
      >
        <p>Ваш заказ принят в обработку.<br>Мы свяжемся с Вами в ближайшее время</p>

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
}
</script>

<style scoped>

</style>
