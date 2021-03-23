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
            class="shadow-0 q-px-md relative-position shadow-on-hover border-radius-6 bg-white"
          >
            <div class="category-card-wrapper text-left">
              <div>
                <p class="text-bold text-subtitle1">{{ category.title }}</p>
                <p v-if="category.label" class="border-radius-6 text-bold text-accent">
                  {{ category.label }}</p>
              </div>
              <div class="q-py-md text-right">
                <q-img
                  :src="category.image"
                  class="category-card-image border-radius-6 shadow-lt"
                  width="70px"
                  height="70px"
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

.categories-wrapper
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 10px

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
    grid-gap: 10px

</style>
