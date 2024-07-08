<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import { getMessage } from '@/utility/functions'

export default {
  name: 'PingRoute',
  data() {
    return {
      msg: ''
    }
  },
  async created() {
    this.msg = await getMessage('ping')
  }
}
</script>