<template>
    <form method="post" @submit.prevent="createQuiz">
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

        <button type="submit" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz</button>
    </form>
    <button @click="createQuizAndQuit()" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz et quitter</button>
</template>

<script>
import store from '@/store/storeCreation.js'

export default {
    name: 'createQuizView',
    data() {
        return { quiz: { question: '', propositions: { proposition1: '', proposition2: '', proposition3: '' }, reponse: '', niveau: '', categorie: '', }, };
    },
    methods: {
        createQuiz() { this.quiz.question && this.quiz.reponse && this.quiz.propositions.proposition1 && this.quiz.propositions.proposition2 && this.quiz.propositions.proposition3 && this.quiz.niveau && this.quiz.categorie ? store.dispatch('createQuiz', this.quiz) : this.$router.push('/create'); },
        createQuizAndQuit() {
            if (this.quiz.question && this.quiz.reponse && this.quiz.propositions.proposition1 && this.quiz.propositions.proposition2 && this.quiz.propositions.proposition3 && this.quiz.niveau && this.quiz.categorie) { store.dispatch('createQuiz', this.quiz); this.$router.push('/dashboard') } else { this.$router.push('/create'); }
        },
    },
}
</script><template>
    <form method="post" @submit.prevent="createQuiz">
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="text" v-model="theme" class="form-control" placeholder="Mathematique" required /><label>Question</label>
            </div>
        </div>
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="text" v-model="question" class="form-control" placeholder="1 + 1 ?" required /><label>Question</label>
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

        <button type="submit" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz </button>
    </form>
</template>

<script>
export default {
    name: 'createQuizView',
    data() {
        return { theme: '', question: '', proposition1: '', proposition2: '', proposition3: '', reponse: '', };
    },
    methods: {
        createQuiz() {
            this.theme && this.question && this.reponse && this.proposition1 && this.proposition2 && this.proposition3 ? this.$router.push('/quiz/view/dashboard') : this.$router.push('/quiz/view/create');
        }
    },
}
</script>