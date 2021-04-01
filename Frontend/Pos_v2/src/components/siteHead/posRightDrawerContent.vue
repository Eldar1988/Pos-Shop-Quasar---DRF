<template>
  <div class="">
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
    <!--    Contacts   -->
    <pos-contacts-buttons class="bg-grey-2 hide-on-desktop"/>
    <!--    xxxxx   -->
    <!--    Mobile callback button   -->
    <div class="q-pa-sm bg-grey-2 hide-on-desktop">
      <pos-call-back color="accent"/>
    </div>
    <!--    xxxxx    -->
    <!--    Navigation   -->
    <pos-drawer-navigation class="bg-grey-2"/>
    <!--    xxxxx   -->
  </div>
</template>

<script>
import PosCallBack from "components/siteHead/posCallBack";
import PosDrawerNavigation from "components/siteHead/posDrawerNavigation";
import PosContactsButtons from "components/siteHead/posContactsButtons";

export default {
  name: "posRightDrawerContent",
  components: {PosContactsButtons, PosDrawerNavigation, PosCallBack},

}
</script>

<style lang="sass">
.shadow-menu
  box-shadow: rgba(99, 99, 99, 0.15) 0px 0px 5px 0px
@media screen and (max-width: 992px)
  .mobile-menu-toolbar
    display: flex !important
    align-items: center
</style>
