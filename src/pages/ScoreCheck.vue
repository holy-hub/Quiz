<template>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container px-5">
            <a class="navbar-brand" href="/">{{ head }}</a>
            <router-link class="navbar-brand ms-auto" :to="{ name: 'doQuiz' }">Refaire un quiz</router-link>
        </div>
    </nav>
    <header class="masthead text-center text-white">
        <div class="masthead-content">
            <div class="container px-5 rounded" style="background: fff4;">
                <ScoreView />
            </div>
        </div>
        <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
</template>

<script>
import '@/assets/style/css/styles.css';
import '@/assets/style/js/scripts.js';
import ScoreView from '@/views/ScoreView.vue'

export default {
    name: 'ScoreCheck',
    components: { ScoreView, },
    props: { head: String, },
}
</script>