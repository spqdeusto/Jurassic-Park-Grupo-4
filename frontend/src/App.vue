<template>
  <q-layout view="hHh LpR fFf" class="JPARK__bg">
    <q-header class="bg-transparent" reveal height-hint="60">
      <q-toolbar class="JPARK__toolbar text-grey-6">
        <q-btn
          flat
          dense
          round
          @click="toggleLeftDrawer"
          aria-label="Menu"
          icon="menu"
          class="q-mr-sm"
        />

        <div class="q-pr-lg" v-if="$q.screen.gt.xs">
          <img class="JPARK__logo" src="/img/brand/logo.png">
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      class="JPARK_leftside bg-transparent text-grey-7"
      :width="330"
    >
      <q-list>
        <q-item clickable class="JPARK__drawer-link JPARK__drawer--dinosaurs" @click="showDinosaurs">
          <q-item-section class="dinosaurs-text">
            <q-item-label>Dinosaurs</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="JPARK__drawer-link JPARK__drawer-link--species" @click="showSpecies">
          <q-item-section class="species-text">
            <q-item-label>Species</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="JPARK__drawer-link JPARK__drawer-link--enclosures" @click="showEnclosures">
          <q-item-section class="enclosures-text">
            <q-item-label>Enclosures</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="JPARK__drawer-link JPARK__drawer-link--offroads" @click="showOffRoads">
          <q-item-section class="offroads-text">
            <q-item-label>OffRoads</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />

      <q-page expand position="top">
        <q-toolbar class="JPARK__sticky q-px-xl">
          <q-space />
              <q-badge v-if="alarm=='normal'" color="green"><q-icon name="check_circle" />&nbsp;NORMAL</q-badge>
              <q-badge v-if="alarm=='low'" color="yellow" text-color="brown"><q-icon name="warning" />&nbsp;LOW ALERT</q-badge>    
              <q-badge v-if="alarm=='average'" color="orange"><q-icon name="warning" />&nbsp;AVERAGE ALERT</q-badge>    
              <q-badge v-if="alarm=='maximum'" color="red"><q-icon name="warning" />&nbsp;MAXIMUM ALERT</q-badge> &nbsp;
              <marquee>

              Welcome to Jurassic Park administration panel.
            </marquee>
        </q-toolbar>

        <q-card class="my-card" v-show="dinosaurs">
          <q-card-section>
            <Dinosaur ref="foo"></Dinosaur>
          </q-card-section>
        </q-card>

        <q-card class="my-card" v-show="species">
          <q-card-section>
            <Specie></Specie>
          </q-card-section>
        </q-card>

        <q-card class="my-card" v-show="enclosures">
          <q-card-section>
            <Enclosure></Enclosure>
          </q-card-section>
        </q-card>

        <q-card class="my-card" v-show="offRoads">
          <q-card-section>
            <OffRoad ref="fooTwo"></OffRoad>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<script>
import { ref } from 'vue';
import axios from 'axios';

import Dinosaur from './components/Dinosaur.vue';
import Specie from './components/Specie.vue';
import Enclosure from './components/Enclosure.vue';
import OffRoad from './components/OffRoad.vue';

export default {
    name: "JurassicParkLayout",
    data(){
        return {
          alarm:"",
          dinosaurs:true,
          species:false,
          enclosures:false,
          offRoads:false
        }
    },
    setup() {
      return {
        leftDrawerOpen : ref(false),
        search : ref(""),
        storage : ref(0.26),
        toggleLeftDrawer() {
            leftDrawerOpen.value = !leftDrawerOpen.value;
        }
      }
    },
    methods: {
        async getAlarm () {
          const response = await axios.get('http://localhost:8000/alarm/get')
          this.alarm = response.data[0]['status']
        },
        showDinosaurs: function() {
          this.hideAll()
          this.dinosaurs=true
          this.$refs.foo.updateForm()
        },
        showSpecies: function() {
          this.hideAll()
          this.species=true
        },
        showEnclosures: function() {
          this.hideAll()
          this.enclosures=true
        },
        showOffRoads: function() {
          this.hideAll()
          this.offRoads=true
          this.$refs.fooTwo.getOffRoads()
        },
        hideAll: function() {
          this.dinosaurs=false
          this.species=false
          this.enclosures=false
          this.offRoads=false
        }
    },
    components: {
      Dinosaur, 
      Specie, 
      Enclosure,
      OffRoad 
    },
    created() {
      this.getAlarm()
    },
    mounted() {
      setInterval(this.getAlarm,2500);
    }
}
</script>

<style lang="sass">
.JPARK
  font-family: 'Montserrat', sans-serif

  &__bg
    background: url(img/brand/bg.jpg)
    background-size: cover

  &__toolbar
    background: rgb(64 45 39 / 60%)
    height: 120px

  &__logo
    width: 183px

  &__toolbar-input-container
    min-width: 100px
    width: 55%

  &__toolbar-input-btn
    border-radius: 0
    max-width: 60px
    width: 100%

  &__leftside
    background: rgb(64 45 39 / 38%)

  &__drawer-item
    padding: 6px 12px 6px 23px
  
  &__drawer-link
      background: url(img/brand/menu_tab.png)
      padding-left: 80px
      color: white
      font-size: 22px
      font-weight: 700
      height: 70px
      margin: 15px

  &__sticky
    min-height: 49px
    color: #402d27
    font-size: 16px
    border: 6px solid #402d27
    margin: 15px
    font-weight: bold
    border-radius: 5px
    margin-right: 15px
    padding-right:200px
    padding: 0px 15px

  &__sticky-help
    border: 1px solid #ccc
    padding-left: 8px
    padding-right: 8px

  &__sticky-settings
    padding-left: 17px
    padding-right: 17px

    border: 1px solid #ccc

.q-page-container 
  padding-right: 35px
  padding-bottom: 30px

.q-drawer
  background: transparent!important

.q-badge
  padding: 5px 10px
  font-size: 16px
  font-weight: bold!important

.q-card
  background: rgb(64 45 39 / 67%)
  color: #dad8d6
  width: 100%
  margin: 0px 16px
  font-size: 1.2em

table
  width: 100%
  background: rgba(0 0 0 / 25%)
  border: 6px solid rgb(255 255 255 / 10%)

td
  border-top: 3px solid rgba(255, 255, 255, 0.08)
  padding: 0px 15px

th
  background: #402d27

hr
  border: 3px solid #000000
  background: #fe0000 !important
  box-shadow: 0px 0px 0px 3px #ffff01
  color: #fff
  font-weight: bold
  border-radius: 1px
  margin: 20px 0px
  height: 3px

button,input,select
  background: #291a15
  color: #beb0a1
  border-radius: 15px
  border: none
  padding: 5px 18px
  margin: 10px 0px

.submit
  border: 3px solid #000000
  background: #fe0000!important
  box-shadow: 0px 0px 0px 3px #ffff01
  color: #fff
  font-weight: bold
  border-radius: 1px
</style>