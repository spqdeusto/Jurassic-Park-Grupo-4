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
    <li v-for="item in dinosaurs" :key="item">
      {{ item.name }} | {{ item.age }}
    </li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data () {
    return {
      dinosaurs: []
    }
  },
  methods: {
    async getDinosaurs () {
      const response = await axios.get('http://localhost:8000/dinosaur/get_all')
      this.dinosaurs = response.data
      console.log(this.dinosaurs)
    }
  },
  created () {
    this.getDinosaurs()
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
