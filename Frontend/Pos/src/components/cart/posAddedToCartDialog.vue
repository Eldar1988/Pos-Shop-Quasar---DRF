<template>
<div>
    <q-card style="width: 100%;" class="shadow-20 q-pa-sm" >
      <div class="flex justify-end">
        <q-btn icon="close" flat color="dark" dense v-close-popup/>
      </div>
      <div class="flex justify-center">
        <q-img
          :src="product.image"
          contain
          height="50px"
        />
        <p class="text-center">{{ product.title }} добавлен в корзину</p>
        <q-btn to="/cart" label="Перейти в корзину" class="full-width border-radius-6 q-mt-sm text-bold" color="primary" unelevated />
      </div>
    </q-card>
</div>
</template>

<script>
export default {
name: "posAddedToCartDialog",
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      dialog: true
    }
  },
}
</script>

<style scoped>

</style>
