<template>
  <div>
    <div class="categories-wrapper text-center justify-center">
      <article
        v-for="category in categories"
        :key="category.id"
        class="category-card"
      >
        <q-card
          class="grey-border shadow-0 q-pa-sm relative-position"
          style="min-height: 100%"
        >
          <q-img
            :src="category.image"
            class="category-card-image"
            contain
          />
          <p class="text-bold q-pt-sm">{{ category.title }}</p>
        </q-card>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: "posCategories",
  props: {
    categories: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.categories-wrapper
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 5px

.category-card
  min-height: 100%

.category-card-image
  height: 150px

@media screen and (max-width: 800px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr 1fr

@media screen and (max-width: 650px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr
    grid-gap: 3px

</style>
