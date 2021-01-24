import axiosInstance from "axios"

export default {
  actions: {
    fetchPageData({ commit }, slug) {
      axiosInstance.get(`${this.getters.getServerURL}/info_page/${slug}/`).then(({data}) => {
        commit('setPageData', data)
      })
    },
    fetchAboutShopInfo({commit}) {
      axiosInstance.get(`${this.getters.getServerURL}/about/`).then(({data}) => {
        commit('setAboutShopInfo', data)
      })
    },
    fetchQuestions({commit}) {
      axiosInstance.get(`${this.getters.getServerURL}/questions/`).then(({data}) => {
        commit('setQuestions', data)
      })
    }
  },
  mutations: {
    setPageData(state, data) {
      state.pageData = data
    },
    setAboutShopInfo(state, data) {
      state.aboutShopInfo = data
    },
    setQuestions(state, data) {
      state.questions = data
    },
  },
  state: {
    pageData: {},
    aboutShopInfo: {},
    questions: []
  },
  getters: {
    getPageData: (state) => state.pageData,
    getAboutShopInfo: (state) => state.aboutShopInfo,
    getQuestions: (state) => state.questions
  }
}
