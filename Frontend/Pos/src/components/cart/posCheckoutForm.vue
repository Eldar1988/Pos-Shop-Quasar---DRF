<template>
  <div class="q-pa-sm">

    <q-stepper
      ref="stepper"
      v-model="step"
      animated
      class="shadow-0 grey-border border-radius-6" color="primary"
      vertical
    >
      <p class="text-subtitle1 text-bold q-pl-lg">Оформление заказа</p>
      <p class="q-pl-lg">Для оформления заказа заполните форму ниже</p>

      <!--      Personal data   -->
      <q-step
        :done="step > 1"
        :error="formData.name === '' || formData.phone === ''"
        :name="1"
        icon="user"
        title="Персональные данные"
        done-color="positive"
        error-color="negative"
      >
        <div class="row">
          <div class="col-12" style="padding: 2px">
            <q-input
              v-model="formData.name"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="ФИО"
              outlined
              type="text"
              maxlength="100" counter
            />
          </div>
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.phone"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Номер телефона*"
              mask="#-###-###-####"
              outlined
              type="tel"
            />
          </div>
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.email"
              label="Email (необязательно)"
              outlined
              type="email"
              onautocomplete
            />
          </div>
        </div>
      </q-step>
      <!--      xxxxx   -->
      <!--      Address   -->
      <q-step
        :error="formData.region === '' || formData.city === '' || formData.address === ''"
        :done="step > 2"
        :name="2"
        icon="edit_location_alt"
        title="Адрес доставки"
        done-color="positive"
        error-color="negative"
      >
        <div class="row">
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.region"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Область*"
              outlined
              type="text"
              maxlength="200" counter
            />
          </div>
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.city"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Город*"
              outlined
              type="text"
              maxlength="200" counter
            />
          </div>
          <div class="col-12" style="padding: 2px">
            <q-input
              v-model="formData.address"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Адрес*"
              outlined
              type="text"
              onautocomplete
              maxlength="200" counter
            />
          </div>
        </div>
      </q-step>
      <!--      xxxxx   -->
      <!--      Order detail   -->
      <q-step
        :name="3"
        icon="assignment"
        title="Детали заказа"
        done-color="positive"
        :done="step > 3"
        error-color="negative"
      >
        <p class="text-bold">Всего товаров: {{ cartLen }}</p>
        <p class="text-bold">Общая сумма заказа: {{ cartSum|formatPrice }}
          <q-icon name="mdi-currency-kzt" class="icon-wrapper"/>
        </p>
        <q-separator class="q-mt-sm"/>
        <p class="text-bold q-pt-sm">Получатель: <span
          class="text-weight-regular">{{ formData.name ? formData.name : 'не указан' }}</span></p>
        <p class="text-bold">Телефон: <span
          class="text-weight-regular">{{ formData.phone ? formData.phone : 'не указан' }}</span></p>
        <p class="text-bold">Адрес доставки: <span class="text-weight-regular">{{
            formData.region ? formData.region : 'регион не указан'
          }}, {{
            formData.city ? formData.city : 'город не указан'
          }}, {{ formData.address ? formData.address : 'адрес не указан' }}</span></p>
      </q-step>
      <!--      xxxxx   -->

      <!--      Payment   -->
      <q-step
        :name="4"
        icon="payments"
        title="Оплата"
      >
        <p class="q-ml-lg text-bold q-pb-md ">Выберите способ оплаты</p>
        <q-card
          class="grey-border shadow-0 border-radius-6 q-pa-sm cursor-pointer shadow-on-hover"
          v-for="payment in paymentMethods"
          :key="payment.id"
          @click="createNewOrder(payment.title, payment.slug)"
        >
          <div class="flex justify-center">
            <q-img :src="payment.image" height="50px" contain/>
            <p class="q-pt-sm text-bold">{{ payment.title }}</p>
          </div>
        </q-card>
      </q-step>

      <!--      xxxxx   -->
      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn v-if="step > 1" class="border-radius-6" color="primary" flat icon="west"
                 @click="$refs.stepper.previous()"/>
          <q-btn :label="step === 4 ? 'Готово' : 'Далее'" color="primary" @click="$refs.stepper.next()"
                 class="q-px-md text-bold border-radius-6 q-ml-sm"/>

        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>
</template>

<script>
import formatPrice from "src/filters/format_price";
import {QSpinnerFacebook} from "quasar";

export default {
  name: "posCheckoutForm",
  filters: {formatPrice},
  props: {
    cartLen: {
      type: Number,
      default: 0
    },
    cartSum: {
      type: Number,
      default: 0
    },
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      paymentMethods: [],
      step: 1,
      personDataError: false,
      formData: {
        name: '',
        phone: '',
        email: '',
        city: '',
        region: '',
        address: '',
      }
    }
  },
  mounted() {
    this.loadPaymentMethods()
  },
  methods: {
    async loadPaymentMethods() {
      this.paymentMethods = await this.$axios.get(`${this.$store.getters.getServerURL}/orders/payments/`)
        .then(({data}) => {
          return data
        })
    },
    checkData(dataName, message, step) {
      if (dataName === '') {
        this.$q.notify({message: `${message}`, position: 'top', color: 'negative'})
        this.step = step
        this.$q.loading.hide()
        return false
      }
      return true
    },
    // New order
    async createNewOrder(paymentMethod, slug) {

      this.$q.loading.show({
        spinner: QSpinnerFacebook,
        spinnerColor: 'white',
        spinnerSize: 80,
        backgroundColor: 'primary',
        message: 'Секунду...',
        messageColor: 'white'
      })
      if (
        !this.checkData(this.formData.name, 'Необходимо указать имя*', 1) ||
        !this.checkData(this.formData.phone, 'Необходимо указать номер телефона*', 1) ||
        !this.checkData(this.formData.region, 'Необходимо указать область доставки*', 2) ||
        !this.checkData(this.formData.city, 'Необходимо указать город доставки*', 2) ||
        !this.checkData(this.formData.address, 'Необходимо указать адрес доставки*', 2)
      ) {
        return null
      }
      let data = this.formData
      data.products = this.products
      data.order_sum = this.cartSum
      data.payment_method = paymentMethod

      await fetch(`${this.$store.getters.getServerURL}/orders/create_order/`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      }).then(response => {
        if (response.status === 200) {

          let cart = []
          localStorage.setItem('cart', JSON.stringify(cart))
          this.$root.$emit('updateCart')
          setTimeout(() => {
            this.$q.loading.hide()

            this.$router.push(`/thanks/${slug}`)
          }, 1500)
        } else {
          this.$q.loading.hide()
          this.$q.notify({
            message: 'Вы корректно заполнили форму заказа? Пожалуйстаб проверьте и попробуйте заново',
            position: 'top'
          })
        }
      })
    }
  }
}
</script>

<style lang="sass">

</style>
