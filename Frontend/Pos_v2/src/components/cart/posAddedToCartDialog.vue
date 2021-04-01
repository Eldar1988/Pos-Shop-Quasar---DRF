<template>
<div>
    <q-card
      square
      style="width: 100%;" class="shadow-20 q-pa-sm" >
      <div class="flex justify-end">
        <q-btn icon="close" flat color="dark" dense v-close-popup/>
      </div>
      <div class="flex justify-center">
        <q-img
          :src="product.image"
          contain
          height="50px"
        />
        <p class="text-center q-py-md">Товар '{{ product.title }}' добавлен в корзину</p>
        <q-btn to="/cart" label="Перейти в корзину"  class="full-width q-mt-sm text-bold" color="accent" unelevated />
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
