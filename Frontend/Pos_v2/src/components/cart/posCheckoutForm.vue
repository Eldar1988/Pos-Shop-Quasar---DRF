<template>
  <div class="">
    <q-stepper
      ref="stepper"
      v-model="step"
      animated
      class="shadow-0 br-0" color="primary"
      vertical
    >
      <p class="text-subtitle1 text-bold q-pl-lg q-pt-sm">Оформление заказа</p>
      <p class="q-pl-lg">Для оформления заказа заполните форму ниже</p>
      <!--      Personal data   -->
      <q-step
        :done="formData.name !== '' && formData.phone !== '' ? step > 1 : false"
        :error="formData.name === '' || formData.phone === ''"
        :name="1"
        icon="user"
        title="Персональные данные"
        done-color="positive"
        error-color="negative"
        class="q-mt-md"
      >
        <div class="row">
          <div class="col-12" style="padding: 2px">
            <q-input
              v-model="formData.name"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="ФИО"
              outlined square
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
              outlined square
              type="tel"
            />
          </div>
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.email"
              label="Email (необязательно)"
              outlined square
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
              outlined square
              type="text"
              maxlength="200" counter
            />
          </div>
          <div class="col-12 col-sm-6" style="padding: 2px">
            <q-input
              v-model="formData.city"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Город*"
              outlined square
              type="text"
              maxlength="200" counter
            />
          </div>
          <div class="col-12" style="padding: 2px">
            <q-input
              v-model="formData.address"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="Адрес*"
              outlined square
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
        <div v-if="allFieldsCompleted">
        <p class="q-ml-lg text-bold q-pb-md ">Выберите способ оплаты</p>
        <q-card
          v-if="googlePayMerchantId"
          square
          class="grey-border shadow-0 q-pa-sm cursor-pointer shadow-on-hover q-mt-sm"
          @click="googlePayDialog = true"
        >
          <div class=" text-center">
            <div class="">
              <div style="height: 50px">
                <img src="../../assets/Gpay.png" style="height: 50px"
                     class="cursor-pointer q-ml-md"
                />
              </div>
            </div>
          </div>
        </q-card>
        <q-card
          square
          class="grey-border shadow-0 q-pa-sm cursor-pointer shadow-on-hover q-mt-sm"
          v-for="payment in paymentMethods"
          :key="payment.id"
          @click="createNewOrder(payment.title, payment.slug)"
        >
          <div class="flex justify-center">
            <q-img :src="payment.image" height="50px" contain/>
            <p class="q-pt-sm text-bold">{{ payment.title }}</p>
          </div>
        </q-card>
        </div>
        <div v-else>
          <q-card
            square
            class="shadow-0 q-px-sm q-py-lg bg-negative text-white text-center"
          >
            <p>Для того, чтобы выбрать способ оплаты необходимо заполнить все обязательные поля.</p>
            <q-btn
              label="ok"
              outline
              class="q-mt-md q-px-sm"
              @click="step = 1"
            />
          </q-card>
        </div>
      </q-step>
      <!--      xxxxx   -->
      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn
            v-if="step > 1"
            color="primary"
            flat
            icon="west"
            @click="$refs.stepper.previous()"
            class="q-py-sm"
          />
          <q-btn
            :label="step === 4 ? 'Готово' : 'Далее'"
            color="primary"
            @click="$refs.stepper.next()"
            class="q-px-xl q-ml-sm text-bold q-py-sm"
            no-caps unelevated
          />
        </q-stepper-navigation>
      </template>
    </q-stepper>

<!--    Google pay dialog   -->
    <q-dialog
      v-model="googlePayDialog"
    >
      <q-card
        style="width: 500px; max-width: 100%"
        class="bg-grey-2"
      >
        <q-toolbar class="bg-dark text-white">
        <q-toolbar-title>Ваш заказ</q-toolbar-title>
          <q-btn icon="close" flat dense v-close-popup/>
        </q-toolbar>
        <q-card-section>
          <div class="cart-items q-mt-md">
            <pos-cart-item
              v-for="product in products"
              :key="product.timeID"
              :product="product"
            />
          </div>
          <p class="text-bold q-pt-md">Всего товаров: {{ cartLen }}</p>
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
          <div class="q-pt-lg text-center">
            <pos-google-pay :amount="cartSum" @createOrder="createNewOrder" :merchant-id="googlePayMerchantId"/>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
<!--    xxxxx -->

  </div>
</template>

<script>
import formatPrice from "src/filters/format_price";
import {QSpinnerFacebook} from "quasar";
import PosGooglePay from "components/cart/posGooglePay";
import PosCartItem from "components/cart/posCartItem";

export default {
  name: "posCheckoutForm",
  components: {PosCartItem, PosGooglePay},
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
  computed: {

    allFieldsCompleted() {
      let allFieldsCompleted = true
      let data = this.formData
      for (let key in data) {
        if(key !== 'email' && data[key] === '') allFieldsCompleted = false
      }
      return allFieldsCompleted
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
      },
      googlePayMerchantId: null,
      googlePayMerchantName: null,
      googleIsTest: null,
      googlePayDialog: false
    }
  },
  created() {
    this.loadPaymentMethods()
  },
  methods: {
    async loadPaymentMethods() {
      this.paymentMethods = await this.$axios.get(`${this.$store.getters.getServerURL}/orders/payments/`)
        .then(({data}) => {
          return data
        })

      this.googlePayMerchantId = await this.$axios.get(`${this.$store.getters.getServerURL}/orders/google_pay_merchant/`)
        .then(({data}) => {
          this.googlePayMerchantName = data.merchantName
          this.googleIsTest = data.test
          return data.merchantId
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
    async createNewOrder(paymentMethod, slug, paid=false, notice='') {

      if (
        !this.checkData(this.formData.name, 'Необходимо указать имя*', 1) ||
        !this.checkData(this.formData.phone, 'Необходимо указать номер телефона*', 1) ||
        !this.checkData(this.formData.region, 'Необходимо указать область доставки*', 2) ||
        !this.checkData(this.formData.city, 'Необходимо указать город доставки*', 2) ||
        !this.checkData(this.formData.address, 'Необходимо указать адрес доставки*', 2)
      ) {
        return null
      }

      this.$q.loading.show({
        spinner: QSpinnerFacebook,
        spinnerColor: 'white',
        spinnerSize: 80,
        backgroundColor: 'primary',
        message: 'Секунду...',
        messageColor: 'white'
      })
      // Преобразование вариаций в строку
      let productsForOrder = this.products.map(item => {
        let variations = ''
        if (item.variations) {
          item.variations.forEach(variation => {
            variations += `${variation.type}: ${variation.value}. `
          })
        }
        item.variations = variations
        return item
      })

      let data = this.formData
      data.products = productsForOrder
      data.order_sum = this.cartSum
      data.paid = paid
      data.notice = notice
      data.payment_method = paymentMethod

      await fetch(`${this.$store.getters.getServerURL}/orders/create_order/`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      }).then(response => {

        if (response.status === 201) {
          let cart = []
          localStorage.setItem('cart', JSON.stringify(cart))
          this.$root.$emit('updateCart')
          document.querySelector('#q-app').scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          })
          this.$q.loading.hide()
          this.$router.push(`/thanks/${slug}`)

        } else {
          this.$q.loading.hide()
          this.$q.notify({
            message: 'Вы корректно заполнили форму заказа? Пожалуйста, проверьте и попробуйте заново',
            position: 'top'
          })
        }
      })
    },

  }
}
</script>

<style lang="sass">

</style>
