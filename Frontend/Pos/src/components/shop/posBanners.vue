<template>
<section class="section q-pa-sm">
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
        <q-btn
          v-if="banner.btn_text"
          :label="banner.btn_text"
          color="negative"
          style="position: absolute; bottom: 10px; right: 10px; z-index: 30"
          size="sm" unelevated
          class="text-bold"
        />
        <template v-slot:loading>
          <q-skeleton class="banner-image full-width" />
        </template>
      </q-img>
      </router-link>
    </article>
  </div>
  <div v-else class="banners-wrapper">
    <q-skeleton
      v-for="(i, index) in 3"
      :key="index"
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
      reloadBannersStatus: true
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

@media screen and (max-width: 1402px)
  .banner-image
    height: 200px

@media screen and (max-width: 1300px)
  .banner-image
    height: 170px

@media screen and (max-width: 1100px)
  .banner-image
    height: 120px

@media screen and (max-width: 1023px)
  .banner-image
    height: 170px

@media screen and (max-width: 800px)
  .banner-image
    height: 130px

@media screen and (max-width: 650px)
  .banners-wrapper
    grid-template-columns: 1fr

  .banner-image
    height: 200px
</style>
