<template>
  <div class="ContentContainer">
    <div class="Content">
      <LoginOrRegister v-if="!hasLogin" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import LoginOrRegister from './LoginOrRegister'

export default {
  name: 'Content',
  components: {
    LoginOrRegister
  },
  data () {
    return {
      msg: 'IT-kanban'
    }
  },
  computed: {
    ...mapGetters(['hasLogin'])
  }
}
</script>

<style scoped>
.ContentContainer {
  width: 100%;
  height: calc(100% - 7rem - 16px);
  overflow: hidden;
}
.Content {
  width: calc(100% + 20px);
  height: 100%;
}
</style>
