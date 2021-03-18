<template>
  <footer class="q-mb-sm q-px-sm">
    <div class="grey-border border-radius-6 text-center text-white q-pb-md q-px-sm bg-info">
      <div class="q-pt-lg" style="max-width: 700px; margin: auto;">
        <p class="text-subtitle1 text-bold q-pt-lg">{{ info.title }}</p>
        <p class="q-pt-md">{{ info.description }}</p>
        <!--        Socials   -->
        <div class="footer-socials">
          <p class="text-subtitle1 text-bold q-pt-lg q-pb-sm">Мы в соцсетях:</p>
          <a
            v-for="social in socials"
            :key="social.id"
            :href="social.url"
            target="_blank"
            class="q-mx-sm"
          >
            <q-icon :name="`mdi-${social.icon}`" color="white" size="30px"/>
          </a>
        </div>
        <!--        xxxxx   -->
        <q-separator inset="" dark class="q-mt-md"/>

        <!--        Links   -->
        <ul class="q-mt-lg flex justify-center q-mt-xl">
          <li>
            <router-link to="/" class="text-white">
              <span class="">Главная</span>
            </router-link>
          </li>
          <li>
            <router-link to="/about" class="text-white q-ml-md">
              <span class="">О магазине</span>
            </router-link>
          </li>
          <li>
            <router-link to="/contacts" class="text-white q-ml-md">
              <span class="">Контакты</span>
            </router-link>
          </li>
        </ul>

        <router-link to="/privacy_policy" class="text-grey-5 q-mt-md block">
          <span class="">Политика конфиденциальности</span>
        </router-link>
        <router-link to="/info/publichnaya_oferta" class="text-grey-5 q-mt-md block">
          <span class="">Публичная оферта</span>
        </router-link>
        <!--        xxxxx   -->
        <q-separator inset="" dark class="q-mt-md"/>
        <small class="text-grey-5 q-mt-sm block">{{ year }}. Все права защищены.</small>
        <small class="text-grey-5 q-mt-sm block">Разработано студией <a href="https://js-code.ru" target="_blank"
                                                                        class="text-grey-5 underline text-bold">JS Code</a></small>

      </div>
    </div>
  </footer>
</template>

<script>

export default {
  name: "posFooter",
  data() {
    return {
      benefits: [],
    }
  },
  mounted() {
    this.getBenefits()
  },
  computed: {
    socials() {
      return this.$store.getters.getSocials
    },
    info() {
      return this.$store.getters.getCompanyInfo
    },
    year() {
      let date = new Date()
      return date.getFullYear()
    }
  },
  methods: {
    getBenefits() {
      this.benefits = this.$store.getters.getBenefits
    }
  }

}
</script>

<style lang="sass">
.splide
  padding: 0

footer
  margin-top: 100px

  ul
    list-style-type: none

    span
      text-decoration: underline

@media screen and (max-width: 992px)
  footer
    padding-bottom: 50px
</style>
