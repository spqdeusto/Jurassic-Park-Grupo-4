<template>
    <div>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
        <span>Name</span><br>
        <input 
          v-model="name"
          type="text"
          placeholder="Introduce el nombre del dinosaurio" 
        /><br>

        <span>Specie</span><br>
        <select required name="species" id="species" v-model="specie">
          <option v-for="specie in species" :value="specie">
            {{ specie.name }}
          </option>
        </select><br>

        <span>Age</span><br>
        <input 
          v-model="age"
          type="number"
          placeholder="Introduce la edad del dinosaurio" 
          min="0"
          max="300"
          
        /><br>

        <span>Weight</span><br>
        <input 
          v-model="weight"
          type="number"
          placeholder="Introduce el peso del dinosaurio"
          min="0"
        /><br>

        <span>Gender</span><br>
        <select required name="gender" id="gender" v-model="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select><br>

        <span>Dangerousness</span><br>
        <select required name="dangerousness" id="dangerousness" v-model="dangerousness">
          <option value="peaceful">Peaceful</option>
          <option value="aggressive">Aggressive</option>
        </select><br>

        <span>Enclosure</span><br>
        <select required name="enclosures" id="enclosures" v-model="enclosure">
          <option v-for="enclosure in enclosures" :value="enclosure">
            {{ enclosure.name }}
          </option>
        </select><br>
        
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
/*const axiosInstance = axios.create({
  headers: {
    "Access-Control-Allow-Origin":"*"
  }
}); */

    export default {
      data() {
        return {
          name: "",
          specie: {},
          enclosure: {},
          gender: "",
          age: 0,
          weight: 0,
          dangerousness: "",
          enclosures: [],
          species: [],
        };
      },
      methods: {
        submitForm: function () {
          axios.post(
            "http://localhost:8000/dinosaur/create",
            {name: this.name,
            specie_id: this.specie.id,
            age: this.age,
            weight: this.weight,
            gender: this.gender,
            dangerousness: this.dangerousness,
            enclosure_id: this.enclosure.id
          }).then((response) => {
            this.response = JSON.stringify(response);
            console.log(response);
          });
        },
        async getSpecies () {
          const response = await axios.get('http://localhost:8000/specie/get_all')
          this.species = response.data
          console.log(this.species)
        },
        async getEnclosures () {
          const response = await axios.get('http://localhost:8000/enclosure/get_all')
          this.enclosures = response.data
          console.log(this.enclosures)
        }
        },
        created () {
          this.getSpecies()
          this.getEnclosures()
        }
      };
  </script>
  <style>
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    margin: 0; 
}
  </style>