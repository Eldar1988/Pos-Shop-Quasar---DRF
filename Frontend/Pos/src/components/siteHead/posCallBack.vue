<template>
<div>
  <q-btn
    label="Обратный звонок"
    icon-right="phone_callback"
    outline
    :color="color"
    class="text-weight-bold full-width"
  />
</div>
</template>

<script>
export default {
  name: "posCallBack",
  props: {
    color: {
      type: String,
      default: 'white'
    }
  }
}
</script>

<style scoped>

</style>
