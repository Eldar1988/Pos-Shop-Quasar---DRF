import axiosInstance from "axios";
import {colors} from "quasar";

export default {
  actions: {
    async fetchMainData({ commit, state }) {
      if (state.mainDataUnloaded) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/`).then(({data}) => {
            commit('setMainData', data)
            colors.setBrand('primary', data.settings.colors.primary_color)
            colors.setBrand('accent', data.settings.colors.accent_color)
            colors.setBrand('positive', data.settings.colors.positive_color)
            colors.setBrand('negative', data.settings.colors.alert_color)
            colors.setBrand('info', data.settings.colors.footer_color)
            colors.setBrand('dark', data.settings.colors.body_color)
          })
        } catch(e) {
          commit('setMainDataUnloaded')
        }
      }
      else {
        return null
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
    mainDataUnloaded: true,
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
