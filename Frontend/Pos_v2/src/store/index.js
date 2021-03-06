import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main'
import shop from './modules/shop'
import pages from './modules/pages'
import services from './modules/services'
import products from './modules/products'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      main,
      shop,
      pages,
      services,
      products
    },
    state: {
      kaspiButton: false,
      // serverURL: 'http://192.168.0.199:8000'
      // serverURL: 'https://max-shop.kz.na4u.ru'
      // serverURL: 'https://dj.posshop.kz.na4u.ru'
      // serverURL: 'https://shop.js-code.ru'
      serverURL: 'https://vitahim.kz.na4u.ru'
      // serverURL: 'https://doors.kz.na4u.ru'
      // serverURL: 'https://astamatrasy.kz.na4u.ru'
      // serverURL: 'https://max-shop.kz.na4u.ru'
    },
    getters: {
      getServerURL:(state) => state.serverURL
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
