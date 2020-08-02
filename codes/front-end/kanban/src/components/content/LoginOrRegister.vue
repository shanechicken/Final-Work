<template>
  <div class="LoginOrRegister">
    <el-tabs :stretch="true" v-model="activeTab" @tab-click="handleClick">
      <el-tab-pane label="登录" name="Login">
        <el-form label-position="left" label-width="80px" :model="LoginData" class="formTab">
          <el-form-item label="项目名">
            <el-input placeholder="请输入项目名" v-model="LoginData.project_id"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input placeholder="请输入密码" v-model="LoginData.password" show-password></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" @click="userLogin">立即登录</el-button>
      </el-tab-pane>
      <el-tab-pane label="注册" name="Register">
        <el-form label-position="left" label-width="80px" :model="RegisterData" class="formTab">
          <el-form-item label="项目名">
            <el-input placeholder="请输入项目名" v-model="RegisterData.project_id"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input placeholder="请输入密码" v-model="RegisterData.password" show-password></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" @click="userRegister">立即注册</el-button>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginOrRegister',
  data () {
    return {
      activeTab: 'Login',
      LoginData: {
        project_id: '',
        password: ''
      },
      RegisterData: {
        project_id: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions(['login']),
    handleClick (tab, event) {
      console.log(tab, event)
    },
    userLogin () {
      fetch('/api/signin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.LoginData)
      }).then(res => res.json())
        .then(json => {
          if (json.message) {
            this.$message({
              message: '登录成功',
              type: 'success',
              center: true
            })
            this.login(this.LoginData.project_id)
          } else {
            this.$message({
              message: '登录失败',
              type: 'error',
              center: true
            })
          }
        })
    },
    userRegister () {
      fetch('/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.RegisterData)
      }).then(res => res.json())
        .then(json => {
          if (json.message) {
            this.$message({
              message: '注册成功',
              type: 'success',
              center: true
            })
            this.LoginData = {...this.RegisterData}
            this.activeTab = 'Login'
          } else {
            this.$message({
              message: '注册失败',
              type: 'error',
              center: true
            })
          }
        })
    }
  }
}
</script>

<style scoped>
.LoginOrRegister {
  width: 20rem;
  height: 25rem;
  box-shadow: 1px 1px 10px #888888;
  margin: 2rem auto;
}
.formTab {
  width: 80%;
  margin: 4rem auto;
}
</style>
