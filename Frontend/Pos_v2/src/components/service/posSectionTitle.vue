<template>
<div class="section-title text-center">
  <h2 class="text-h5 text-weight-bold">
    {{ title }}
  </h2>
</div>
</template>

<script>
export default {
name: "posSectionTitle",
  props: {
    title: {
      type: String,
      default: null
    }
  }
}
</script>

<style lang="sass">

</style>
