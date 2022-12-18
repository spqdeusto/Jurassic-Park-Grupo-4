<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <ul id="example-1">
    <li v-for="offroad in off_roads" :key="offroad">
      {{ offroad.on_route }} | {{ offroad.n_visitors }}
    </li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data () {
    return {
      off_roads: []
    }
  },
  methods: {
    async getOffRoads () {
      const response = await axios.get('http://localhost:8000/offroad/get_all')
      this.off_roads = response.data
      console.log(this.off_roads)
    }
  },
  created () {
    this.getOffRoads()
  }
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
