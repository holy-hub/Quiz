<template>
    <div class="container bg-white">
        <div class="py-5">
            <table class="table table-bordered table-striped table-hover text-wrap px-5">
                <thead>
                    <tr>
                        <th>Question</th>
                        <th>Propositions</th>
                        <th>Reponse</th>
                    </tr>
                </thead>
                <tfoot>
                    <tr>
                        <th>Question</th>
                        <th>Propositions</th>
                        <th>Reponse</th>
                    </tr>
                </tfoot>
                <tbody>
                    <tr>
                        <td class="alert alert-info" v-if="errorMessage">{{ errorMessage }}</td>
                    </tr>
                    <div v-if="quizzes.length > 0">
                        <tr v-for="quiz in quizzes" :key="quiz.id">
                            <td class="pt-5"><router-link class="nav-link" :to="{ name: 'updateQuiz', params: { idQuiz: quiz.id } }">{{ quiz.question }}</router-link></td>
                            <td>
                                <div class="card">
                                    <div class="card-header">{{ quiz.niveau }}</div>
                                    <div class="card-body">
                                        <ul class="list-group">
                                            <li class="list-group-item list-group-item-action" v-for="prop in quiz.propositions" :key="prop.id">{{ prop.text }}</li>
                                        </ul>
                                    </div>
                                    <div class="card-footer">{{ quiz.categorie }}</div>
                                </div>
                            </td>
                            <td class="pt-5">{{ quiz.reponse }}</td>
                        </tr>
                    </div>
                    <tr v-else>
                        <td>Aucun quiz enregistré...</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import api from '@/api'

export default {
    name: 'DisplayQuiz',
    data() {
        return { quizzes: [], errorMessage: '', }
    },
    create() {
        this.fetchQuiz();
    },
    methods: {
        fecthquiz() {
            api.get('/api/quizzes/')
                .then(response => {
                    this.quizzes = response.data.map(quiz => quiz.question);
                })
                .catch(error => {
                    console.error('Error fetching quizzes:', error);
                    this.errorMessage = 'Error fetching quizzes';
                });
        },
    },
}
</script>