<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <ul id="enclosures">
    <li v-for="enclosure in enclosures" :key="enclosure">
      {{ enclosure.name }} | {{ enclosure.status }}
    </li>
  </ul>

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
    submitForm: function () {
          axios.post(
            "http://localhost:8000/enclosure/create",
            {name: this.name,
            status: this.status
          }).then((response) => {
            this.response = JSON.stringify(response);
            console.log(response);
          });
        },
    async getEnclosures () {
      const response = await axios.get('http://localhost:8000/enclosure/get_all')
      this.enclosures = response.data
      console.log(this.enclosures)
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
