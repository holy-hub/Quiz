<template>
  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container px-5">
          <a class="navbar-brand" href="/">{{ head }}</a>
          <router-link class="navbar-brand ms-auto" :to="{ name: 'dashboard' }">DASHBOARD</router-link>
      </div>
  </nav>
  <header class="masthead text-center text-white">
        <div class="masthead-content">
            <div class="container py-3" style="background: #fff3">
                <DisplayQuiz />
            </div>
        </div>
        <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
</template>

<script>
import DisplayQuiz from '@/views/DisplayQuiz.vue'

export default {
    name: 'ListQuiz',
    components: { DisplayQuiz, },
    props: { head: String, }
}
</script>