<template>
  <q-layout view="hHh LpR fFf" class="bg-grey-3">
    <q-header class="bg-grey-3 text-grey-9" reveal height-hint="60">
      <q-toolbar class="GPLAY__toolbar text-grey-6">
        <q-btn
          v-if="$q.platform.is.mobile || !leftDrawerOpen"
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

        <div class="GPLAY__toolbar-input-container row no-wrap">
          <q-input dense outlined square v-model="search" placeholder="Search" class="bg-white col" />
          <q-btn class="GPLAY__toolbar-input-btn" color="primary" icon="search" unelevated />
        </div>

        <q-space />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-grey-3 text-grey-7"
      :width="300"
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
        <q-toolbar class="GPLAY__sticky bg-white q-px-xl">
          <q-space />
          Esto es una prueba
        </q-toolbar>
      </q-page-sticky>
      Prueba
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from 'vue'
</script>

<style lang="sass">
.GPLAY

  &__toolbar
    background: #ffffff!important
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

  &__sticky
    min-height: 49px
    border-bottom: 1px solid rgba(0,0,0,0.12)
    background: #fe0000!important

  &__sticky-help
    border: 1px solid #ccc
    padding-left: 8px
    padding-right: 8px

  &__sticky-settings
    padding-left: 17px
    padding-right: 17px
    border: 1px solid #ccc

.q-item
      background: url(img/brand/menu_tab.png)
      padding-left: 80px
      color: white
      font-size: 20px
      font-weight: 700
      height: 70px
</style>