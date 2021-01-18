import axiosInstance from "axios";

export default {
  actions: {
    async fetchCategoryData({ commit }, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/category/${slug}/`).then(({data}) => {
          commit('setCategoryData', data)
        })
      } catch(e) {
        throw e
      }
    },
    async fetchLabelData({ commit }, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/label/${slug}/`).then(({data}) => {
          commit('setLabelData', data)
        })
      } catch(e) {
        throw e
      }
    },
    async fetchBrandData({ commit }, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/brand/${slug}/`).then(({data}) => {
          commit('setBrandData', data)
        })
      } catch(e) {
        throw e
      }
    },
    async fetchProductDetailData({ commit }, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/product/${slug}/`).then(({data}) => {
          commit('setProductData', data)
        })
      } catch(e) {
        throw e
      }
    }
  },
  mutations: {
    setCategoryData(state, data) {
      state.category = data
    },
    setLabelData(state, data) {
      state.label = data
    },
    setBrandData(state, data) {
      state.brand = data
    },
    setProductData(state, data) {
      state.productDetailData = data
    }
  },
  state: {
    category: {},
    label: {},
    brand: {},
    productDetailData: {}
  },
  getters: {
    getCategoryDetail: (state) => state.category,
    getLabelDetail: (state) => state.label,
    getBrandDetail: (state) => state.brand,
    getProductDetailData: (state) => state.productDetailData,
  }
}
