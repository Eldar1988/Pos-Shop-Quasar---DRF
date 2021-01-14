<template>
  <div>
    <!--    Mobile menu toolbar   -->
    <q-toolbar class="hide-on-desktop bg-primary mobile-menu-toolbar">
      <q-toolbar-title class="text-uppercase text-white text-h6 text-weight-bold">Меню</q-toolbar-title>
      <q-btn
        icon="close"
        color="white"
        flat dense
        @click="$emit('closeDrawer')"
      />
    </q-toolbar>
    <!--    xxxxx   -->
    <!--    Mobile callback button   -->
    <div class="q-pa-sm hide-on-desktop">
      <pos-call-back color="primary"/>
    </div>
    <!--    xxxxx    -->
    <!--    Navigation   -->
    <pos-drawer-navigation />
    <!--    xxxxx   -->
  </div>
</template>

<script>
import PosCallBack from "components/siteHead/posCallBack";
import PosDrawerNavigation from "components/siteHead/posDrawerNavigation";

export default {
  name: "posRightDrawerContent",
  components: {PosDrawerNavigation, PosCallBack}
}
</script>

<style lang="sass">
@media screen and (max-width: 992px)
  .mobile-menu-toolbar
    display: flex !important
    align-items: center
</style>
