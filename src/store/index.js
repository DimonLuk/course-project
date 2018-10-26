import Vue from 'vue'
import Vuex from 'vuex'
import warrantyStore from './warranty_store'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    warrantyStore
  }
})

export default store
