<template>
  <div class="container bg-white">
    <div class="py-5">
      <table
        class="table table-bordered table-striped table-hover text-wrap px-5"
      >
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
          <tr v-for="score in scores" :key="score.id">
            <td></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'HistoryView',
  data () {
    return {
      scores: [], errorMessage: '',
    }
  },
  created () {
    this.fetchScore()
  },
  methods: {
    fetchScore () {
      api.get('/api/scores/').then(response => (this.scores = response.data))
        .catch(error => { console.log('error fethcing Score:' + error); this.errorMessage = 'Error fetching Score.' });
    },
  }
}
</script>
