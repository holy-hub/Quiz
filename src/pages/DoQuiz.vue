<template>
    <header class="masthead text-center text-white">
        <div class="masthead-content">
            <div class="container px-5">
                <MakeQuiz />
            </div>
        </div>
        <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
</template>

<script>
import MakeQuiz from '@/views/MakeQuiz.vue'

export default {
    name: 'DoQuiz',
    components: { MakeQuiz, },
}
</script>