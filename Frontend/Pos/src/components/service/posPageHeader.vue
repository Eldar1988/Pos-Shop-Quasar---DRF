<template>
  <section class="page-header q-pa-sm">
    <div
      v-if="title"
      class="shadow-lt border-radius-6 q-pa-md"
    >
      <h1 class="page-header-text">{{ title }}</h1>
    </div>
  </section>
</template>

<script>
export default {
  name: "posPageHeader",
  props: {
    title: {
      type: String,
      default: null
    }
  }
}
</script>

<style lang="sass">
.page-header-text
  font-size: 22px
  font-weight: 700
  text-align: center


@media screen and (max-width: 650px)
  .page-header-text
    font-size: 16px
</style>
