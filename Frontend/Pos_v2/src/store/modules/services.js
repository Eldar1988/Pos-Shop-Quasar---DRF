import axiosInstance from "axios"
import notifier from "src/functions/notifier"

export default {
  state: {
    serviceCategories: null,
    allServices: null,
    serviceCategory: null,
    service: null
  },

  actions: {
    async fetchServiceCategories({commit}) {
      try{
        await axiosInstance.get(`${this.getters.getServerURL}/services/categories/`)
          .then(({data}) => {
            commit('setServiceCategories', data)
          })
      } catch (e) {
        notifier(`Не удалось загрузить категории услуг. Ошибка сервера: ${e.message}`)
      }
    },

    async fetchAllServices({commit}) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/services/all_services/`)
          .then(({data}) => {
            commit('setAllServices', data)
          })
      } catch (e) {
        notifier(`Не удалось загрузить услуги. Ошибка сервера: ${e.message}`)
      }
    },

    async fetchServiceCategoryDetail({commit}, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/services/category/${slug}/`)
          .then(({data}) => {
            commit('setCategory', data)
          })

      } catch (e) {
        notifier(`Не удалось загрузить услуги. Ошибка сервера: ${e.message}`)
      }
    },

    async fetchServiceDetail({commit}, id) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/services/service/${id}/`)
          .then(({data}) => {
            commit('setService', data)
          })

      } catch (e) {
        notifier(`Не удалось загрузить услугу. Ошибка сервера: ${e.message}`)
      }
    }
  },

  mutations: {
    setServiceCategories(state, data) {
      state.serviceCategories = data
    },
    setAllServices(state, data) {
      state.allServices = data
    },
    setCategory(state, data) {
      state.serviceCategory = data
    },
    setService(state, data) {
      state.service = data
    }
  },

  getters: {
    getServiceCategories: state => state.serviceCategories,
    getAllServices: state => state.allServices,
    getServiceCategoryDetail: state => state.serviceCategory,
    getService: state => state.service
  }
}
