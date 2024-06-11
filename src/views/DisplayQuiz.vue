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
                    <tr v-for="quiz in quizzes" :key="quiz.id">
                        <td class="pt-5"><router-link class="navbar-brand" :to="{ name: 'updateQuiz', params: { idQuiz: quiz.id } }">question</router-link></td>
                        <td>
                            <div class="card">
                                <div class="card-header">niveau</div>
                                <div class="card-body">
                                    <ul class="list-group">
                                        <li class="list-group-item list-group-item-action">Proposition 1</li>
                                        <li class="list-group-item list-group-item-action">Proposition 2</li>
                                        <li class="list-group-item list-group-item-action">Proposition 3</li>
                                    </ul>
                                </div>
                                <div class="card-footer">categorie</div>
                            </div>
                        </td>
                        <td class="pt-5">reponse</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'DisplayQuiz',
    computed: { ...mapState(['quizzes']), },
}
</script>