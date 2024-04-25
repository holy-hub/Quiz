<template>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container px-5">
            <a class="navbar-brand" href="/">{{ head }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span
                    class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><router-link class="nav-link" :to="{ name: 'signin' }">Inscription</router-link></li>
                </ul>
            </div>
        </div>
    </nav>

    <section class="background-radial-gradient overflow-hidden">
        <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
            <div class="row gx-lg-5 align-items-center mb-5">
                <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
                    <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218, 81%, 95%)">
                        Bienvenue cher(e) <br /><span style="color: hsl(218, 81%, 75%)">createur(trice) de culture . .
                            .</span>
                    </h1>
                    <p class="mb-4 opacity-70" style="color: hsl(218, 81%, 85%)">Il n'y a rien de plus enrichissant que
                        la quête du savoir. Explorez de nouveaux horizons, élargissez vos perspectives et nourrissez
                        votre esprit avec une offre inégalée pour vous cultiver.</p>
                </div>

                <LoginView />
            </div>
        </div>
    </section>
</template>

<script>
import LoginView from '@/views/Login.vue'

export default {
    name: 'LoginApp',
    props: { head: String, },
    components: { LoginView, },
    data() {
        return {};
    }, }
</script>

<style scoped>
.background-radial-gradient { background-color: hsl(218, 41%, 15%); background-image: radial-gradient(650px circle at 0% 0%, hsl(218, 41%, 35%) 15%, hsl(218, 41%, 30%) 35%, hsl(218, 41%, 20%) 75%, hsl(218, 41%, 19%) 80%, transparent 100%), radial-gradient(1250px circle at 100% 100%, hsl(218, 41%, 45%) 15%, hsl(218, 41%, 30%) 35%, hsl(218, 41%, 20%) 75%, hsl(218, 41%, 19%) 80%, transparent 100%); }
#radius-shape-1 { height: 220px; width: 220px; top: -60px; left: -130px; background: radial-gradient(#44006b, #ad1fff); overflow: hidden; }
#radius-shape-2 { border-radius: 38% 62% 63% 37% / 70% 33% 67% 30%; bottom: -60px; right: -110px; width: 300px; height: 300px; background: radial-gradient(#44006b, #ad1fff); overflow: hidden; }
.bg-glass { background-color: hsla(0, 0%, 100%, 0.9) !important; backdrop-filter: saturate(200%) blur(25px); }
</style>