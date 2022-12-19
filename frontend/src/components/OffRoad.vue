<template>
  <table>
    <tr>
      <th>Id</th>
      <th>On Route</th>
      <th>N.º visitors</th>
      <th>Security system</th>
      <th>Delete</th>
    </tr>
    <tr v-for="item in off_roads" :key="item">
      <td>{{ item.id }}</td>
      <td>{{ item.on_route }}</td>
      <td>{{ item.n_visitors }}</td>
      <td>{{ item.security_system }}</td>
      <td align="center"><q-btn round color="red" v-on:click="deleteOffRoad(item.id)" icon="delete_outline" /></td>
    </tr>
  </table>
  <hr>
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
          off_roads: [],

          on_route: false,
          n_visitors: 0,
          security_system: false,
          off_roads: []
        };
      },
      methods: {
        async getOffRoads () {
          const response = await axios.get('http://localhost:8000/offroad/get_all')
          this.off_roads = response.data
        },
        deleteOffRoad(id) {
          axios.get("http://localhost:8000/offroad/delete/"+id)
          setTimeout(() => this.getOffRoads(), 500);
        },
        submitForm: function () {
          axios.post(
            "http://localhost:8000/offroad/create",
            {on_route: this.on_route,
            n_visitors: this.n_visitors,
            security_system: this.security_system
          }).then((response) => {
            this.response = JSON.stringify(response);
          });
          setTimeout(() => this.getOffRoads(), 500);
        }},
        created () {
          this.getOffRoads()
        }
      };
  </script>