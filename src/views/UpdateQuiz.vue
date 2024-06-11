<template>
    <form method="post" @submit.prevent="updateQuiz" ::key="quiz.id">
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="email" v-model="question" class="form-control" placeholder="1 + 1 ?" required /><label>Question</label>
            </div>
        </div>

        <div class="row">
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition1" value="{{ proposition1 }}" placeholder="11" class="form-control" required /><label>Proposition 1</label>
                    </div>
                </div>
            </div>
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition2" value="{{ proposition2 }}" placeholder="7" class="form-control" required /><label>Proposition 2</label>
                    </div>
                </div>
            </div>
            <div class="col mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition3" value="{{ proposition3 }}" placeholder="2" class="form-control" required /><label>Proposition 3</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-group mb-4">
            <div class="form-floating">
                <select class="form-select text-center" v-model="reponse">
                    <option value="" disabled> Reponse </option><hr>
                    <option v-if="proposition1" value="{{ proposition1 }}">{{ proposition1 }}</option><hr v-if="proposition2 && proposition1">
                    <option v-if="proposition2" value="{{ proposition2 }}">{{ proposition2 }}</option><hr v-if="proposition3 && proposition2">
                    <option v-if="proposition3" value="{{ proposition3 }}">{{ proposition3 }}</option>
                </select>
                <label>-- Choisir la response de la Question --</label>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mb-4">
                <div class="form-group mb-4">
                    <div class="form-floating">
                        <select class="form-select text-center" v-model="niveau">
                            <option value="facile">FACILE</option><hr>
                            <option value="moyen">MOYEN</option><hr>
                            <option value="difficile">DIFFICILE</option>
                        </select>
                        <label>-- Choisir la Niveau --</label>
                    </div>
                </div>
            </div>
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="categorie" value="{{ categorie }}" placeholder="" class="form-control" required /><label>Categorie du Quiz (Economie)</label>
                    </div>
                </div>
            </div>
        </div>

        <div class="d-flex justify-content-arround">
            <button type="submit" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz </button>
            <button @click="deleteQuiz(quiz.id)" class="btn btn-danger btn-block mb-4"> Supprimer ce quiz </button>
        </div>
    </form>
</template>

<script>
import store from '@/store/storeCreation.js'

export default {
    name: 'UpdateQuizView',
    computed: { quizDisplay() { return store.state.quizzes }, },
    data() {
        return { quiz: { question: 'quizDisplay.question', propositions: { proposition1: 'quizDisplay.propositions.proposition1', proposition2: 'quizDisplay.propositions.proposition2', proposition3: 'quizDisplay.propositions.proposition3' }, reponse: 'quizDisplay.reponse', niveau: 'quizDisplay.niveau', categorie: 'quizDisplay.categorie', }, };
    },
    methods: {
        updateQuiz(id) {
            if (this.quiz.question && this.quiz.reponse && this.quiz.propositions.proposition1 && this.quiz.propositions.proposition2 && this.quiz.propositions.proposition3 && this.quiz.niveau && this.quiz.categorie) { store.dispatch('updateQuiz', { id, quiz: this.quiz }) }
        },
        deleteQuiz(id) { store.dispatch('deleteQuiz', id) },
    },
    
}
</script>