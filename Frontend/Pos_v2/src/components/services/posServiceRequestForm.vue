<template>
  <div>
    <q-card
      v-if="form"
      square
      class="shadow-0 q-py-xl text-center"
    >
      <div >
        <p class="text-bold text-uppercase">{{ callToActionText }}</p>
        <div style="width: 500px; margin: auto; max-width: 90%" class="q-pt-lg">
          <q-input v-model="formData.name" square label="Ваше имя*" outlined type="text"/>
          <q-input v-model="formData.phone" square label="Номер телефона*" outlined type="tel" class="q-mt-md" mask="# ### ### ####"/>
          <q-input v-model="formData.comment" square label="Комментарий (необязательно)" outlined type="textarea"
                   class="q-mt-md"/>
          <q-btn
            :label="btnText"
            class="full-width q-py-sm q-mt-md text-bold"
            color="accent"
            unelevated
            @click="sendServiceRequest"
          />
        </div>
      </div>
    </q-card>
    <q-slide-transition>
    <q-card
      v-if="!form"
      square
      class="shadow-0 q-py-lg bg-positive text-white text-center q-px-sm text-bold"
    >
        <p>Спасибо! <br> Ваша заявка принята. <br> Мы свяжемся с Вами в ближайшее время.</p>
    </q-card>
    </q-slide-transition>
  </div>
</template>

<script>
import notifier from "src/functions/notifier";

export default {
  name: "posServiceRequestForm",
  props: {
    serviceID: {
      type: Number,
      default: null
    },
    btnText: {
      type: String,
      default: 'Консультация'
    },
    callToActionText: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      formData: {
        name: '',
        phone: '',
        comment: ''
      },
      form: true
    }
  },
  methods: {
    validate(name, phone) {
      if (name === '') {
        notifier('Необходимо указать имя.')
        return false
      }
      if (phone === '') {
        notifier('Необходимо указать номер телефона.')
        return false
      }
      return true
    },
    sendServiceRequest() {
      let valid = this.validate(this.formData.name, this.formData.phone)
      if (valid) {
        let data = this.formData
        data.service = this.serviceID
        let sendData = JSON.stringify(data)
        this.$axios.post(`${this.$store.getters.getServerURL}/services/create_service_request/`, {
          name: this.formData.name,
          phone: this.formData.phone,
          comment: this.formData.comment,
          service: this.serviceID
        })
          .then(response => {
            if (response.status === 201) {
              notifier('Ваша заявка принята', 'positive')
              this.form = false
            } else {
              notifier('Ошибка сервера. Пожалуйста, попробуйте еще раз или свяжитесь с нами по телефону.')
            }
          })
      }
    }
  }
}
</script>

<style scoped>

</style>
