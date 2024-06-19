<template>
  <router-view head="QUIZ - APP" />
</template>

<script>
import $ from 'jquery'

$(document).ready(function() { $('#app').hide().fadeToggle('slow'); $('body').hide().fadeToggle('slow'); });
export default {
  name: 'App',
  components: { },
}
</script>

<style>
#app { font-family: Avenir, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-align: center; color: #2c3e50; scroll-behavior: smooth; transition: all 3s ease; }
</style>