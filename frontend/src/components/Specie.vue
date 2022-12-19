<template>
  <table>
    <tr>
      <th>Id</th>
      <th>Name</th>
      <th>Delete</th>
    </tr>
    <tr v-for="item in species" :key="item">
      <td>{{ item.id }}</td>
      <td>{{ item.name }}</td>
      <td align="center"><q-btn round color="red" v-on:click="deleteSpecie(item.id)" icon="delete_outline" /></td>
    </tr>
  </table>
  <hr>
  <div>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
        <span>Name</span><br>
        <input 
          v-model="name"
          type="text"
          placeholder="Introduce el nombre de la especie" 
        /><br>

        <input 
          class="submit" 
          type="submit" 
          value="Submit"
        >
      </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      species: [],

      name: ""
    }
  },
  methods: {
    async getSpecies () {
      const response = await axios.get('http://localhost:8000/specie/get_all')
      this.species = response.data
    },
    deleteSpecie(id) {
      axios.get("http://localhost:8000/specie/delete/"+id)
      setTimeout(() => this.getSpecies(), 500);
    },
    submitForm: function () {
      axios.post(
        "http://localhost:8000/specie/create",
        {name: this.name
      }).then((response) => {
        this.response = JSON.stringify(response);
      });
      setTimeout(() => this.getSpecies(), 500);
    },
  },
  created () {
    this.getSpecies()
  }
}
</script>