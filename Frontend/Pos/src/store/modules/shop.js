import axiosInstance from "axios";

export default {
  actions: {
    async fetchCategoryData({commit}, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/category/${slug}/`).then(({data}) => {
          commit('setCategoryData', data)
        })
      } catch (e) {
        throw e
      }
    },
    async fetchLabelData({commit}, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/label/${slug}/`).then(({data}) => {
          commit('setLabelData', data)
        })
      } catch (e) {
        throw e
      }
    },
    async fetchBrandData({commit}, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/brand/${slug}/`).then(({data}) => {
          commit('setBrandData', data)
        })
      } catch (e) {
        throw e
      }
    },
    async fetchProductDetailData({commit}, slug) {
      try {
        await axiosInstance.get(`${this.getters.getServerURL}/shop/product/${slug}/`).then(({data}) => {
          commit('setProductData', data)
        })
      } catch (e) {
        throw e
      }
    },
    async loadSaleProducts({commit, state}) {
      if(!state.saleProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/home_sale_products/`)
            .then(({data}) => {
              commit('setSaleProducts', data.results)
            })
        } catch (e) {
          throw e
        }
      }
    },
    async  fetchLatestProducts({commit, state}) {
      if(!state.latestProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/latest_products/`)
            .then(({data}) => {
              commit('setLatestProducts', data)
            })
        }catch (e) {
          throw e
        }
      }
    },
    async fetchCategories({commit}) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/categories/`)
            .then(({data}) => {
              commit('setCategories', data)
            })
        }catch (e) {
          throw e
        }
    },
    async fetchHitProducts({commit, state}) {
      if(!state.hitProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/home_hit_products/`)
            .then(({data}) => {
              commit('setHitProducts', data)
            })
        }catch (e) {
          throw e
        }
      }
    },
    async fetchSaleProducts({commit, state}) {
      if (!state.saleProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/home_sale_products/`)
            .then(({data}) => {
              commit('setSaleProducts', data)
            })
        }catch (e) {
          throw e
        }
      }
    },
    async fetchFutureProducts({commit, state}) {
      if (!state.futureProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/shop/home_future_products/`)
            .then(({data}) => {
              commit('setFutureProducts', data)
            })
        }catch (e) {
          throw e
        }
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
    },
    setSaleProducts(state, data) {
      state.saleProducts = data
    },
    setCategories(state, data) {
      state.categories = data
    },
    setLatestProducts(state, data) {
      state.latestProducts = data
    },
    setHitProducts(state, data) {
      state.hitProducts = data
    },
    setFutureProducts(state, data) {
      state.futureProducts = data
    }

  },
  state: {
    category: {},
    label: {},
    brand: {},
    productDetailData: {},
    saleProducts: null,
    categories: [],
    latestProducts: null,
    hitProducts: null,
    futureProducts: null
  },
  getters: {
    getCategoryDetail: (state) => state.category,
    getLabelDetail: (state) => state.label,
    getBrandDetail: (state) => state.brand,
    getProductDetailData: (state) => state.productDetailData,
    getSaleProducts: (state) => state.saleProducts,
    getCategories: state => state.categories,
    getLatestProducts: state => state.latestProducts,
    getHitProducts: state => state.hitProducts,
    getFutureProducts: state => state.futureProducts,
  }
}
