<template>
  <form method="POST" @submit.prevent="signin">
    <div class="alert alert-success mb-3" v-if="msg">{{ msg }}</div>
    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="form-group">
          <div class="form-floating">
            <input
              type="text"
              v-model="nom"
              class="form-control"
              placeholder="nom"
              required
            /><label>Nom</label>
          </div>
        </div>
      </div>
      <div class="col-md-6 mb-4">
        <div class="form-group">
          <div class="form-floating">
            <input
              type="text"
              v-model="prenom"
              class="form-control"
              placeholder="prenom"
              required
            /><label>Prenom</label>
          </div>
        </div>
      </div>
    </div>

    <div class="form-group mb-4">
      <div class="form-floating">
        <input
          type="email"
          v-model="email"
          class="form-control"
          placeholder="email"
          required
        /><label>Email address</label>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="form-group">
          <div class="form-floating">
            <input
              type="password"
              v-model="password"
              class="form-control"
              placeholder="password"
              required
            /><label>Password</label>
          </div>
        </div>
      </div>
      <div class="col-md-6 mb-4">
        <div class="form-group">
          <div class="form-floating">
            <input
              type="password"
              v-model="confirmPassword"
              class="form-control"
              placeholder="confirmPassword"
              required
            /><label>Confirm Password</label>
          </div>
        </div>
      </div>
    </div>
    <div class="mb-4 text-center alert alert-danger" v-if="error">
      {{ error }}
    </div>
    <div class="form-group mb-4">
      <div class="form-floating">
        <input
          type="text"
          v-model="domicile"
          class="form-control"
          placeholder="domicile"
          required
        /><label>Domicile</label>
      </div>
    </div>

    <div class="form-group mb-4">
      <div class="form-floating">
        <input
          type="text"
          v-model="username"
          class="form-control"
          placeholder="username"
          required
        /><label>Nom utilisateur</label>
      </div>
    </div>

    <div class="form-check d-flex justify-content-center mb-4">
      <input
        class="form-check-input me-2"
        type="checkbox"
        value=""
        id="form2Example33"
        checked
      />
      <label class="form-check-label" for="form2Example33"
        >Subscribe to our newsletter</label
      >
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">
      Sign up
    </button>

    <div class="text-center">
      <p>or sign up with:</p>
      <button
        type="button"
        title="Facebook"
        class="btn btn-link btn-floating mx-1"
      >
        <fa :icon="['fab', 'facebook-f']" />
      </button>
      <button
        type="button"
        title="Google"
        class="btn btn-link btn-floating mx-1"
      >
        <fa :icon="['fab', 'google']" />
      </button>
      <button
        type="button"
        title="Twitter"
        class="btn btn-link btn-floating mx-1"
      >
        <fa :icon="['fab', 'twitter']" />
      </button>
      <button
        type="button"
        title="Github"
        class="btn btn-link btn-floating mx-1"
      >
        <fa :icon="['fab', 'github']" />
      </button>
    </div>
  </form>
</template>

<script>
import api from '@/api'

export default {
  name: 'SignInView',
  data () {
    return {
      nom: '',
      prenom: '',
      username: '',
      domicile: '',
      email: '',
      password: '',
      confirmPassword: '',
      error: '',
      msg: ''
    }
  },
  methods: {
    signin () {
      const data = {
        nom: this.nom,
        prenom: this.prenom,
        email: this.email,
        domicile: this.domicile,
        password: this.password,
        username: this.username
      }
      if (this.password === this.confirmPassword) {
        api
          .post('/api/users/', data)
          .then(response => {
            console.log('User created:', response.data)
            this.msg = 'Password does not match with confirm password'
            this.$router.push('/login')
          })
          .catch(error => {
            console.error('Error creating User:', error)
            this.error = 'Signin failed'
          })
      } else {
        this.error = 'Password does not match with confirm password'
      }
    }
  }
}
</script>
