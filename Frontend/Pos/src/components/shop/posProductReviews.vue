<template>
  <div class="q-pa-sm">
    <q-card
      v-if="reviews.length === 0"
      class="q-px-sm q-py-lg text-weight-regular shadow-0 bg-white"
    >
      Отзывов к данному товару еще нет.
    </q-card>
    <div
      v-for="i in reviews"
      :key="i.id"
    >

      <q-chat-message
        v-if="i.public"
        text-sanitize
        :name="i.name"
        bg-color="grey-2"
        class="q-px-md text-left text-weight-regular"
      >
        {{ i.text }} <br><br>
        Оценка:
        <q-rating v-model="i.rating" color="orange" readonly/>
      </q-chat-message>
    </div>
    <q-btn
      label="Добавить отзыв"
      icon-right="rate_review"
      class="text-bold full-width border-radius-6 q-mt-md q-py-sm"
      unelevated
      color="primary"
      @click="dialog = true"
    />

    <q-dialog
      v-model="dialog"
    >
      <q-card style="width: 500px; max-width: 90vw;">
        <q-toolbar class="bg-primary text-white">
          <q-toolbar-title class="flex justify-between" style="align-items: center">
            <div class="text-h6 text-bold">Новый отзыв</div>
            <q-icon name="close" class="cursor-pointer" v-close-popup/>
          </q-toolbar-title>

        </q-toolbar>


        <q-card-section class="text-center">
          <p class="text-bold text-h6">Ваша оценка: {{ review.rating }}</p>
          <q-rating v-model="review.rating" color="orange" size="28px" />
          <small v-if="!review.rating" class="text-negative"><br>{{ errorReviewRating }}</small>
          <q-input v-model="review.name" label="Ваше имя*" outlined type="text" class="q-mt-md"/>
          <small v-if="!review.name" class="text-negative block">{{ errorReviewName }}</small>

          <q-input v-model="review.text" label="Ваш отзыв*" outlined type="textarea" clearable clear-icon="backspace"
                   class="q-mt-md"/>
          <small v-if="!review.text" class="text-negative">{{ errorReviewText }}</small>
        </q-card-section>

        <q-card-actions align="center" class="bg-white text-teal q-px-md q-pb-md">
          <q-btn
            color="accent"
            label="Отправить отзыв"
            class="q-py-sm full-width text-bold red-shadow border-radius-6"
            icon-right="mark_chat_read"
            unelevated
            :loading="loading"
            @click="createReview"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "posProductReviews",
  props: {
    reviews: {
      type: Array,
      default: null
    },
    productId: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      review: {
        name: '',
        text: '',
        rating: ''
      },
      dialog: false,
      errorReviewName: '',
      errorReviewText: '',
      errorReviewRating: '',
      loading: false
    }
  },
  methods: {
    async createReview() {
      this.loading = true
      if (this.review.rating === '') {
        this.errorReviewRating = 'Необходимо поставить оценку'
        this.loading = false
        return null
      }
      if (this.review.name === '') {
        this.errorReviewName = 'Необходимо указать ваше имя'
        this.loading = false
        return null
      }
      if (this.review.text === '') {
        this.errorReviewText = 'Необходимо написать отзыв'
        this.loading = false
        return null
      }
      let data = this.review
      data.product = this.productId

      await fetch(`${this.$store.getters.getServerURL}/shop/create_review/`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      }).then(response => {
        if (response.status === 201) {
          setTimeout(() => {
            this.loading = false
            this.dialog = false
            this.review.name = ''
            this.review.text = ''
            this.$q.notify({message: 'Спасибо! Ваш отзыв скоро появится на сайте', position: 'top', color: 'positive'})
          }, 1000)
        } else {
          this.loading = false
          this.$q.notify({message: 'Ошибка! Извините, что-то пошло не так, попробуйте еще раз', position: 'top'})
        }
      })

    }
  }
}
</script>

<style scoped>

</style>
