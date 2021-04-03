import axiosInstance from "axios"
import notifier from "src/functions/notifier"

export default {
  state: {
    products: null
  },

  actions: {
    async fetchProducts({commit}, params) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/products/?${params}`)
          .then(({data}) => commit('setProducts'), data)
      } catch (e) {
        notifier(`Не удалось загрузить товары. Ошибка сервера: ${e.message}`)
      }
    }
  },

  mutations: {
    setProducts(state, data) {
      state.products = data
    }
  },

  getters: {
    getShopProducts: state => state.products
  }
}
