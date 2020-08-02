<template>
  <div class="KanBanDetail">
    <div class="grid-content-container bg-purple-dark">
      <div class="grid-content">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>卡片名称</span>
            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
          </div>
          <div>
            Content
          </div>
        </el-card>
      </div>
    </div>
    <div class="grid-content-container bg-purple">
      <div class="grid-content">
      </div>
    </div>
    <div class="grid-content-container bg-purple-light">
      <div class="grid-content">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'KanBanDetail',
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.KanBanDetail {
  margin-top: 1rem;
  width: 100%;
  height: calc(100% - 1rem);
  overflow-y: scroll;
  text-align: left;
}

.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content-container {
  border-radius: 4px;
  min-height: 550px;
  min-width: 250px;
  margin: auto 5px;
  display: inline-block;
  overflow: hidden;
}
.grid-content {
  width: calc(100% + 20px);
  overflow-y: scroll;
}
.box-card {
  width: calc(100% - 20px);
  margin-left: 7px;
  margin-top: 10px;
}
</style>
