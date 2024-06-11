<template>
  <section id="scroll">
    <div class="container px-5">
      <div class="row gx-5 align-items-center">
        <div class="col-lg-6 order-lg-2">
          <div class="p-5"><img class="img-fluid rounded-circle" src="@/assets/img/01.jpg" alt="Picture" head="Picture 0x00: Testez vos connaissances" /></div>
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
          <div class="p-5"><img class="img-fluid rounded-circle" src="@/assets/img/02.jpg" alt="Picture" head="Picture 0x00: Énigmes et quiz pour stimuler votre cerveau" /></div>
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
          <div class="p-5"><img class="img-fluid rounded-circle" src="@/assets/img/03.jpg" alt="Picture" title="Picture 0x00: Élargissez vos connaissances" /></div>
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
import '@/assets/style/css/output.css';
export default {
  name: 'LandView',
  props: { msg: String, subMsg: String, head: String },
  mounted() {
    this.handleScroll();
    window.addEventListener('scroll', this.handleScroll);
    document.addEventListener('click', this.handleClick);
  },
  methods: {
    handleScroll() { const scrollpos = window.scrollY; const header = this.$el.querySelector('#header'); const navcontent = this.$el.querySelector('#nav-content'); const navaction = this.$el.querySelector('#navAction'); const toToggle = this.$el.querySelectorAll('.toggleColour'); if (scrollpos > 10) { header.classList.add('bg-white'); navaction.classList.remove('bg-white'); navaction.classList.add('gradient'); navaction.classList.remove('text-gray-800'); navaction.classList.add('text-white'); for (let i = 0; i < toToggle.length; i++) { toToggle[i].classList.add('text-gray-800'); toToggle[i].classList.remove('text-white'); } header.classList.add('shadow'); navcontent.classList.remove('bg-gray-100'); navcontent.classList.add('bg-white'); } else { header.classList.remove('bg-white'); navaction.classList.remove('gradient'); navaction.classList.add('bg-white'); navaction.classList.remove('text-white'); navaction.classList.add('text-gray-800'); for (let i = 0; i < toToggle.length; i++) { toToggle[i].classList.add('text-white'); toToggle[i].classList.remove('text-gray-800'); } header.classList.remove('shadow'); navcontent.classList.remove('bg-white'); navcontent.classList.add('bg-gray-100'); } },
    handleClick(e) { const target = e.target; const navMenuDiv = this.$el.querySelector('#nav-content'); const navMenu = this.$el.querySelector('#nav-toggle'); if (!this.checkParent(target, navMenuDiv)) { navMenuDiv.classList.contains('hidden') ? this.checkParent(target, navMenu) ? null : navMenuDiv.classList.add('hidden') : navMenuDiv.classList.add('hidden'); } },
    checkParent(t, elm) { while (t.parentNode) { if (t === elm) { return true; } t = t.parentNode; } return false; }
  }
}
</script>

<style>
    .gradient { background: linear-gradient(90deg, #d53369 0%, #daae51 100%); }
  </style>