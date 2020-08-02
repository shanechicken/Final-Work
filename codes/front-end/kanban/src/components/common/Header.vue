<template>
  <div class="Header">
    <img src="../../../static/images/SYSU-IT.png" class="logo" />
    <el-dropdown class="userInfo">
      <div class="el-dropdown-link">
        <el-avatar src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png" alt="头像"></el-avatar>
      </div>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      msg: 'SYSU-IT'
    }
  }
}
</script>

<style scoped>
.Header {
  width: 100%;
  height: 4rem;
  background: rgba(44, 152, 224, 0.8);
  padding-top: 1rem;
}
.userInfo {
  width: 3rem;
  height: 3rem;
  margin-left: calc(100% - 360px);
  margin-top: 0.2rem;
}
.logo {
  height: 3rem;
  float: left;
}
</style>
