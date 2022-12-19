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
      <th>Delete</th>
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
      <td align="center"><q-btn round color="red" v-on:click="deleteDinosaur(item.id)" icon="delete_outline" /></td>
    </tr>
  </table>
  <hr>
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

export default {
  data () {
    return {
      dinosaurs: [],

      name: "",
      specie: {},
      enclosure: {},
      gender: "",
      age: 0,
      weight: 0,
      dangerousness: "",
      enclosures: [],
      species: [],
    }
  },
  methods: {
    async getDinosaurs () {
      const response = await axios.get('http://localhost:8000/dinosaur/get_all')
      this.dinosaurs = response.data
      console.log(this.dinosaurs)
    },
    deleteDinosaur(id) {
        axios.get("http://localhost:8000/dinosaur/delete/"+id)
        this.getDinosaurs()
    },
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
      this.getDinosaurs()
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
    this.getDinosaurs()
    this.getSpecies()
    this.getEnclosures()
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
