<template>
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