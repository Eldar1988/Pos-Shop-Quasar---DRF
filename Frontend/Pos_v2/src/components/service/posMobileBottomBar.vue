<template>
  <div class="mobile-bottom-bar bg-white shadow-10"
       :style="this.$q.platform.is.ios ? `bottom: 20px` : `bottom: 5px`"
  >
    <div class="flex flex-center">
      <a :href="`tel:${contacts.phone}`">
        <q-btn
          icon="las la-phone-volume"
          flat round
          color="dark"
          size="20px"
          style="margin-top: -7px"
        />
      </a>
    </div>
    <div class="flex flex-center text-center">

      <a :href="`https://wa.me/${contacts.whatsapp}`">
        <q-btn
          icon="lab la-whatsapp"
          flat round
          color="dark"
          size="20px"
          style="margin-top: -8px"
        />
      </a>
    </div>
    <div class="flex flex-center">
      <q-btn
        icon="las la-ellipsis-h"
        color="dark"
        flat
        size="24px"
        style="margin-top: -8px"
        @click="$emit('openDraw')"
      />
    </div>
    <div class="flex flex-center">
      <q-fab
        v-model="fab"
        vertical-actions-align="right"
        color="dark" active-icon="lar la-times-circle"
        flat
        icon="lar la-question-circle"
        direction="up" padding="10px"
        style="z-index: 100"
      >
        <q-fab-action label-position="right" color="primary" icon="question_answer" label="Вопросы и ответы" to="/questions"/>
        <q-fab-action label-position="right" color="accent" icon="phone_callback" label="Консультация" @click="callBack"/>
      </q-fab>
    </div>
    <div class="flex flex-center">
      <q-btn
        icon="las la-search"
        round flat
        color="dark"
        to="/search"
        size="20px"
        style="margin-top: -8px"
      />
    </div>

  </div>
</template>

<script>
export default {
  name: "posMobileBottomBar",
  data() {
    return {
      fab: false
    }
  },
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  },
  methods: {
    callBack() {
      this.$root.$emit('callBack')
    }
  }
}
</script>

<style lang="sass">
.mobile-bottom-bar
  position: fixed
  bottom: 5px
  left: 8px
  right: 8px
  height: 52px
  color: white
  display: grid
  grid-template-columns: repeat(5, 1fr)
  align-items: start
  z-index: 1000
  padding: 3px 0 0
  overflow: visible

.q-btn--fab .q-icon, .q-btn--fab-mini .q-icon
  font-size: 34px !important

.q-fab__icon-holder
  min-width: 32px !important
  min-height: 26px !important

</style>
