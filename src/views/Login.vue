<template>
    <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
        <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
        <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>
        <div class="card bg-glass">
            <div class="card-body px-4 py-5 px-md-5">
                <div class="my-4 text-center alert alert-danger" v-if="error">{{ error }}</div>
                <form method="post" @submit.prevent="login">
                    <div class="form-group mb-4">
                        <div class="form-floating">
                            <input type="email" v-model="email" class="form-control" placeholder="Email" /><label>Email address</label>
                        </div>
                    </div>
                    <div class="form-group mb-4">
                        <div class="form-floating">
                            <input type="password" v-model="password" class="form-control" placeholder="Password" /><label>password</label>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary btn-block mb-4"> Se connecter </button>

                    <div class="text-center">
                        <p>ou se connecter avec:</p>
                        <button type="button" class="btn btn-link btn-floating mx-1"> <i class="fab fa-facebook-f"></i>
                        </button>
                        <button type="button" class="btn btn-link btn-floating mx-1"> <i class="fab fa-google"></i>
                        </button>
                        <button type="button" class="btn btn-link btn-floating mx-1"> <i class="fab fa-twitter"></i>
                        </button>
                        <button type="button" class="btn btn-link btn-floating mx-1"> <i class="fab fa-github"></i>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
      name: 'LoginView',
      data() {
          return { email: '', password: '', error: '', };
      },
      methods: {
          login() {
              this.email === '' && this.password === '' ? this.$router.push('/View/Admin') : this.error = 'Identifiants incorrects, veuillez réessayer.';
          }
      },
  }
</script>