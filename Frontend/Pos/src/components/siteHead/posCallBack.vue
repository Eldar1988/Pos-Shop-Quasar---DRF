<template>
  <div>
    <q-btn
      label="Обратный звонок"
      icon-right="phone_callback"
      outline
      :color="color"
      class="text-weight-bold full-width border-radius-6"
      unelevated
      @click="dialog = true"
    />

    <q-dialog
      v-model="dialog"
    >
      <q-card style="width: 500px; max-width: 90vw;">
        <q-toolbar class="bg-primary text-white">
          <q-toolbar-title class="flex justify-between" style="align-items: center">
            <div class="text-h6 text-bold">Обратный звонок</div>
            <q-icon name="close" class="cursor-pointer" v-close-popup/>
          </q-toolbar-title>

        </q-toolbar>

        <q-card-section class="">
          Пожалуйста, заполните форму<br>Мы свяжемся с вами в ближайшее время
        </q-card-section>
        <q-card-section class="">
          <q-input v-model="formData.name" label="Ваше имя*" outlined type="text"/>
            <small class="text-negative">{{ errorTextName }}</small>
          <q-input v-model="formData.phone" label="Номер телефона*" outlined type="tel" mask="#-###-###-####"
                   class="q-mt-md"/>
          <small class="text-negative">{{ errorTextPhone }}</small>
        </q-card-section>

        <q-card-actions align="center" class="bg-white text-teal q-pa-md">
          <q-btn
            color="accent"
            label="Отправить"
            class="q-py-sm full-width text-bold red-shadow border-radius-6"
            icon-right="forward_to_inbox"
            unelevated
            :loading="loading"
            @click="callBack"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>


<script>
export default {
  name: "posCallBack",
  props: {
    color: {
      type: String,
      default: 'white'
    }
  },
  data() {
    return {
      dialog: false,
      errorTextName: '',
      errorTextPhone: '',
      formData: {
        name: '',
        phone: ''
      },
      loading: false
    }
  },
  methods: {

    async callBack() {
      this.loading = true
      if (this.formData.name === '') {
        this.errorTextName = 'Как к вам обращаться?'
        return null
      }
      if (this.formData.phone === '') {
        this.errorTextPhone = 'Укажите ваш номер телефона'
        return null
      }
      await fetch(`${this.$store.getters.getServerURL}/orders/call_back/`,{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(this.formData)
      }).then(response => {
        if (response.status === 201) {
          setTimeout(() => {
            this.loading = false
            this.dialog = false
            this.$router.push('/thanks/callback/')
          }, 1000)
        } else {
          this.loading = false
          this.$q.notify({message: 'Извините, произошла ошибка. Попробуйте еще раз', position: 'top'})
        }

      })
    }
  }
}
</script>

<style scoped>

</style>
