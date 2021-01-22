import axiosInstance from "axios"

export default {
  actions: {
    fetchPageData({ commit }, slug) {
      axiosInstance.get(`${this.getters.getServerURL}/info_page/${slug}/`).then(({data}) => {
        commit('setPageData', data)
      })
    }
  },
  mutations: {
    setPageData(state, data) {
      state.pageData = data
    }
  },
  state: {
    pageData: {}
  },
  getters: {
    getPageData: (state) => state.pageData
  }
}
