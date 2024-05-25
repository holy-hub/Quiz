<template>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container px-5">
            <a class="navbar-brand" href="/">{{ head }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span
                    class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><router-link class="nav-link" :to="{ name: 'doQuiz' }">Commencer un Quiz</router-link></li>
                    <li class="nav-item"><router-link class="nav-link" :to="{ name: 'login' }">Connexion</router-link></li>
                </ul>
            </div>
        </div>
    </nav>
    <LandView msg="Welcome to Our Quiz App" subMsg="Vivez une experience inouie avec nous" />
</template>

<script>
// import '@/assets/style/css/styles.css'; // import '@/assets/style/js/scripts.js';
import LandView from '@/views/LandPage.vue'

export default {
    name: 'LandPage',
    components: { LandView, },
    props: { head: String, },
}
</script>