<template>

    <ul id="off_road">
      <li v-for="offroad in off_roads" :key="offroad">
        {{ offroad.on_route }} | {{ offroad.n_visitors }}
      </li>
    </ul>

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
          min="1"
          max="5"
          
        /><br>
        <span>Security System</span><br>
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
          security_system: false,
          off_roads: []
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
        },
        async getOffRoads () {
        const response = await axios.get('http://localhost:8000/offroad/get_all')
        this.off_roads = response.data
        console.log(this.off_roads)
        }
      },
      created () {
        this.getOffRoads()
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