<template>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container px-5">
            <a class="navbar-brand" href="/">{{ head }}</a>
            <router-link class="navbar-brand ms-auto" :to="{ name: 'login' }">Connexion</router-link>
        </div>
    </nav>
    <header class="masthead text-center text-white">
        <div class="masthead-content">
            <div class="container px-5">
                <h1 class="masthead-heading mb-0">Welcome to Our Quiz App</h1>
                <h2 class="masthead-subheading mb-0">Vivez une experience inouie avec nous</h2>
                <router-link class="btn btn-primary btn-xl rounded-pill mt-5" :to="{ name: 'doQuiz' }">Commencer un Quiz</router-link>
            </div>
        </div>
        <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
    <LandView />
</template>

<script>
import '@/assets/style/css/styles.css';
import '@/assets/style/js/scripts.js';
import LandView from '@/views/LandPage.vue'

export default {
    name: 'LandPage',
    components: { LandView, },
    data() { return{} },
    props: { head: String, },
}
</script>