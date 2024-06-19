<template>
  <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
    <div
      id="radius-shape-1"
      class="position-absolute rounded-circle shadow-5-strong"
    ></div>
    <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>
    <div class="card bg-glass">
      <div class="card-body px-4 py-5 px-md-5">
        <form method="POST" @submit.prevent="login">
          <div class="my-4 text-center alert alert-danger" v-if="error">
            {{ error }}
          </div>
          <div class="form-group mb-4">
            <div class="form-floating">
              <input
                type="email"
                v-model="email"
                class="form-control"
                placeholder="Email"
              /><label>Email address</label>
            </div>
          </div>
          <div class="form-group mb-4">
            <div class="form-floating">
              <input
                type="password"
                v-model="password"
                class="form-control"
                placeholder="Password"
              /><label>password</label>
            </div>
          </div>

          <button type="submit" class="btn btn-primary btn-block mb-4">
            Se connecter
          </button>

          <div class="text-center">
            <p>ou se connecter avec:</p>
            <button type="button" class="btn btn-link btn-floating mx-1">
              <fa :icon="['fab', 'facebook-f']" />
            </button>
            <button type="button" class="btn btn-link btn-floating mx-1">
              <fa :icon="['fab', 'google']" />
            </button>
            <button type="button" class="btn btn-link btn-floating mx-1">
              <fa :icon="['fab', 'twitter']" />
            </button>
            <button type="button" class="btn btn-link btn-floating mx-1">
              <fa :icon="['fab', 'github']" />
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'LoginView',
  data () { return { email: '', password: '', error: '', } },
  methods: {
    login () {
      const data = { email: this.email, password: this.password }

      api
        .post('/accounts/api/login/', data)
        .then(response => {
          console.log('Quiz created: ', response.data)
          this.$router.push('/all/creation') })
        .catch(error => {
          console.error('Error login: ', error)
          this.error = 'Identifiants incorrects, veuillez réessayer.' })
    }
  }
}
</script>
