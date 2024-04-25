import { createApp }                      from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App                                from './App.vue'
import LandPage                           from './pages/LandPage.vue'
import DashboardView                      from './pages/DashboardView.vue'
import LoginApp                           from './pages/Login.vue'
import SignInApp                          from './pages/SignIn.vue'
import CreateQuiz                         from './pages/CreateQuiz.vue'
import DoQuiz                             from './pages/DoQuiz.vue'
import NotFound                           from './pages/[...all].vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

const routes = [
    { path: '/', component: LandPage, name: 'landPage' },
    { path: '/quiz/view', children: [
        { path: '/dashboard', component: DashboardView, name: 'dashboard'  },
        { path: '/create',    component: CreateQuiz,    name: 'createQuiz' },
        { path: '/do/new',    component: DoQuiz,        name: 'doQuiz'     },
        { path: '/not/found', component: NotFound,      name: 'notFound'   },
        { path: '/:pathMatch(.*)*',      redirect: '/not/found'            },
        { path: '/accounts', children: [
            { path: '/login',  component: LoginApp,  name: 'login'  },
            { path: '/signin', component: SignInApp, name: 'signin' },
        ] },
    ]},
]
const router = createRouter({ history : createWebHistory(), routes })

createApp(App).use(router).mount('#app')