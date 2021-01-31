<template>
  <div class="fullscreen bg-blue text-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 30vh">
        404
      </div>

      <div class="text-subtitle1" style="opacity:.4">
        Извините, страница не найдена
      </div>

      <q-btn
        class="q-mt-xl border-radius-6 text-bold"
        color="white"
        text-color="dark"
        unelevated
        to="/"
        label="На главную"
        icon="home"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Error404'
}
</script>
