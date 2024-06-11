import { createStore } from 'vuex'

const store = createStore({
    state: { quizzes: [], categories: [], niveau: [], score: [[]], },
    mutations: {
        addQuiz(state, quiz) { state.quizzes.push(quiz); },
        addScore(state, payload) { state.score.push([payload.categories, payload.score, payload.niveau]); },
        updateQuiz(state, { id, quiz }) {
            const index = state.quizzes.findIndex(q => q.id === id);
            if (index !== -1) { state.quizzes.splice(index, 1, quiz) }
        },
        deleteQuiz(state, id) {
            const index = state.quizzes.findIndex(q => q.id === id);
            if (index !== -1) { state.quizzes.splice(index, 1) }
        },
        getCategories(state) { state.categories = [...new Set(state.quizzes.map(quiz => quiz.categorie))] },
        getQuizzesByCategory(state, category) { state.quizzes = state.quizzes.filter(quiz => quiz.categorie === category) },
        getLevel(state) { state.niveau = [...new Set(state.quizzes.map(quiz => quiz.niveau))] },
        getQuizzesByLevel(state, niveau) { state.quizzes = state.quizzes.filter(quiz => quiz.niveau === niveau) },
    },
    actions: {
        createQuiz({ commit }, quiz) { commit('addQuiz', quiz) },
        addScore({ commit }, categories, score, niveau) { commit('addScore', { categories, score, niveau }) },
        updateQuiz({ commit }, { id, quiz }) {
            commit('updateQuiz', { id, quiz })
            this.$router.push('/listQuiz') },
        deleteQuiz({ commit }, id) {
            commit('deleteQuiz', id)
            this.$router.push('/listQuiz') },
    }
});

export default store;