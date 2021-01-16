<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <span class="text-uppercase text-weight-bold logo-title">Pos-shop</span>
        </q-toolbar-title>
        <pos-call-back class="hide-on-mobile q-mr-lg"/>
        <q-tabs align="center" stretch>
          <q-route-tab to="/" icon="roofing" class="small-tabs"/>
          <q-route-tab to="/" icon="store" class="small-tabs"/>
          <q-route-tab to="/" icon="shopping_bag" class="small-tabs"/>
        </q-tabs>
        <q-btn size="lg" dense flat round icon="view_list" @click="right = !right"/>
      </q-toolbar>
    </q-header>
    <q-drawer show-if-above v-model="right" side="right" bordered>
      <pos-right-drawer-content @closeDrawer="right = false"/>
    </q-drawer>

    <q-page-container>
      <!--    Page reload dialog-->
      <pos-page-reload-dialog />
      <!--    xxxxx   -->
      <router-view/>
    </q-page-container>


  </q-layout>
</template>

<script>
import PosCallBack from "components/siteHead/posCallBack";
import PosRightDrawerContent from "components/siteHead/posRightDrawerContent";
import PosPageReloadDialog from "components/service/posPageReloadDialog";
// import PosPageReloadDialog from "components/service/posPageReloadDialog";

export default {
  components: {PosPageReloadDialog, PosRightDrawerContent, PosCallBack},
  data() {
    return {
      right: false,
    }
  },
  computed: {
    backendError() {
      return this.$store.getters.getMainDataStatus
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
