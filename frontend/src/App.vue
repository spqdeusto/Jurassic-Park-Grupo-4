<template>
  <q-layout view="hHh LpR fFf" class="bg-brown-4">
    <q-header class="bg-brown-10 text-grey-9" reveal height-hint="60">
      <q-toolbar class="GPLAY__toolbar text-grey-6">
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
          <img class="GPLAY__logo" src="/img/brand/logo.png">
        </div>

        <q-space />

        <!--<div class="GPLAY__toolbar-input-container row no-wrap">
          <q-input dense outlined square v-model="search" placeholder="Search" class="bg-white col" />
          <q-btn class="GPLAY__toolbar-input-btn" color="primary" icon="search" unelevated />
        </div>-->

        <q-space />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      class="bg-brown-6 text-grey-7"
      :width="330"
    >
      <q-list>
        <q-item clickable class="GPLAY__drawer-link GPLAY__drawer--dinosaurs">
          <q-item-section class="dinosaurs-text">
            <q-item-label>Dinosaurs</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="GPLAY__drawer-link GPLAY__drawer-link--species">
          <q-item-section class="species-text">
            <q-item-label>Species</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="GPLAY__drawer-link GPLAY__drawer-link--enclosures">
          <q-item-section class="enclosures-text">
            <q-item-label>Enclosures</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="GPLAY__drawer-link GPLAY__drawer-link--offroads">
          <q-item-section class="offroads-text">
            <q-item-label>OffRoads</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable class="GPLAY__drawer-link GPLAY__drawer-link--alarm">
          <q-item-section class="alarm-text">
            <q-item-label>Alarm</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />

      <q-page-sticky expand position="top">
        <q-toolbar class="GPLAY__sticky bg-brown-8 q-px-xl">
          <q-space />
            <marquee>Bienvenido al panel de Jurassic Park. Esto se trata de una prueba.</marquee>
        </q-toolbar>
      </q-page-sticky>

      <q-page-container>
        hola
      </q-page-container>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from 'vue'
export default {
  name: 'JurassicParkLayout',
  setup () {
    const leftDrawerOpen = ref(false)
    const search = ref('')
    const storage = ref(0.26)
    function toggleLeftDrawer () {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }
    return {
      leftDrawerOpen,
      search,
      storage,
      toggleLeftDrawer
    }
  }
}
</script>

<style lang="sass">
.GPLAY
  font-family: 'Montserrat', sans-serif

  &__toolbar
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
    //border: 3px solid black
    //box-shadow: 0 0 0 4px #ffff01
    color: white
    font-size: 16px

  &__sticky-help
    border: 1px solid #ccc
    padding-left: 8px
    padding-right: 8px

  &__sticky-settings
    padding-left: 17px
    padding-right: 17px
    border: 1px solid #ccc
</style>