<template>
    <div>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
        <span>On Route</span><br>
        <input 
          v-model="on_route"
          type="checkbox"
        /><br>

        <span>Visitors</span><br>
        <input 
          v-model="n_visitors"
          type="number"
          placeholder="Introduce los visitantes" 
          min="0"
          max="20"
          
        /><br>
        <span>Securuity System</span><br>
        <input 
          v-model="security_system"
          type="checkbox"
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
          on_route: false,
          n_visitors: 0,
          security_system: false
        };
      },
      methods: {
        submitForm: function () {
          axios.post(
            "http://localhost:8000/offroad/create",
            {on_route: this.on_route,
            n_visitors: this.n_visitors,
            security_system: this.security_system
          }).then((response) => {
            this.response = JSON.stringify(response);
            console.log(response);
          });
        }}
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