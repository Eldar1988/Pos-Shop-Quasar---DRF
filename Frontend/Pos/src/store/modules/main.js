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
      state.mainDataUnloaded = false
      state.categories = data.categories
      state.pages = data.pages
      state.companyInfo = data.companyInfo
      state.homeSlider = data.slider
      state.hitProducts = data.hitProducts
      state.latestProducts = data.latestProducts
      state.reviews = data.reviews
      state.contacts = data.contacts
      state.benefits = data.benefits
      state.socials = data.socials
      state.siteSettings = data.settings
      state.brands = data.brands
      state.clients = data.clients
    },
    setMainDataUnloaded(state) {
      state.mainDataUnloaded = true
    }
  },
  state: {
    mainDataUnloaded: false,
    categories: [],
    pages: [],
    companyInfo: {},
    homeSlider: [],
    hitProducts: [],
    latestProducts: [],
    reviews: [],
    contacts: {},
    benefits: [],
    socials: [],
    siteSettings: {},
    brands: [],
    clients: []
  },
  getters: {
    getMainDataStatus: (state) => state.mainDataUnloaded,
    getCategories: (state) => state.categories,
    getPages: (state) => state.pages,
    getServerStatus: (state) => state.mainDataUnloaded,
    getCompanyInfo: (state) => state.companyInfo,
    getHomeSlider: (state) => state.homeSlider,
    getHitProducts: (state) => state.hitProducts,
    getLatestProducts: (state) => state.latestProducts,
    getShopReviews: (state) => state.reviews,
    getContacts: (state) => state.contacts,
    getBenefits: (state) => state.benefits,
    getSocials: (state) => state.socials,
    getSiteSettings: (state) => state.siteSettings,
    getBrands: (state) => state.brands,
    getClients: (state) => state.clients
  }
}
