<template>
    <header class="masthead text-center text-white">
      <div class="masthead-content">
        <div class="container px-5">
          <h1 class="masthead-heading mb-0">{{ msg }}</h1>
          <h2 class="masthead-subheading mb-0">{{ subMsg }}</h2>
          <router-link class="btn btn-primary btn-xl rounded-pill mt-5" :to="{ name: 'doQuiz' }">Faire du Quiz</router-link>
        </div>
      </div>
      <div class="bg-circle-1 bg-circle"></div><div class="bg-circle-2 bg-circle"></div><div class="bg-circle-3 bg-circle"></div><div class="bg-circle-4 bg-circle"></div>
    </header>
    <section id="scroll">
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6 order-lg-2">
            <div class="p-5"><img class="img-fluid rounded-circle" src="./../assets/img/01.jpg" alt="Picture" head="Picture 0x00: Testez vos connaissances" /></div>
          </div>
          <div class="col-lg-6 order-lg-1">
            <div class="p-5">
              <h2 class="display-4">Testez vos connaissances ...</h2>
              <p>{{ head }} est une application de quiz divertissante avec des catégories variées. Répondez à des questions à choix multiples dans un temps imparti et découvrez votre score final. Défiez vos amis et partagez vos résultats !</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6">
            <div class="p-5"><img class="img-fluid rounded-circle" src="./../assets/img/02.jpg" alt="Picture" head="Picture 0x00: Énigmes et quiz pour stimuler votre cerveau" /></div>
          </div>
          <div class="col-lg-6">
            <div class="p-5">
              <h2 class="display-4">Énigmes et quiz pour stimuler votre cerveau!</h2>
              <p>{{ head }} vous propose des énigmes et des quiz pour tester votre logique et vos compétences générales. Entraînez votre cerveau avec des défis progressifs et mesurez-vous à d'autres joueurs !</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6 order-lg-2">
            <div class="p-5"><img class="img-fluid rounded-circle" src="./../assets/img/03.jpg" alt="Picture" title="Picture 0x00: Élargissez vos connaissances" /></div>
          </div>
          <div class="col-lg-6 order-lg-1">
            <div class="p-5">
              <h2 class="display-4">Élargissez vos connaissances!</h2>
              <p>{{ head }} est une application éducative avec des quiz interactifs sur divers sujets. Apprenez de nouvelles informations intéressantes tout en vous amusant avec des questions stimulantes.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
export default {
  name: 'LandView',
  props: { msg: String, subMsg: String, head: String },
}
</script>