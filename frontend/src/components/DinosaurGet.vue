<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <table style="width:100%">
    <tr>
      <th>Id</th>
      <th>Name</th>
      <th>Specie Id</th>
      <th>Age</th>
      <th>Weight</th>
      <th>Gender</th>
      <th>Dangerousness</th>
      <th>Enclosure Id</th>
    </tr>
    <tr v-for="item in dinosaurs" :key="item">
      <td>{{ item.id }}</td>
      <td>{{ item.name }}</td>
      <td>{{ item.specie_id }}</td>
      <td>{{ item.age }}</td>
      <td>{{ item.weight }}</td>
      <td>{{ item.gender }}</td>
      <td>{{ item.dangerousness }}</td>
      <td>{{ item.enclosure_id }}</td>
    </tr>
  </table>
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
