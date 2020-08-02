<template>
  <div class="KanBanDetail">
    <div class="grid-content-container bg-purple-dark">
      <div>
        <el-button
          type="primary"
          icon="el-icon-plus"
          class="add-btn"
          size="small"
          @click="() => {
            currentBlock = 'todo'
            dialogFormVisible = true;
          }"
          >添加</el-button
        >
      </div>
      <div class="grid-content" id="todo">
        <BoxCard v-for="item in toDoList" :key="item" :title="item" :getCardList="getCardList" />
      </div>
    </div>
    <div class="grid-content-container bg-purple">
      <div>
        <el-button
          type="primary"
          icon="el-icon-plus"
          class="add-btn"
          size="small"
          @click="() => {
            currentBlock = 'inprogress'
            dialogFormVisible = true;
          }"
          >添加</el-button
        >
      </div>
      <div class="grid-content" id="inprogress">
        <BoxCard v-for="item in inProgressList" :key="item" :title="item" :getCardList="getCardList" />
      </div>
    </div>
    <div class="grid-content-container bg-purple-light">
      <div>
        <el-button
          type="primary"
          icon="el-icon-plus"
          class="add-btn"
          size="small"
          @click="() => {
            currentBlock = 'done'
            dialogFormVisible = true;
          }"
          >添加</el-button
        >
      </div>
      <div class="grid-content" id="done">
        <BoxCard v-for="item in doneList" :key="item" :title="item" :getCardList="getCardList" />
      </div>
    </div>
    <el-dialog title="添加卡片" :visible.sync="dialogFormVisible">
      <el-form :model="formData">
        <el-form-item label="任务名：" label-width="120px">
          <el-input v-model="formData.task_name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addCard">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import dragula from 'dragula'
import * as $ from 'jquery'
import { mapGetters } from 'vuex'

import BoxCard from './BoxCard'

export default {
  name: 'KanBanDetail',
  components: {
    BoxCard
  },
  data () {
    return {
      drake: null,
      toDoList: [],
      doneList: [],
      inProgressList: [],
      formData: {
        project_id: '',
        task_name: ''
      },
      dialogFormVisible: false,
      currentBlock: 'todo'
    }
  },
  computed: {
    ...mapGetters(['projectId'])
  },
  created () {
    this.getCardList('todo')
    this.getCardList('inprogress')
    this.getCardList('done')
  },
  mounted () {
    this.drake = dragula(Array.from($('.grid-content')), {
      isContainer: function (el) {
        return false // 点击和拖动都会触发，drake.containers元素将被考虑
      },
      moves: function (el, source, handle, sibling) {
        return true // 一直能拖动，拖动时触发
      },
      accepts: function (el, target, source, sibling) {
        return true // 元素可以放在任何`container`中
      },
      invalid: function (el, handle) {
        return false // 默认情况下不会阻止任何拖动
      },
      direction: 'vertical', // 元素的排放方向
      copy: false, // 拖动的元素是否为副本
      copySortSource: false, // 复制的源容器重新排序
      revertOnSpill: false, // 是否将拖到容器外的元素放回原处
      removeOnSpill: false, // 是否将拖到容器外的元素删除
      mirrorContainer: document.body, // 设置获取附加镜像元素的元素
      ignoreInputTextSelection: true // 允许用户选择输入文本
    })
      .on('drag', (el, source) => {
        this.$emit('drag', el, source)
        el.classList.add('is-moving')
        this.currentBlock = $(el).parent()[0].id
      })
      .on('dragend', (el) => {
        this.$emit('dragend', el)
        el.classList.add('is-moved')
        el.classList.remove('is-moving')
        window.setTimeout(() => {
          el.classList.remove('is-moved')
        }, 600)
        if ($(el).parent()[0].id !== this.currentBlock) {
          fetch('/api/task', {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              project_id: this.projectId,
              task_name: $(el).attr('title'),
              new_status: {
                todo: 1,
                inprogress: 2,
                done: 3
              }[$(el).parent()[0].id]
            })
          }).then(res => res.json())
            .then(json => {
              if (json.message) {
                this.$message({
                  message: '移动成功',
                  type: 'success',
                  center: true
                })
              } else {
                this.$message({
                  message: '移动失败',
                  type: 'error',
                  center: true
                })
              }
            })
        }
      })
      .on('cancel', (el, container, source) => {
        this.$emit('cancel', el, container, source)
      })
      .on('remove', (el, container, source) => {
        this.$emit('remove', el, container, source)
      })
      .on('shadow', (el, container, source) => {
        this.$emit('shadow', el, container, source)
      })
      .on('over', (el, container, source) => {
        this.$emit('over', el, container, source)
      })
      .on('out', (el, container, source) => {
        this.$emit('out', el, container, source)
      })
      .on('cloned', (clone, original, type) => {
        this.$emit('cloned', clone, original, type)
      })
    this.$emit('init', this.drake)
  },
  methods: {
    getCardList (type) {
      fetch(`/api/${type}?project_id=${this.projectId}`).then(res => res.json()).then(json => {
        switch (type) {
          case 'todo':
            this.toDoList = json[type]
            break
          case 'inprogress':
            this.inProgressList = json[type]
            break
          case 'done':
            this.doneList = json[type]
            break
        }
      })
    },
    addCard () {
      this.formData.project_id = this.projectId
      fetch(`/api/${this.currentBlock}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.formData)
      }).then(res => res.json())
        .then(json => {
          if (json.message) {
            this.$message({
              message: '创建成功',
              type: 'success',
              center: true
            })
            this.getCardList(this.currentBlock)
          } else {
            this.$message({
              message: '创建失败',
              type: 'error',
              center: true
            })
          }
          this.dialogFormVisible = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
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
  height: 98%;
  min-width: 250px;
  margin: auto 5px;
  display: inline-block;
  overflow: hidden;
}
.grid-content {
  width: calc(100% + 20px);
  height: calc(100% + 20px);
  overflow-y: scroll;
}
.add-btn {
  margin-left: calc(100% - 80px);
  margin-top: 10px;
}
</style>
