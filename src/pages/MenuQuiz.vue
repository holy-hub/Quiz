<template>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container px-5">
            <a class="navbar-brand" href="/">{{ head }}</a>
            <router-link class="navbar-brand ms-auto" :to="{ name: 'dashboard' }">DASHBOARD</router-link>
        </div>
    </nav>

    <section class="background-radial-gradient overflow-hidden">
        <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
            <div class="row gx-lg-5 align-items-center mb-5">
                <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10; position: sticky;" id="card">
                    <ul class="list-group list-group-item-flush">
                        <li class="list-group-item list-group-item-action" v-for="category in categories" :value="category" :key="category" @click="getQuizzesByCategory(category)">{{ category }}</li>
                    </ul>
                </div>

                <MenuView />
            </div>
        </div>
    </section>
</template>

<script>
import MenuView     from '@/views/MenuView.vue'
import { mapState } from 'vuex'
import $ from 'jquery'

export default {
    name: 'MenuQuiz',
    props: { head: String, },
    components: { MenuView, },
    data() {
        return {};
    },
    computed: { ...mapState(['categories']), },
    created() { this.$store.commit('getCategories') },
    methods: {
        getQuizzesByCategory(category) { this.$store.commit('getQuizzesByCategory', category) },
    }
}

$('#card').hide().show(2000);
</script>

<style scoped>
.background-radial-gradient { background-color: hsl(218, 41%, 15%); background-image: radial-gradient(650px circle at 0% 0%, hsl(218, 41%, 35%) 15%, hsl(218, 41%, 30%) 35%, hsl(218, 41%, 20%) 75%, hsl(218, 41%, 19%) 80%, transparent 100%), radial-gradient(1250px circle at 100% 100%, hsl(218, 41%, 45%) 15%, hsl(218, 41%, 30%) 35%, hsl(218, 41%, 20%) 75%, hsl(218, 41%, 19%) 80%, transparent 100%); }
#radius-shape-1 { height: 220px; width: 220px; top: -60px; left: -130px; background: radial-gradient(#44006b, #ad1fff); overflow: hidden; }
#radius-shape-2 { border-radius: 38% 62% 63% 37% / 70% 33% 67% 30%; bottom: -60px; right: -110px; width: 300px; height: 300px; background: radial-gradient(#44006b, #ad1fff); overflow: hidden; }
.bg-glass { background-color: hsla(0, 0%, 100%, 0.9) !important; backdrop-filter: saturate(200%) blur(25px); }
</style>