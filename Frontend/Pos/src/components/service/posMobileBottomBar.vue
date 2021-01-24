<template>
  <div class="mobile-bottom-bar bg-primary"
       :style="this.$q.platform.is.ios ? `height: 70px` : `height: 52px`"
  >
    <div class="flex flex-center">
      <a :href="`tel:${contacts.phone}`">
        <q-btn
          icon="call"
          flat round
          color="white"
        />
      </a>
    </div>
    <div class="flex flex-center text-center">

      <a :href="`https://wa.me/${contacts.whatsapp}`">
        <q-btn
          icon="mdi-whatsapp"
          flat round
          color="white"
        />
      </a>
    </div>
    <div class="flex flex-center">
      <q-btn
        icon="menu"
        outline round
        color="white"
        style="margin-top: 2px"
        @click="$emit('openDraw')"
      />
    </div>
    <div class="flex flex-center">
      <q-fab
        v-model="fab"
        vertical-actions-align="right"
        color="white"
        flat
        icon="help_outline"
        direction="up" padding="10px"
      >
        <q-fab-action label-position="right" color="primary" icon="question_answer" label="Вопросы и ответы" to="/questions"/>
        <q-fab-action label-position="right" color="accent" icon="phone_callback" label="Консультация" @click="callBack"/>
      </q-fab>
    </div>
    <div class="flex flex-center">
      <q-btn
        icon="search"
        round flat
        color="white"
        to="/search"
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
  bottom: 0
  left: 0
  right: 0
  width: 100%
  color: white
  display: grid
  grid-template-columns: repeat(5, 1fr)
  align-items: start
  z-index: 1000
  padding: 3px 0 0
</style>
