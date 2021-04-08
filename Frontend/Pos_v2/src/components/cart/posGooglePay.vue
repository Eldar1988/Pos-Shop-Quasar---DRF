<template>
<div>
  <google-pay-button
    :environment="this.isTest ? 'TEST' : 'PRODUCTION'"
    v-bind:button-type="buttonType"
    v-bind:button-color="buttonColor"
    v-bind:existing-payment-method-required="existingPaymentMethodRequired"
    v-bind:paymentRequest.prop="{
          apiVersion: paymentRequest.apiVersion,
          apiVersionMinor: paymentRequest.apiVersionMinor,
          allowedPaymentMethods: paymentRequest.allowedPaymentMethods,
          merchantInfo: paymentRequest.merchantInfo,
          transactionInfo: {
            totalPriceStatus: 'FINAL',
            totalPriceLabel: 'Total',
            totalPrice: `${amount.toString()}.00`,
            currencyCode: 'KZT',
            countryCode: 'KZ',
          },
          callbackIntents: ['PAYMENT_AUTHORIZATION'],
        }"
    v-on:loadpaymentdata="onLoadPaymentData"
    v-on:error="onError"
    v-bind:onPaymentAuthorized.prop="onPaymentDataAuthorized"
  ></google-pay-button>
</div>
</template>

<script>
import "@google-pay/button-element"
export default {
  name: "posGooglePay",
  props: {
    amount: {
      type: Number,
      default: 0
    },
    merchantId: {
      type: String,
      default: ''
    },
    merchantName: {
      type: String,
      default: ''
    },
    isTest: {
      type: Boolean,
      default: true
    }
  },
  data: () => ({
    existingPaymentMethodRequired: true,
    buttonColor: "default",
    buttonType: "buy",
    paymentRequest: {
      apiVersion: 2,
      apiVersionMinor: 0,
      allowedPaymentMethods: [
        {
          type: "CARD",
          parameters: {
            allowedAuthMethods: ["PAN_ONLY", "CRYPTOGRAM_3DS"],
            allowedCardNetworks: ["MASTERCARD", "VISA"],
          },
          tokenizationSpecification: {
            type: "PAYMENT_GATEWAY",
            parameters: {
              gateway: "example",
              gatewayMerchantId: "exampleGatewayMerchantId",
            },
          },
        },
      ],
      merchantInfo: {
        merchantId: '',
        merchantName: '',
      },
    },
  }),
  mounted() {
    this.paymentRequest.merchantInfo.merchantId = this.merchantId
    this.paymentRequest.merchantInfo.merchantName = this.merchantName
  },
  methods: {
    onLoadPaymentData: (event) => {

    },
    onError: (event) => {
      this.$emit('createOrder', 'Google Pay', 'google_pay', false, 'Не удалось оплатить с Google pay')
    },
    onPaymentDataAuthorized (paymentData) {
      this.$emit('createOrder', 'Google Pay', 'google_pay', true)
      return {
        transactionState: "SUCCESS",
      };
    },
  },
}
</script>

<style scoped>

</style>
