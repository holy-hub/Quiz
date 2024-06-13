<template>
    <form method="POST" @submit.prevent="createQuiz">
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="email" v-model="question" class="form-control" placeholder="1 + 1 ?"
                    required /><label>Question</label>
            </div>
        </div>

        <div class="row">
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition1" value="{{ proposition1 }}" placeholder="11"
                            class="form-control" required /><label>Proposition 1</label>
                    </div>
                </div>
            </div>
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition2" value="{{ proposition2 }}" placeholder="7"
                            class="form-control" required /><label>Proposition 2</label>
                    </div>
                </div>
            </div>
            <div class="col mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <input type="text" v-model="proposition3" value="{{ proposition3 }}" placeholder="2"
                            class="form-control" required /><label>Proposition 3</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-group mb-4">
            <div class="form-floating">
                <select class="form-select text-center" v-model="reponse">
                    <option value="" disabled> Reponse </option>
                    <hr>
                    <option v-if="proposition1" value="{{ proposition1 }}">{{ proposition1 }}</option>
                    <hr v-if="proposition2 && proposition1">
                    <option v-if="proposition2" value="{{ proposition2 }}">{{ proposition2 }}</option>
                    <hr v-if="proposition3 && proposition2">
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
                            <option value="facile">FACILE</option>
                            <hr>
                            <option value="moy">MOYEN</option>
                            <hr>
                            <option value="diff">DIFFICILE</option>
                        </select>
                        <label>-- Choisir le Niveau --</label>
                    </div>
                </div>
            </div>
            <div class="col-md-6 mb-4">
                <div class="form-group">
                    <div class="form-floating">
                        <label>Categorie du Quiz (Economie)</label>
                        <input type="text" v-model="category" list="browse" placeholder="" class="form-control"
                            required />
                        <datalist id="browse">
                            <option :v-for="category in categories" value="{{ category }}">{{ category }}</option>
                        </datalist>
                    </div>
                </div>
            </div>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz</button>
    </form>
    <button @click="createQuizAndQuit()" class="btn btn-primary btn-block mb-4"> Creer un nouveau Quiz et
        quitter</button>
</template>

<script>
import axios from 'axios';

export default {
    name: 'createQuizView',
    data() {
        return { score: '', errorMessage: '', question: '', proposition1: '', proposition2: '', proposition3: '', reponse: '', niveau: '', categorie: '', };
    },
    created() {
        this.fetchCategories();
    },
    methods: {
        fetchCategories() {
            axios.get('api/categories/')
                .then(response => {
                    this.categories = response.data.map(cat => cat.name);
                })
                .catch(error => {
                    console.error('Error fetching categories:', error);
                });
        },
        createQuiz() {
            const data = {
                question: this.question,
                propositions: {
                    proposition1: this.proposition1,
                    proposition2: this.proposition2,
                    proposition3: this.proposition3,
                },
                reponse: this.reponse,
                niveau: this.niveau,
                category: this.category,
            };

            axios.post('api/quiz/', data)
                .then(response => {
                    console.log('Quiz created:', response.data);
                })
                .catch(error => { console.error('Error creating quiz:', error); });
        },
        createQuizAndQuit() {
            this.createQuiz(); this.$router.push('/dashboard')
        },
    },
}
</script>