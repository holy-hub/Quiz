<template>
  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container px-5">
      <a class="navbar-brand" href="/">{{ head }}</a>
      <router-link class="navbar-brand ms-auto" :to="{ name: 'listQuiz' }">Liste des QUIZ</router-link>
    </div>
  </nav>
  <header class="masthead text-center text-white">
    <div class="masthead-content">
      <div class="container py-3" style="background: #fff3">
        <HistoryView />
      </div>
    </div>
    <div class="bg-circle-1 bg-circle"></div>
    <div class="bg-circle-2 bg-circle"></div>
    <div class="bg-circle-3 bg-circle"></div>
    <div class="bg-circle-4 bg-circle"></div>
  </header>
</template>

<script>
import HistoryView from '@/views/HistoryView.vue'

export default {
  name: 'HistoryMatch',
  components: { HistoryView },
  props: { head: String },
  data () {
    return {
      quizzes: []
    }
  },
}
</script>
