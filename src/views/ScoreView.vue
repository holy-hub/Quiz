<template lang="en">
    <div class="bg-light rounded">
        
        <div class="card">
            <div class="card-header"><h2><b><u>CATEGORIE</u></b>: {{ scroe.categorie }}</h2></div>
            <div class="card-body">
                <div class="alert alert-info"><h2><b><u>SCORE</u></b>: {{ scroe.score }}</h2></div>
            </div>
            <div class="card-footer"><h3><b><u>NIVEAU</u></b>: {{ score.niveau }}</h3></div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ScoreView',
    props: { idQuiz: { type: String, required: true }, },
    computed: {
        score() { return this.$store.state.score.find(item => item[0] === this.id); }
    },
}
</script>