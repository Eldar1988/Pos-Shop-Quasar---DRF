<template>
  <div>
    <q-btn
      label="Обратный звонок"
      icon-right="phone_callback"
      :color="color"
      class="full-width text-bold"
      @click="dialog = true"
      unelevated
    />

    <q-dialog
      v-model="dialog"
    >
      <q-card class="text-dark" style="width: 500px; max-width: 90vw;">
        <q-toolbar class="bg-grey-3 ">
          <q-toolbar-title class="flex justify-between" style="align-items: center">
            <div class="text-h6 text-bold">Обратный звонок</div>
            <q-icon name="close" class="cursor-pointer" v-close-popup/>
          </q-toolbar-title>

        </q-toolbar>

        <q-card-section class="">
          Пожалуйста, заполните форму<br>Мы свяжемся с вами в ближайшее время
        </q-card-section>
        <q-card-section class="">
          <div class="q-pa-sm">
            <q-input v-model="formData.name" label="Ваше имя*" type="text"/>
            <small v-if="formData.name === ''" class="text-negative">{{ errorTextName }}</small>
            <q-input v-model="formData.phone" label="Номер телефона*" type="tel" mask="#-###-###-####"
                     class="q-mt-md"/>
            <small v-if="formData.phone === ''" class="text-negative">{{ errorTextPhone }}</small>
          </div>
        </q-card-section>

        <q-card-actions align="center" class="bg-white text-teal q-pa-md">
          <q-btn
            color="accent"
            label="Отправить"
            class="q-py-sm full-width text-bold"
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
      default: 'accent'
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
  mounted() {
    this.$root.$on('callBack', () => {
      this.dialog = !this.dialog
    })
  },
  methods: {
    async callBack() {
      this.loading = true
      if (this.formData.name === '') {
        this.errorTextName = 'Как к вам обращаться?'
        this.loading = false
        return null
      }
      if (this.formData.phone === '') {
        this.errorTextPhone = 'Укажите ваш номер телефона'
        this.loading = false
        return null
      }
      await fetch(`${this.$store.getters.getServerURL}/orders/call_back/`, {
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
