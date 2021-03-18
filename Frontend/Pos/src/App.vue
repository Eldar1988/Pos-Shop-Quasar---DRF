<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  mounted() {
    this.$q.notify.setDefaults({
      position: 'top',
      timeout: 4000,
      textColor: 'white',
      actions: [{ icon: 'close', color: 'white' }]
    })
  }
}
</script>
