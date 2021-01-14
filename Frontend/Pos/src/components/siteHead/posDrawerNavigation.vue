<template>
  <nav>
    <q-toolbar class="bg-grey-4">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Категории</q-toolbar-title>
    </q-toolbar>
    <q-list>
      <!--    Category skeletons-->
      <div v-if="categories.length < 1">
        <q-item
          clickable
          v-ripple
          v-for="(i, index) in 10"
          :key="index"
          class="border-bottom"
        >
          <q-item-section avatar>
            <q-skeleton type="circle" width="30px" height="30px"/>
          </q-item-section>

          <q-item-section>
            <q-skeleton height="20px"/>
          </q-item-section>
        </q-item>
      </div>
      <!--    xxxxx   -->
      <!--    Categories   -->
      <div
        v-for="category in categories"
        :key="category.id"
      >
        <q-item
          clickable
          v-ripple
          v-if="!category.parent"
          class="border-bottom"
        >
          <q-item-section avatar>
            <q-img :src="category.image" class="circle-image"/>
          </q-item-section>
          <q-item-section class="text-subtitle2 text-weight-bold text-dark">{{ category.title }}</q-item-section>
        </q-item>
      </div>
      <!--    xxxxx   -->
    </q-list>

    <q-toolbar class="bg-grey-4">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Информация</q-toolbar-title>
    </q-toolbar>
    <!--    Info Pages   -->
    <q-list>
      <!--      Home   -->
      <q-item
        clickable
        v-ripple
        class="border-bottom"
      >
        <q-item-section avatar>
          <q-icon name="home"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          Главная
        </q-item-section>
      </q-item>
      <!--   xxxxx   -->
      <!--      About   -->
      <q-item
        clickable
        v-ripple
        class="border-bottom"
      >
        <q-item-section avatar>
          <q-icon name="store"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          О магазине
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Pages   -->
      <q-item
        v-for="page in pages"
        :key="page.id"
        clickable
        v-ripple
        class="border-bottom"
      >
        <q-item-section avatar>
          <q-icon name="keyboard_arrow_right"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          {{ page.title }}
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
    </q-list>
    <!--    xxxxx   -->
  </nav>
</template>

<script>
export default {
  name: "posDrawerNavigation",
  computed: {
    categories() {
      return this.$store.getters.getCategories
    },
    pages() {
      return this.$store.getters.getPages
    }
  }
}
</script>

<style scoped>

</style>
