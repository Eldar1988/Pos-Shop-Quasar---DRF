<template>
  <section>
    <div class="categories-wrapper text-center justify-center">
      <div
        v-for="parentCategory in categoriesWithChild"
        :key="parentCategory.id"
      >
        <p class="text-bold q-pt-md category-card-title text-uppercase">{{ parentCategory.title }}</p>
      <article
        v-for="category in parentCategory.child"
        :key="category.id"
        class="category-card"
      >
        <router-link :to="`/shop/${category.slug}`">
          <q-card
            square
            style="min-height: 100%; display: grid; align-items: center"
            class="shadow-0 relative-position shadow-on-hover bg-white"
          >
            <div class="category-card-wrapper text-left">
              <div>
                <p class="text-bold category-card-title q-px-sm q-pt-sm" style="line-height: 1.2">{{ category.title }}</p>
                <p v-if="category.label" class="text-accent category-card-label q-px-sm q-pb-sm">
                  {{ category.label }}</p>
              </div>
              <div class="q-pa-sm text-right">
                <q-img
                  :src="category.image"
                  class="category-card-image"
                  cover
                  height="50px"
                  width="50px"
                >
                  <template v-slot:loading>
                    <q-skeleton class="full-width category-card-image" square/>
                  </template>
                </q-img>
              </div>
            </div>
          </q-card>
        </router-link>
      </article>
      </div>
      <div
        v-for="category in categoriesWithoutChild"
        :key="category.id"
      >
        <p class="text-bold q-pt-md category-card-title text-uppercase" style="opacity: 0">Разное</p>
        <article
          class="category-card"
        >
          <router-link :to="`/shop/${category.slug}`">
            <q-card
              square
              style="min-height: 100%; display: grid; align-items: center"
              class="shadow-0 relative-position shadow-on-hover bg-white"
            >
              <div class="category-card-wrapper text-left">
                <div>
                  <p class="text-bold category-card-title q-px-sm q-pt-sm" style="line-height: 1.2">{{ category.title }}</p>
                  <p v-if="category.label" class="text-accent category-card-label q-px-sm q-pb-sm">
                    {{ category.label }}</p>
                </div>
                <div class="q-pa-sm text-right">
                  <q-img
                    :src="category.image"
                    class="category-card-image"
                    cover
                    height="50px"
                    width="50px"
                  >
                    <template v-slot:loading>
                      <q-skeleton class="full-width category-card-image" square/>
                    </template>
                  </q-img>
                </div>
              </div>
            </q-card>
          </router-link>
        </article>
      </div>
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
    },
    categoriesWithChild() {
      return this.$store.getters.getCategories.filter(item => item.child.length > 0)
    },
    categoriesWithoutChild() {
      return this.$store.getters.getCategories.filter(item => !item.parent && item.child.length === 0)
    }
  }
}
</script>

<style lang="sass">
.category-card-title
  font-size: 14px

.category-card-label
  font-size: 14px !important
  line-height: 1.2 !important

.category-card-wrapper
  display: grid
  grid-template-columns: 2fr 1fr
  align-items: center

.categories-wrapper
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-gap: 10px

.category-card
  margin-top: 10px


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

  .category-card
    margin-top: 5px

  .category-card-title
    font-size: 14px

  .category-card-label
    padding-top: 7px
    font-size: 12px !important
    line-height: 1.2 !important

  .category-card-wrapper
    grid-template-columns: 3fr 1fr

</style>
