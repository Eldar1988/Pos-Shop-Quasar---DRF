<template>
<section class="q-pa-sm">
  <div v-if="!reloadBannersStatus" class="banners-wrapper">
    <article
      v-for="banner in banners"
      :key="banner.id"
      class="shadow-on-hover border-radius-6"
    >
      <router-link
        :to="banner.url ? banner.url : ''"
      >
      <q-img
        :src="banner.image"
        :contain="banner.contain"
        class="banner-image"
      >
        <template v-slot:loading>
          <q-skeleton class="banner-image full-width" />
        </template>
      </q-img>
      </router-link>
    </article>
  </div>
  <div v-else class="banners-wrapper">
    <q-skeleton
      v-for="i in 3"
      :key="i"
      class="full-width banner-image"
    />
  </div>
</section>
</template>

<script>
export default {
  name: "posBanners",
  data() {
    return {
      banners: [],
      reloadBannersStatus: false
    }
  },
  mounted() {
    this.loadBanners()
  },
  methods: {
    async loadBanners() {
      try {
        this.banners = await this.$axios.get(`${this.$store.getters.getServerURL}/banners/`)
          .then(({data}) => {
            this.reloadBannersStatus = false
            return data
          })
      }
      catch (e) {
        this.reloadBannersStatus = true
        this.reloadBanners()
      }
    },
    reloadBanners() {
      let reload = setInterval(() => {
        this.reloadBannersStatus ? this.loadBanners() : clearInterval(reload)
      }, 5000)
    }
  }
}
</script>

<style lang="sass">
.banners-wrapper
  display: grid
  grid-template-columns: repeat(3, 1fr)
  grid-gap: 10px

.banner-image
  height: 250px

@media screen and (max-width: 650px)
  .banners-wrapper
    grid-template-columns: 1fr

  .banner-image
    height: 200px
</style>
