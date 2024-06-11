import { createApp }                      from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App                                from './App.vue'
import LandPage                           from './pages/LandPage.vue'
import DashboardView                      from './pages/DashboardView.vue'
import LoginApp                           from './pages/Login.vue'
import SignInApp                          from './pages/SignIn.vue'
import CreateQuiz                         from './pages/CreateQuiz.vue'
import DoQuiz                             from './pages/DoQuiz.vue'
import ListQuiz                           from './pages/ListQuiz.vue'
import UpdateQuiz                         from './pages/UpdateQuiz.vue'
import ScoreCheck                         from './pages/ScoreCheck.vue'
import MenuQuiz                           from './pages/MenuQuiz.vue'
import store                              from './store/storeCreation.js'
import $                                  from 'jquery'
import 'bootstrap/dist/js/bootstrap.min.js';
import 'bootstrap/dist/css/bootstrap.min.css';

const routes = [
    { path: '/', component: LandPage, name: 'landPage' },
    { path: '/quiz/view', children: [
        { path: '/admin', children: [
            { path: '/:id/dashboard',  component: DashboardView, name: 'dashboard'  },
            { path: '/create',         component: CreateQuiz,    name: 'createQuiz' },
            { path: '/update/:idQuiz', component: UpdateQuiz,    name: 'updateQuiz' },
            { path: '/all/creation',   component: ListQuiz,      name: 'listQuiz'   },
        ] },
        { path: '/user', children: [
            { path: '/do/new',    component: DoQuiz,     name: 'doQuiz' },
            { path: '/:idQuiz/score', component: ScoreCheck, name: 'score'  },
            { path: '/menu',      component: MenuQuiz,   name: 'menu'   },
        ] },
        { path: '/accounts', children: [
            { path: '/login',  component: LoginApp,  name: 'login'  },
            { path: '/signin', component: SignInApp, name: 'signin' },
        ] },
    ] },
    { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({ history : createWebHistory(), routes })

createApp(App).config.globalProperties.$$ = $
createApp(App).use(router).use(store).mount('#app')