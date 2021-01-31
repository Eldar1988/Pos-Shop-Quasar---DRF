<template>
<q-page>
<section class="info-page">
  <script type="application/ld+json" v-html="schema"></script>
  <script type="application/ld+json" v-html="navigateSchema"></script>
  <q-breadcrumbs class="q-pa-sm q-mt-md">
    <q-breadcrumbs-el icon="home" to="/"/>
    <q-breadcrumbs-el label="Вопросы и ответы"/>
  </q-breadcrumbs>
  <pos-page-header title="Ответы на часто задаваемые вопросы" />
  <div>
    <q-expansion-item
      v-for="question in questions"
      :key="question.id"
      switch-toggle-side group=""

      :label="question.question"
      class="border-radius-6 bg-white text-bold q-mt-md" dense-toggle
    >
      <q-card>
        <q-card-section class="text-weight-regular">
          <div v-html="question.answer"></div>
        </q-card-section>
      </q-card>
    </q-expansion-item>

  </div>
  <pos-share class="q-mt-xl" :image="this.$store.getters.getCompanyInfo.logo" description="Ответы на часто задаваемые вопросы" />
</section>
</q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
import PosShare from "components/service/posShare";
export default {
  name: "Questions",
  components: {PosShare, PosPageHeader},
  computed: {
    questions () {
      return this.$store.getters.getQuestions
    },
    schema() {
      let questions = this.$store.getters.getQuestions
      let answers = []
      questions.forEach((item) => {
        let answer = {
          "@type": "Question",
          "name": item.question,
          "acceptedAnswer": {
            "@type": "Answer",
            "text": item.answer
          }
        }
        answers.push(answer)
      })
      return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": answers
      }
    },
    navigateSchema() {
      return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
          "@type": "ListItem",
          "position": 1,
          "name": "Вопросы и ответы",
          "item": `${this.$store.getters.getCompanyInfo.site_url}/questions`
        }]
      }
    }
  },
  preFetch({ store }) {
    return store.dispatch('fetchQuestions')
  },
  meta() {
    let siteTitle = this.$store.getters.getCompanyInfo.name
    return {
      title: `Вопросы и ответы | ${siteTitle}`,
      meta: {
        description: {
          name: "description",
          content: "На этой странице вы найдете вопросы на часто задаваемые вопросы.",
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: `Вопросы и ответы | ${siteTitle}`,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.getters.getCompanyInfo.site_url}/questions`,
        },
        ogDescription: {
          property: "og:description",
          content: "На этой странице вы найдете вопросы на часто задаваемые вопросы.",
        },
        ogImage: {
          property: "og:image",
          content: `${this.$store.getters.getCompanyInfo.logo}`
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
