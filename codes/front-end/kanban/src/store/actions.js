const actions = {
  login (context, data) {
    context.commit('UPDATE_LOGIN_STATE', data)
  }
}

export default actions
