<template>
  <nav>
    <q-toolbar class="bg-grey-4">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Магазин</q-toolbar-title>
    </q-toolbar>
    <q-list>
      <!--    Category skeletons-->
      <div v-if="categories.length < 1">
        <q-item
          clickable
          v-ripple
          v-for="(i, index) in 10"
          :key="index"
          class="menu-item"
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
        <!--        Parent category   -->
        <q-expansion-item
          v-if="category.child.length > 0"
          expand-separator
          icon="perm_identity"
          :label="category.title"
          class="menu-item"
        >
          <template v-slot:header>
            <q-item-section avatar>
              <q-img :src="category.image" class="border-radius-6"/>
            </q-item-section>
            <q-item-section><span class="text-subtitle2 text-weight-bold text-dark">{{ category.title }}</span>
            </q-item-section>
          </template>
          <!--          Childs    -->
          <q-item
            clickable
            v-ripple
            class="q-ml-sm"
            :to="`/shop/${category.slug}`"
            exact-active-class="text-primary"
            :title="category.title"
          >
            <q-item-section class="text-subtitle2 text-weight-bold text-dark">Все {{
                category.title.toLowerCase()
              }}
            </q-item-section>
          </q-item>
          <q-item
            v-for="category in category.child"
            :key="category.id"
            clickable
            v-ripple
            class="q-ml-sm"
            :to="`/shop/${category.slug}`"
            exact-active-class="text-primary"
            :title="category.title"
          >
            <q-item-section avatar>
              <q-img :src="category.image" class="border-radius-6"/>
            </q-item-section>
            <q-item-section class="text-dark">{{ category.title }}</q-item-section>
          </q-item>

        </q-expansion-item>
        <!--        xxxxx   -->

        <q-item
          v-if="category.parent === null && category.child.length === 0"
          clickable
          v-ripple
          class="menu-item"
          :to="`/shop/${category.slug}`"
          exact-active-class="text-primary"
          :title="category.title"
        >
          <q-item-section avatar>
            <q-img :src="category.image" class="border-radius-6" contain />
          </q-item-section>
          <q-item-section class="text-subtitle2 text-weight-bold text-dark">{{ category.title }}</q-item-section>
        </q-item>
      </div>
      <!--    xxxxx   -->
    </q-list>

    <q-toolbar class="bg-grey-4 q-mt-md">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Информация</q-toolbar-title>
    </q-toolbar>
    <!--    Info Pages   -->
    <q-list>
      <!--      Home   -->
      <q-item
        clickable
        v-ripple
        class="text-dark menu-item"
        exact-active-class="text-primary"
        to="/"
        title="Перейти на главную"
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
        class="menu-item"
        exact-active-class="text-primary"
        to="/about"
        title="Информация о магазине"
      >
        <q-item-section avatar>
          <q-icon name="store"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          О магазине
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Questions   -->
      <q-item
        clickable
        v-ripple
        class="menu-item"
        exact-active-class="text-primary"
        to="/questions"
        title="Часто задаваемые вопросы и ответы на них"
      >
        <q-item-section avatar>
          <q-icon name="question_answer"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          Вопросы и ответы
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Questions   -->
      <q-item
        clickable
        v-ripple
        class="menu-item"
        exact-active-class="text-primary"
        to="/files"
        title="Файлы для загрузки"
      >
        <q-item-section avatar>
          <q-icon name="cloud_download"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          Файлы
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Contacts   -->
      <q-item
        clickable
        v-ripple
        class="menu-item"
        exact-active-class="text-primary"
        to="/contacts"
        title="Контактная информация"
      >
        <q-item-section avatar>
          <q-icon name="place"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          Контакты
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Pages   -->
      <q-item
        v-for="page in pages"
        :key="page.id"
        clickable
        v-ripple
        class="menu-item"
        :to="`/info/${page.slug}`"
        :title="page.title"
      >
        <q-item-section avatar>
          <q-icon name="keyboard_arrow_right"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          {{ page.title }}
        </q-item-section>
      </q-item>
      <!--      xxxxx   -->
      <!--      Privacy policy   -->
      <q-item
        clickable
        v-ripple
        class="menu-item"
        exact-active-class="text-primary"
        to="/privacy_policy"
      >
        <q-item-section avatar>
          <q-icon name="assignment"/>
        </q-item-section>
        <q-item-section class="text-subtitle2 text-weight-bold">
          Политика конфиденциальности
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

<style lang="sass">
.menu-item
  border-radius: 10px
  box-shadow: rgba(99, 99, 99, 0.05) 0px 2px 11px 0px
  width: 95%
  margin: 10px auto 0
</style>
