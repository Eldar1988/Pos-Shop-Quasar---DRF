<template>
  <div>
    <p class="text-bold q-pb-sm">Поделиться с друзьями:</p>
    <yandex-share :services="['whatsapp', 'telegram', 'vkontakte','facebook','twitter', 'odnoklassniki', 'pinterest']" :description="description" :image="image" />
  </div>
</template>

<script>
import YandexShare from '@cookieseater/vue-yandex-share';
export default {
  components: {YandexShare},
  props: {
    description: {
      type: String,
      default: ''
    },
    image: {
      type: String,
      default: ''
    }
  },
  created() {
  },
  name: "posShare"
}
</script>

<style scoped>

</style>
