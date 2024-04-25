<template>
    <header class="masthead text-center text-white">
      <div class="masthead-content">
        <div class="container px-5">
          <h1 class="masthead-heading mb-0">| <span class="text-warning">{{ error }}</span> {{ head }}</h1>
          <h2 class="masthead-subheading mb-0">Error lors de cette page que vous recherchez, veuillez retrousser votre chemin vers l'accueil.</h2>
          <router-link class="btn btn-primary btn-xl rounded-pill mt-5" :to="{ name: 'Home' }">Accueil</router-link>
        </div>
      </div>
      <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
  </template>
  
  <script>
  import '@/assets/style/css/styles.css'
  import '@/assets/style/js/scripts.js'
  
  export default {
      name: 'NotFoundComponent',
      props: { head: String, error: String, },
  }
  </script>
  
  <style>
  </style>