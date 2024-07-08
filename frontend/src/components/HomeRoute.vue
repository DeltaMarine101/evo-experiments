<template>
  <div class="content">
    <p>{{ msg }}</p>
    <el-button color="#626aef" @click="() => sendMessage('object_test', { name: `testing_22`, age: 34.5 })"> Run </el-button>
  </div>
</template>

<script lang="ts">
import { getMessage, sendMessage } from '@/utility/functions';
import type { TestMessage } from '@/utility/interface';
import { ElButton } from 'element-plus';

export default {
  name: 'HomeRoute',
  components: { ElButton },
  async beforeMount() {
    this.msg = (await getMessage('object_test')) as TestMessage
  },
  data() {
    return {
      msg: {}
    }
  },
  methods: {
    sendMessage
  }
}
</script>