<template lang="en">
    <div class="col-lg-6 mb-5 mb-lg-0 position-relative" id="card2">
        <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
        <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>
        <div class="card bg-glass">
            <div class="card-body px-4 py-5 px-md-5">
                <ul class="list-group list-group-item-numbered">
                    <li class="list-group-item list-group-item-action" v-for="quiz in quizzes" :key="quiz.id">{{ quiz.question }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from 'vuex'
import $            from 'jquery'

export default {
    name: 'MenuView',
    computed: { ...mapState(['quizzes', ]) },
}

$('#card2').fadeIn("slow");
</script>