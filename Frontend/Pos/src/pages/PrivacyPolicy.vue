<template>
<q-page>
  <pos-page-header :title="policy.title" />
  <section class="info-page">
    <div v-html="policy.body" class="border-radius-6 q-px-md q-py-md grey-border"></div>
  </section>
</q-page>
</template>

<script>
import PosPageHeader from "components/service/posPageHeader";
export default {
  name: "PrivacyPolicy",
  components: {PosPageHeader},
  data() {
    return {
      policy: {}
    }
  },
  created() {
    this.loadPolicy()
  },
  methods: {
    async loadPolicy() {
      this.policy = await this.$axios.get(`${this.$store.getters.getServerURL}/privacy_policy/`).then(({data}) => {
        return data
      })
    }
  }
}
</script>

<style scoped>

</style>
