import axiosInstance from "axios"
import notifier from "src/functions/notifier"

export default {
  state: {
    productsData: null,
    productsLoading: false
  },

  actions: {
    async fetchShopProducts({commit, state}, params) {
      commit('changeProductsLoading', true)
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/products/?${params}`)
          .then(({data}) => commit('setProductsData', data))
      } catch (e) {
        notifier(`Не удалось загрузить товары. Ошибка сервера: ${e.message}`)
      }
    }
  },

  mutations: {
    setProductsData(state, data) {
      state.productsData = data
      this.commit('changeProductsLoading', false)
    },
    changeProductsLoading(state, status) {
      state.productsLoading = status
    }
  },

  getters: {
    getShopProductsData: state => state.productsData,
    getProductsLoading: state => state.productsLoading
  }
}
