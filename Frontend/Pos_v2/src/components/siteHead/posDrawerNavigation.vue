<template>
  <nav class="bg-grey-2">
    <q-toolbar class="bg-grey-2">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Магазин</q-toolbar-title>
    </q-toolbar>
    <q-list class="bg-grey-2">
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
            <q-skeleton height="20px" square/>
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
            <q-item-section avatar >
              <q-img :src="category.image" class="br-0"/>
            </q-item-section>
            <q-item-section><span class="text-subtitle1 text-dark">{{ category.title }}</span>
            </q-item-section>
          </template>
          <!--          Childs    -->
          <q-item
            v-for="category in category.child"
            :key="category.id"
            clickable
            v-ripple
            class=""
            :to="`/shop/${category.slug}`"
            exact-active-class="text-primary"
            :title="category.title"
          >
            <q-item-section avatar>
              <q-img :src="category.image" class="br-0"/>
            </q-item-section>
            <q-item-section class="text-dark">{{ category.title }}</q-item-section>
          </q-item>
          <q-separator inset=""/>
          <q-item
            clickable
            v-ripple
            class=""
            :to="`/shop/${category.slug}`"
            exact-active-class="text-primary"
            :title="category.title"
          >
            <q-item-section avatar>
              <q-img :src="category.image" class="br-0"/>
            </q-item-section>
            <q-item-section class="text-subtitle1 text-dark">
              Все {{
                category.title.toLowerCase()
              }}
            </q-item-section>
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
            <q-img :src="category.image" class="br-0" contain/>
          </q-item-section>
          <q-item-section class="text-subtitle1 text-dark">{{ category.title }}</q-item-section>
        </q-item>
      </div>
      <!--    xxxxx   -->
    </q-list>

    <q-toolbar class="bg-grey-2 q-pt-md">
      <q-toolbar-title class="text-uppercase text-weight-bold text-subtitle1 letter-5">Информация</q-toolbar-title>
    </q-toolbar>
    <!--    Info Pages   -->
    <q-list class="bg-grey-2 q-mt-md">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
        <q-item-section class="text-subtitle1">
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
    pages() {
      return this.$store.getters.getPages
    },
    categories() {
      return this.$store.getters.getCategories
    }
  },
  created() {
    this.$store.dispatch('fetchCategories')
  },
}
</script>

<style lang="sass">
.menu-item
  border-radius: 0
  width: 95%
  margin: 0 auto 5px
  background: #ffffff
</style>
