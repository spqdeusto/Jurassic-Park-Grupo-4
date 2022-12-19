<template>
  <table>
    <tr>
      <th>Id</th>
      <th>Status</th>
      <th>Name</th>
      <th>Delete</th>
    </tr>
    <tr v-for="item in enclosures" :key="item">
      <td>{{ item.id }}</td>
      <td>{{ item.status }}</td>
      <td>{{ item.name }}</td>
      <td align="center"><q-btn round color="red" v-on:click="deleteEnclosure(item.id)" icon="delete_outline" /></td>
    </tr>
  </table>
  <hr>
  <div>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
        <span>Name</span><br>
        <input 
          v-model="name"
          type="text"
          placeholder="Introduce a name"
        /><br>

        <span>Electric system activated</span><br>
        <input 
          v-model="status"
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
  name: 'Home',
  data () {
    return {
      enclosures: [],

      name: "",
      status: false
    }
  },
  methods: {
    async getEnclosures () {
      const response = await axios.get('http://localhost:8000/enclosure/get_all')
      this.enclosures = response.data
    },
    deleteEnclosure(id) {
        axios.get("http://localhost:8000/enclosure/delete/"+id)
        setTimeout(() => this.getEnclosures(), 500);
    },
    submitForm: function () {
      axios.post(
        "http://localhost:8000/enclosure/create",
        {name: this.name,
        status: this.status
      }).then((response) => {
        this.response = JSON.stringify(response);
        console.log(response);
      });
      setTimeout(() => this.getEnclosures(), 500);
    }
  },
  created () {
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
