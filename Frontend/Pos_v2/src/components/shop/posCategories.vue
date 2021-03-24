<template>
  <section>
    <div class="categories-wrapper text-center justify-center">
      <article
        v-for="category in categories || defaultCategories"
        :key="category.id"
        class="category-card"
      >
        <router-link :to="`/shop/${category.slug}`">
          <q-card
            square
            class="shadow-0 q-px-sm relative-position shadow-on-hover bg-white"
          >
            <div class="category-card-wrapper text-left">
              <div>
                <p class="text-bold category-card-title">{{ category.title }}</p>
                <p v-if="category.label" class="text-accent category-card-label">
                  {{ category.label }}</p>
              </div>
              <div class="q-py-md text-right">
                <q-img
                  :src="category.image"
                  class="category-card-image"
                  width="100%"
                  height="70px"
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
  },
  computed: {
    defaultCategories() {
      return this.$store.getters.getCategories
    }
  }
}
</script>

<style lang="sass">
.category-card-title
  font-size: 16px

.category-card-label
  padding-top: 7px
  font-size: 14px !important
  line-height: 1.2 !important

.category-card-wrapper
  display: grid
  grid-template-columns: 2fr 1fr
  align-items: center

.categories-wrapper
  display: grid
  grid-template-columns: repeat(5, 1fr)
  grid-gap: 10px

.category-card
  min-height: 100%

.category-card-image
  height: 150px

@media screen and (max-width: 1500px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr 1fr 1fr

@media screen and (max-width: 1280px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr 1fr

@media screen and (max-width: 650px)
  .categories-wrapper
    grid-template-columns: 1fr 1fr
    grid-gap: 5px

  .category-card-title
    font-size: 14px

  .category-card-label
    padding-top: 7px
    font-size: 12px !important
    line-height: 1.2 !important

  .category-card-wrapper
    grid-template-columns: 3fr 1fr

</style>
