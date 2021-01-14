import axiosInstance from "axios";

export default {
  actions: {
    async fetchMainData({ commit }) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/`).then(({data}) => {
          commit('setMainData', data)
        })
      } catch(e) {
        commit('setMainDataUnloaded')
        }
    }
  },
  mutations: {
    setMainData(state, data) {
      state.categories = data.categories
      state.pages = data.pages
    },
    setMainDataUnloaded(state) {
      state.mainDataUnloaded = true
    }
  },
  state: {
    mainDataUnloaded: false,
    categories: [],
    pages: []
  },
  getters: {
    getMainDataStatus: (state) => state.mainDataUnloaded,
    getCategories: (state) => state.categories,
    getPages: (state) => state.pages
  }
}
