<template>
  <section>
    <div class="categories-wrapper text-center justify-center">
      <article
        v-for="category in categories"
        :key="category.id"
        class="category-card"
      >
        <router-link :to="`/shop/${category.slug}`">
        <q-card
          class="grey-border shadow-0 q-py-sm q-px-md relative-position shadow-on-hover border-radius-6"
          style="min-height: 100%"
        >
          <div class="category-card-wrapper">
            <div>
              <p class="text-bold q-pt-sm text-left q-pb-sm">{{ category.title }}</p>
              <p v-if="category.label" class="category-card-label bg-accent text-left border-radius-6 text-bold">{{ category.label }}</p>
            </div>
            <div>
          <q-img
            :src="category.image"
            class="category-card-image border-radius-6"
            contain
          />
            </div>

          </div>
        </q-card>
        </router-link>
      </article>
    </div>
  </section>
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
.category-card-wrapper
  display: grid
  grid-template-columns: 2fr 1fr
  align-items: center

.category-card-label
  color: white
  display: flex
  justify-content: center
  align-items: center
  padding: 5px 5px
  width: 90%

.categories-wrapper
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 5px

.category-card
  min-height: 100%

.category-card-image
  height: 150px

@media screen and (max-width: 1500px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr 1fr

@media screen and (max-width: 1280px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr

@media screen and (max-width: 650px)
  .categories-wrapper
    grid-template-columns: 1fr
    grid-gap: 3px

</style>
