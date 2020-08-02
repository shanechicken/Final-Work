<template>
  <div class="Index">
    <Header />
    <Content />
    <Footer />
  </div>
</template>

<script>
import Header from './common/Header'
import Footer from './common/Footer'
import Content from './Content'

export default {
  name: 'Index',
  components: {
    Header,
    Footer,
    Content
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
.Index {
  width: 100%;
  height: 100%;
}
</style>
