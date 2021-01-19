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
      <q-step
        :done="step > 1"
        :error="formData.name === '' || formData.phone === ''"
        :name="1"
        icon="user"
        title="Персональные данные"
      >
        <div class="row">
          <div class="col-12" style="padding: 2px">
            <q-input
              v-model="formData.name"
              :rules="[val => !!val || 'Это обязательное поле*']"
              label="ФИО"
              outlined
              type="text"
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
            />
          </div>
        </div>
      </q-step>

      <q-step
        :done="step > 2"
        :name="2"
        caption="Optional"
        icon="create_new_folder"
        title="Create an ad group"
      >
        An ad group contains one or more ads which target a shared set of keywords.
      </q-step>

      <q-step
        :name="3"
        disable
        icon="assignment"
        title="Ad template"
      >
        This step won't show up because it is disabled.
      </q-step>

      <q-step
        :name="4"
        icon="add_comment"
        title="Create an ad"
      >
        Try out different ad text to see what brings in the most customers, and learn how to
        enhance your ads using features like ad extensions. If you run into any problems with
        your ads, find out how to tell if they're running and how to resolve approval issues.
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn :label="step === 4 ? 'Finish' : 'Continue'" color="primary" @click="$refs.stepper.next()"/>
          <q-btn v-if="step > 1" class="q-ml-sm" color="primary" flat label="Back" @click="$refs.stepper.previous()"/>
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>
</template>

<script>
export default {
  name: "posCheckoutForm",
  data() {
    return {
      step: 1,
      personDataError: false,
      formData: {
        name: '',
        phone: '',
        email: '',
        city: '',
        region: '',
        address: '',
        postalCode: ''
      }
    }
  },
}
</script>

<style lang="sass">

</style>
