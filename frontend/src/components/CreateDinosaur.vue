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
        <input 
          v-model="specie_id"
          type="number"
          placeholder="Introduce la especie del dinosaurio" 
        /><br>

        <span>Age</span><br>
        <input 
          v-model="age"
          type="number"
          placeholder="Introduce la edad del dinosaurio" 
        /><br>
        <span>Weight</span><br>
        <input 
          v-model="weight"
          type="number"
          placeholder="Introduce el peso del dinosaurio" 
        /><br>

        <span>Gender</span><br>
        <select required name="gender" id="gender" v-model="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <span>Dangerousness</span><br>
        <select required name="dangerousness" id="dangerousness" v-model="dangerousness">
          <option value="peaceful">Peaceful</option>
          <option value="aggresive">Aggresive</option>
        </select>

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
const axiosInstance = axios.create({
  headers: {
    "Access-Control-Allow-Origin":"*"
  }
});

    export default {
      data() {
        return {
          name: "",
          specie_id: 0,
          gender: "",
          age: 0,
          weight: 0,
          dangerousness: "",
          enclosure_id: 1,
        };
      },
      methods: {
        submitForm: function () {
          axiosInstance.post(
            "http://localhost:8000/dinosaur/create",
            {name: this.name,
            specie_id: this.specie_id,
            age: this.age,
            weight: this.weight,
            gender: this.gender,
            dangerousness: this.dangerousness,
            enclosure_id: this.enclosure_id
          }).then((response) => {
            this.response = JSON.stringify(response);
            console.log(response);
          });
        }
      }
        };
  </script>
  <style>

  </style>