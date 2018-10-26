import state from './state'
import mutations from './mutations'
import actions from './actions'

const warrantyStore = {
  namespaced: true,
  state,
  mutations,
  actions
}

export default warrantyStore
