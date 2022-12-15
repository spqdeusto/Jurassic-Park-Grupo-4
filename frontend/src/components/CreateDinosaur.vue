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
          v-model="specie"
          type="text"
          placeholder="Introduce la especie del dinosaurio" 
        /><br>

        <span>Age</span><br>
        <input 
          v-model="age"
          type="text"
          placeholder="Introduce la edad del dinosaurio" 
        /><br>
        <span>Weight</span><br>
        <input 
          v-model="weight"
          type="text"
          placeholder="Introduce el peso del dinosaurio" 
        /><br>

        <span>Gender</span><br>
        <select required name="gender" id="gender" v-model="gender">
          <option value=1>Male</option>
          <option value=2>Female</option>
        </select>

        <span>Dangerousness</span><br>
        <select required name="dangerousness" id="dangerousness" v-model="dangerousness">
          <option value=1>Peaceful</option>
          <option value=2>Aggresive</option>
        </select>

        <input 
          class="submit" 
          type="submit" 
          value="Submit"
        >

      </form>
      <div v-if="formSubmitted">
        <h3>Form Submitted</h3>
        <p>Name: {{ name }}</p>
        <p>Gender: {{ gender }}</p>
        <small>Click on run to launch the app again.</small>
      </div>

    </div>
  </template>

  <script>
import axios from 'axios';

    export default {
      data() {
        return {
          name: "",
          specie_id: 0,
          gender: 0,
          age: 0,
          weight: 0,
          dangerousness: 0,
          enclosure_id: 1,
        };
      },
      methods: {
        submitForm: function () {
          axios.post(
            "http://localhost:8000/dinosaur/create",
            {name: this.name,
            specie_id: this.specie_id,
            age: this.age,
            weight: this.weight,
            gender: this.gender,
            dangerousness: this.dangerousness,
            enclosure_id: this.enclosure_id
          }).then((response) => {
            this.response = JSON.stringify(response, null, 2);
            console.log(response);
          });
        }
      },
    };
  </script>
  <style>

  </style>