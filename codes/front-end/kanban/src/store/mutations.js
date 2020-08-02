const mutations = {
  UPDATE_LOGIN_STATE (state, data) {
    state.hasLogin = data
  },
  UPDATE_PROJECT_ID (state, data) {
    state.projectId = data
  }
}

export default mutations
