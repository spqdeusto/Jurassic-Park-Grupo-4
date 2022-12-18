<template>
    <ul id="example-1">
    <li v-for="item in species" :key="item">
     {{ item.name }} <q-btn round color="black" v-on:click="deleteSpecie(item.id)" icon="my_location" />
    </li>
    </ul>
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
      data() {
        return {
            species: [],
            name: "",
        }
      },
      methods: {
        submitForm: function () {
          axios.post("http://localhost:8000/specie/create",{name: this.name}).then((response) => {
                this.response = JSON.stringify(response);
                console.log(response);
          });
        },
        async getSpecies () {
            const response = await axios.get('http://localhost:8000/specie/get_all')
            this.species = response.data
            console.log(this.species)
        },
        async deleteSpecie (id) {
            axios.post("http://localhost:8000/specie/delete",{specie_id: id}).then((response) => {
                this.response = JSON.stringify(response);
                console.log(response);
          });
        }
      },
      created () {
        this.getSpecies()
    }
    };
  </script>