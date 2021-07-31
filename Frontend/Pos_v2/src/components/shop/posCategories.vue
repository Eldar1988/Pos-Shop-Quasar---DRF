<template>
  <section>
    <div class="categories-wrapper text-center justify-center">
      <!--      main categories-->
      <div
        v-for="parentCategory in categoriesWithChild"
        :key="parentCategory.id"
      >
        <q-card
          square
          style="min-height: 100%; display: grid; align-items: center"
          class="shadow-0 relative-position shadow-on-hover bg-white cursor-pointer"
          @click="showChildCategories (parentCategory)"
        >
          <div class="category-card-wrapper text-left q-px-md">
            <div>
              <p class="category-card-title q-px-sm text-bold" style="line-height: 1.2">{{
                  parentCategory.title
                }}</p>
              <p v-if="parentCategory.label" class="text-accent category-card-label q-px-sm q-pb-sm">
                {{ parentCategory.label }}</p>
            </div>
            <div class="q-pa-sm text-right">
              <q-img
                :src="parentCategory.image"
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
      </div>
      <!--      categories-->
      <div
        v-for="category in categoriesWithoutChild"
        :key="category.id"
      >
        <q-card
          square
          style="min-height: 100%; display: grid; align-items: center"
          class="shadow-0 relative-position shadow-on-hover bg-white cursor-pointer"
        >
          <router-link :to="`/shop/${category.slug}`">
            <div class="category-card-wrapper text-left q-px-md">
              <div>
                <p class="category-card-title q-px-sm text-bold" style="line-height: 1.2">{{
                    category.title
                  }}</p>
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
          </router-link>
        </q-card>
      </div>
    </div>
    <q-dialog v-model="dialog" maximized>
      <q-card
        square
        style="width: 992px; max-width: 100%"
        class="bg-grey-2"
      >
        <q-toolbar
          class="bg-primary text-white"
        >
          <q-toolbar-title class="text-subtitle1">{{ dialogCardTitle }}</q-toolbar-title>
          <q-btn icon="close" dense flat v-close-popup/>
        </q-toolbar>
        <q-scroll-area style="height: 85vh">
          <q-card-section>
            <div class="row q-col-gutter-md">
              <div
                v-for="category in childCategories"
                :key="category.id"
                class="col-md-6 col-12"
              >
                <q-card
                  square
                  style="min-height: 100%; display: grid; align-items: center"
                  class="shadow-0 relative-position shadow-on-hover bg-white cursor-pointer"
                >
                  <q-item :to="`/shop/${category.slug}`" class="q-pa-none">
                    <div class="flex no-wrap" style="align-items: center">
                      <div class="q-pa-sm">
                        <q-img
                          :src="category.image"
                          class="category-card-image"
                          cover
                          height="70px"
                          width="70px"
                        >
                          <template v-slot:loading>
                            <q-skeleton class="full-width category-card-image" square/>
                          </template>
                        </q-img>
                      </div>
                      <div>
                        <p class="ccategory-card-title q-px-sm text-bold" style="line-height: 1.2">
                          {{ category.title }}</p>
                        <p v-if="category.label" class="text-accent category-card-label q-px-sm q-pb-sm">
                          {{ category.label }}</p>
                      </div>
                    </div>
                  </q-item>
                </q-card>
              </div>
            </div>
          </q-card-section>
        </q-scroll-area>
      </q-card>
    </q-dialog>
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
      let categories = this.$store.getters.getCategories.filter(item => item.child.length > 0)
      categories.sort((a, b) => {
        return b.child.length - a.child.length
      })
      return categories
    },
    categoriesWithoutChild() {
      return this.$store.getters.getCategories.filter(item => !item.parent && item.child.length === 0)
    }
  },
  methods: {
    showChildCategories(category) {
      this.childCategories = category.child
      this.dialogCardTitle = category.title
      this.dialog = true
    }
  },
  data() {
    return {
      childCategories: [],
      dialog: false,
      dialogCardTitle: ''
    }
  },
}
</script>

<style lang="sass">
.category-card-title
  font-size: 16px

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

@media screen and (max-width: 992px)
  .category-card-title
    font-size: 14px

@media screen and (max-width: 650px)
  .categories-wrapper
    grid-template-columns: 1fr
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
