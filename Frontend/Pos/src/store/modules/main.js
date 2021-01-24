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
      state.reviews = data.reviews
      state.contacts = data.contacts
      state.benefits = data.benefits
      state.socials = data.socials
      state.siteSettings = data.settings
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
    reviews: [],
    contacts: {},
    benefits: [],
    socials: [],
    siteSettings: {}
  },
  getters: {
    getMainDataStatus: (state) => state.mainDataUnloaded,
    getCategories: (state) => state.categories,
    getPages: (state) => state.pages,
    getServerStatus: (state) => state.mainDataUnloaded,
    getCompanyInfo: (state) => state.companyInfo,
    getHomeSlider: (state) => state.homeSlider,
    getHitProducts: (state) => state.hitProducts,
    getShopReviews: (state) => state.reviews,
    getContacts: (state) => state.contacts,
    getBenefits: (state) => state.benefits,
    getSocials: (state) => state.socials,
    getSiteSettings: (state) => state.siteSettings,
  }
}
