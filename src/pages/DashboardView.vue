<template>
    <!--Nav-->
    <nav class="bg-gray-800 pt-2 md:pt-1 pb-1 px-1 mt-0 h-auto fixed w-full z-20 top-0">
        <div class="flex flex-wrap items-center">
            <div class="flex flex-shrink md:w-1/3 justify-center md:justify-start text-white">
                <router-link :to="{ name: 'dashboard' }">
                    <span class="text-xl pl-2"><i class="em em-grinning"></i> {{ head }}</span>
                </router-link>
            </div>

            <div class="flex flex-1 md:w-1/3 justify-center md:justify-start text-white px-2">
                <span class="relative w-full">
                    <input type="search" placeholder="Search"
                        class="w-full bg-gray-900 text-white transition border border-transparent focus:outline-none focus:border-gray-400 rounded py-3 px-2 pl-10 appearance-none leading-normal">
                    <div class="absolute search-icon" style="top: 1rem; left: .8rem;">
                        <svg class="fill-current pointer-events-none text-white w-4 h-4"
                            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                            <path d="M12.9 14.32a8 8 0 1 1 1.41-1.41l5.35 5.33-1.42 1.42-5.33-5.34zM8 14A6 6 0 1 0 8 2a6 6 0 0 0 0 12z">
                            </path>
                        </svg>
                    </div>
                </span>
            </div>

            <div class="flex w-full pt-2 content-center justify-between md:w-1/3 md:justify-end">
                <ul class="list-reset flex justify-between flex-1 md:flex-none items-center">
                    <li class="flex-1 md:flex-none md:mr-3">
                        <router-link class="inline-block py-2 px-4 text-white no-underline" :to="{}">Quiz</router-link>
                    </li>
                    <li class="flex-1 md:flex-none md:mr-3">
                        <router-link class="inline-block text-gray-600 no-underline hover:text-gray-200 hover:text-underline py-2 px-4"
                            :to="{ name: 'createQuiz' }">Nouveau</router-link>
                    </li>
                    <li class="flex-1 md:flex-none md:mr-3">
                        <div class="relative inline-block">
                            <button @click="toggleDD('myDropdown')" class="drop-button text-white focus:outline-none">
                                <span class="pr-2"><i class="em em-robot_face"></i></span> Hi, {{ nom }} <svg
                                    class="h-3 fill-current inline" xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 20 20">
                                    <path
                                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                                </svg></button>
                            <div id="myDropdown"
                                class="dropdownlist absolute bg-gray-800 text-white right-0 mt-3 p-3 overflow-auto z-30 invisible">
                                <input type="text" class="drop-search p-2 text-gray-600" placeholder="Search.."
                                    id="myInput" onkeyup="filterDD('myDropdown','myInput')">
                                <router-link :to="{}"
                                    class="p-2 hover:bg-gray-800 text-white text-sm no-underline hover:no-underline block"><i
                                        class="fa fa-user fa-fw"></i> Profile</router-link>
                                <router-link :to="{}"
                                    class="p-2 hover:bg-gray-800 text-white text-sm no-underline hover:no-underline block"><i
                                        class="fa fa-cog fa-fw"></i> Settings</router-link>
                                <div class="border border-gray-800"></div>
                                <router-link :to="{ name: 'landPage' }"
                                    class="p-2 hover:bg-gray-800 text-white text-sm no-underline hover:no-underline block"><i
                                        class="fas fa-sign-out-alt fa-fw"></i> Log Out</router-link>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- / Nav-->
    <div class="bg-gray-800 font-sans leading-normal tracking-normal mt-12">
        <NavDash />
        <div class="flex flex-col md:flex-row">
            <MenuView />
            <div class="main-content flex-1 bg-gray-100 mt-12 md:mt-2 pb-24 md:pb-5">
                <div class="bg-gray-800 pt-3">
                    <div
                        class="rounded-tl-3xl bg-gradient-to-r from-blue-900 to-gray-800 p-4 shadow text-2xl text-white">
                        <h3 class="font-bold pl-2">Dashboard</h3>
                    </div>
                </div>
                <MetricCard />
                <GraphView />
            </div>
        </div>
    </div>
</template>

<script>
import MenuView   from '@/views/dashboard/MenuView.vue'
import GraphView  from '@/views/dashboard/GraphView.vue'
import MetricCard from '@/views/dashboard/MetricCard.vue'
import '@/assets/style/css/output.css';

export default {
    name: 'DashboardView',
    components: { MenuView, GraphView, MetricCard, },
    data() {
        return {}
    },
    methods: {
        toggleDD(e, myDropMenu) { document.getElementById(myDropMenu).classList.toggle("invisible"); },
        filterDD(e, myDropMenu, myDropMenuSearch) { var input, filter, a, i, div; input = document.getElementById(myDropMenuSearch); filter = input.value.toUpperCase(); div = document.getElementById(myDropMenu); a = div.getElementsByTagName("a"); for (i = 0; i < a.length; i++) { a[i].style.display = a[i].innerHTML.toUpperCase().indexOf(filter) > -1 ? "" : "none"; } },
        handleWindowClick(event) { if (!event.target.matches('.drop-button') && !event.target.matches('.drop-search')) { var dropdowns = document.getElementsByClassName("dropdownlist"); for (var i = 0; i < dropdowns.length; i++) { var openDropdown = dropdowns[i]; if (!openDropdown.classList.contains('invisible')) { openDropdown.classList.add('invisible'); } } } }
    },
    mounted() { window.addEventListener('click', this.handleWindowClick); },
}
</script>