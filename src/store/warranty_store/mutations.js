const mutations = {
  SET_CURRENT_WARRANTY (state, data) {
    state.warranty = data.warranty
    state.components = data.components
  }
}

export default mutations
