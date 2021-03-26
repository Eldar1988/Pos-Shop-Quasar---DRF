<template>
  <div>
    <div class="menu-contacts">
      <q-btn
        :label="contacts.phone"
        class="full-width bg-white"
        color="dark"
        outline
        icon="call"
        type="a"
        :href="`tel:${contacts.phone}`"
        title="Телефон для консультаций и заказов"
      />
      <q-btn
        :label="contacts.whatsapp"
        class="full-width bg-white"
        color="dark"
        outline
        icon="mdi-whatsapp"
        type="a"
        :href="`https://wa.me/${contacts.whatsapp}`"
        title="Номер Whatsapp"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "posContactsButtons",
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  }
}
</script>

<style lang="sass">
.menu-contacts
  display: grid
  grid-template-columns: 1fr 1fr
  padding: 0 10px
  grid-gap: 10px

@media screen and (max-width: 1100px)
  .menu-contacts
    grid-template-columns: 1fr
    padding: 10px 8px
    grid-gap: 10px
</style>
