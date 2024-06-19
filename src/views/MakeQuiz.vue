<template>
  <div class="container-fluid bg-white">
    <div class="row">
      <div
        class="bg-light rounded col-md-6"
        v-for="quiz in quizzes"
        :key="quiz.id"
        @click="startQuiz(quiz)"
      >
        {{ quiz.category }}
      </div>
      <div class="col-md-6 justify-content-center" v-if="currentQuiz">
        <div class="card">
          <div class="card-header">{{ currentQuiz.question }}</div>
          <div class="card-body">
            <div class="form-check">
              <input
                type="radio"
                class="form-check-input"
                v-model="response"
                value="{{ currentQuiz.proposition }}"
              />Option 1
              <label class="form-check-label"></label>
            </div>
            <div class="form-check">
              <input
                type="radio"
                class="form-check-input"
                v-model="response"
                value="{{ currentQuiz.proposition1 }}"
              />Option 1
              <label class="form-check-label"></label>
            </div>
            <div class="form-check">
              <input
                type="radio"
                class="form-check-input"
                v-model="response"
                value="{{ currentQuiz.proposition2 }}"
              />Option 1
              <label class="form-check-label"></label>
            </div>
          </div>
          <div class="card-footer">
            <div class="alert alert-success" v-if="answers(currentQuiz)">Vous avez trouve la bonne reponse</div>
            <div class="alert alert-danger" v-else>Vous avez trouve la mauvaise reponse</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'MakeQuiz',
  data () {
    return { quizzes: [], score: 0, response: '', errorMessage: '', currentQuiz: '', }
  },
  created () {
    this.fetchQuizzes()
  },
  methods: {
    fetchQuizzes () {
      api
        .get('/api/quizzes/')
        .then(response => {
          this.quizzes = response.data
        })
        .catch(error => {
          console.error('Error fetching quizzes:', error)
          this.errorMessage = 'Error fetching quizzes'
        })
    },
    startQuiz(quiz) {
      this.currentQuiz = quiz
    },
    answers (quiz) {
      if (this.response === quiz.response) {
        this.score += 1
        return true
      }
    },
  }
}
</script>
