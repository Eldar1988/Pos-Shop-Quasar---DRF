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
    <!--    Contacts   -->
    <div class="manu-contacts q-py-md q-px-sm full-width">
      <a :href="`tel:${contacts.phone}`" title="Телефон для консультаций и заказов">
        <q-btn
          :label="contacts.phone"
          class="full-width border-radius-6 text-bold shadow-menu"
          color="dark"
          flat
          icon="call"

        />
      </a>
      <a :href="`https://wa.me/${contacts.whatsapp}`" title="Номер Whatsapp" class="q-mt-sm block">
        <q-btn
          :label="contacts.whatsapp"
          class="full-width border-radius-6 text-bold shadow-menu"
          color="green"
          flat
          icon="mdi-whatsapp"
        />
      </a>
    </div>
    <!--    xxxxx   -->
    <!--    Mobile callback button   -->
    <div class="q-pa-sm hide-on-desktop">
      <pos-call-back color="accent"/>
    </div>
    <!--    xxxxx    -->
    <!--    Navigation   -->
    <pos-drawer-navigation/>
    <!--    xxxxx   -->
  </div>
</template>

<script>
import PosCallBack from "components/siteHead/posCallBack";
import PosDrawerNavigation from "components/siteHead/posDrawerNavigation";

export default {
  name: "posRightDrawerContent",
  components: {PosDrawerNavigation, PosCallBack},
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  }
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
