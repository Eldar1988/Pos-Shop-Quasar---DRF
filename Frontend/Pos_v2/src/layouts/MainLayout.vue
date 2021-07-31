<template>
  <q-layout view="hHh lpR fFf">
    <pos-set-site-colors/>
    <q-header class="text-primary bg-white shadow-lt" height-hint="98">
      <q-toolbar>
        <!--        Shop logo   -->
        <q-toolbar-title>
          <router-link to="/" class="q-ml-sm">
            <q-img :src="info.logo" height="40px" contain style="width: 190px; max-width: 90%;" position="left">
              <template v-slot:loading>
                <q-skeleton height="40px" style="width: 190px; max-width: 90%" square/>
              </template>
            </q-img>
            <!--            <span class="text-uppercase text-primary text-weight-bold logo-title">{{ info.name }}</span>-->
          </router-link>
        </q-toolbar-title>
        <!--        xxxxx   -->
        <!--        Contact button   -->
        <pos-contacts-buttons class="hide-on-mobile" v-if="!$q.platform.is.mobile"/>
        <!--        xxxxx   -->
        <!--        Call back   -->
        <pos-call-back class="hide-on-mobile q-mr-lg"/>
        <!--        xxxxx   -->
        <!--        Header tabs   -->
        <pos-header-icons/>
        <!--        xxxxx   -->
        <q-btn size="lg" dense flat icon="las la-ellipsis-v" color="dark" @click="right = !right"/>
      </q-toolbar>
    </q-header>
    <q-drawer show-if-above v-model="right" side="right" class="text-dark">
      <pos-right-drawer-content @closeDrawer="right = false"/>
    </q-drawer>

    <!--    Pages   -->
    <q-page-container class="text-dark">
      <!--    Page reload dialog-->
      <pos-page-reload-dialog/>
      <!--    xxxxx   -->
      <router-view/>
      <!--    Footer   -->
      <pos-footer/>
      <!--    xxxxx   -->
    </q-page-container>
    <!--    xxxxx   -->
    <!--    Mobile bottom bar   -->
    <div class="hide-on-desktop">
      <pos-mobile-bottom-bar @openDraw="right = true"/>
    </div>
    <!--    xxxxx   -->
    <!--    Scripts   -->
    <div v-for="script in scripts" :key="script.id" v-html="script.script"></div>
    <!--    xxxxx   -->
  </q-layout>
</template>

<script>
import PosCallBack from "components/siteHead/posCallBack";
import PosRightDrawerContent from "components/siteHead/posRightDrawerContent";
import PosPageReloadDialog from "components/service/posPageReloadDialog";
import PosHeaderIcons from "components/siteHead/posHeaderIcons";
import PosMobileBottomBar from "components/service/posMobileBottomBar";
import PosFooter from "components/footer/posFooter";
import PosSetSiteColors from "components/service/posSetSiteColors";
import PosContactsButtons from "components/siteHead/posContactsButtons";

export default {
  components: {
    PosContactsButtons,
    PosSetSiteColors,
    PosFooter, PosMobileBottomBar, PosHeaderIcons, PosPageReloadDialog, PosRightDrawerContent, PosCallBack
  },
  data() {
    return {
      right: false,
    }
  },
  // created() {
  //   this.$store.dispatch('fetchMainData')
  // },
  async mounted() {
    setTimeout(() => {
      this.$store.dispatch('fetchCategories')
      this.$store.dispatch('fetchLatestProducts')
      this.$store.dispatch('fetchServiceCategories')
    }, 500)
  },
  computed: {
    backendError() {
      return this.$store.getters.getMainDataStatus
    },
    info() {
      return this.$store.getters.getCompanyInfo
    },
    scripts() {
      return this.$store.getters.getSiteSettings.scripts
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchMainData')
  }
}
</script>

<style lang="sass">
.small-tabs
  padding: 0 3px
</style>
