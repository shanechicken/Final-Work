<template>
  <div class="box-card" :title="title" ref='box-card'>
    <el-card>
      <div slot="header" class="clearfix">
        <span>{{ title || "标题" }}</span>
        <el-dropdown class="card-op" @command="handleCommand">
          <div class="el-dropdown-link">
            <i class="el-icon-more"></i>
          </div>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="delete">删除</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div>
        <input type="hidden" :value="cardType" />
        {{ content || "描述" }}
      </div>
    </el-card>
    <el-dialog
      title="提示"
      :visible.sync="centerDialogVisible"
      width="30%"
      center>
      <span>您确定要删除这个任务卡片吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="centerDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteCard">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import * as $ from 'jquery'

export default {
  name: 'KanBanDetail',
  props: {
    title: String,
    content: String,
    cardType: String,
    getCardList: Function
  },
  data () {
    return {
      centerDialogVisible: false
    }
  },
  computed: {
    ...mapGetters(['projectId'])
  },
  created () {
  },
  methods: {
    deleteCard () {
      fetch(`/api/task?project_id=${this.projectId}&task_name=${$('.box-card').attr('title')}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
        .then(json => {
          if (json.message) {
            this.$message({
              message: '删除成功',
              type: 'success',
              center: true
            })
            this.getCardList($('.box-card').parent()[0].id)
          } else {
            this.$message({
              message: '删除失败',
              type: 'error',
              center: true
            })
          }
        })
      this.centerDialogVisible = false
    },
    handleCommand (command) {
      this.centerDialogVisible = true
    }
  }
}
</script>

<style lang="scss" scoped>
.box-card {
  width: calc(100% - 30px);
  margin-left: 13px;
  margin-top: 20px;
  cursor: move;
}
.box-card.is-moving {
  transform: scale(1.08);
  transition-duration: .5s;
}
.box-card.is-moved {
  transform: scale(1);
  transition-duration: .5s;
}
.card-op {
  float: right;
  margin-top: -8px;
  cursor: pointer;
}
</style>
