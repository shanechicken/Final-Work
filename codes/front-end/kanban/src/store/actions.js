const actions = {
  login (context, data) {
    context.commit('UPDATE_LOGIN_STATE', true)
    context.commit('UPDATE_PROJECT_ID', data)
  }
}

export default actions
