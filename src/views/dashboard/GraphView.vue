<template>
    <div class="flex flex-row flex-wrap flex-grow mt-2">

        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
            <!--Graph Card-->
            <div class="bg-white border-transparent rounded-lg shadow-xl">
                <div
                    class="bg-gradient-to-b from-gray-300 to-gray-100 uppercase text-gray-800 border-b-2 border-gray-300 rounded-tl-lg rounded-tr-lg p-2">
                    <h5 class="font-bold uppercase text-gray-600">Graph</h5>
                </div>
                <div class="p-5"><canvas id="chartjs-4" class="chartjs" width="undefined" height="undefined"></canvas>

                </div>
            </div>
            <!--/Graph Card-->
        </div>

        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
            <!--Table Card-->
            <div class="bg-white border-transparent rounded-lg shadow-xl">
                <div
                    class="bg-gradient-to-b from-gray-300 to-gray-100 uppercase text-gray-800 border-b-2 border-gray-300 rounded-tl-lg rounded-tr-lg p-2">
                    <h5 class="font-bold uppercase text-gray-600">Graph</h5>
                </div>
                <div class="p-5">
                    <table class="w-full p-5 text-gray-700">
                        <thead>
                            <tr>
                                <th class="text-left text-blue-900">Theme</th>
                                <th class="text-left text-blue-900">Points</th>
                                <th class="text-left text-blue-900">Niveau</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Culture</td>
                                <td>+1</td>
                                <td>Facile</td>
                            </tr>
                            <tr>
                                <td>Parasites</td>
                                <td>+10</td>
                                <td>Difficle</td>
                            </tr>
                            <tr>
                                <td>Cuisine</td>
                                <td>+5</td>
                                <td>Moyen</td>
                            </tr>
                        </tbody>
                    </table>

                    <p class="py-2"><router-link :to="{}">Voir plus ...</router-link></p>

                </div>
            </div>
            <!--/table Card-->
        </div>

        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
            <!--Advert Card-->
            <div class="bg-white border-transparent rounded-lg shadow-xl">
                <div
                    class="bg-gradient-to-b from-gray-300 to-gray-100 uppercase text-gray-800 border-b-2 border-gray-300 rounded-tl-lg rounded-tr-lg p-2">
                    <h5 class="font-bold uppercase text-gray-600">Advert</h5>
                </div>
                <div class="p-5 text-center shadow-2xl">
                    <!-- <script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CK7D52JJ&placement=wwwtailwindtoolboxcom" id="_carbonads_js"></script> -->
                    <div class="text-5xl font-extrabold ...">
                        <span class="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500">
                            Hello world
                        </span>
                    </div>
                </div>
            </div>
            <!--/Advert Card-->
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
    name: 'GraphView',
    mounted() {
        new Chart(document.getElementById("chartjs-4"), {
            "type": "doughnut",
            "data": {
                "labels": ["Difficle", "Moyen", "facile"],
                "datasets": [{
                    "label": "Niveaux",
                    "data": [4, 2, 5],
                    "backgroundColor": ["rgb(255, 99, 132)", "rgb(54, 162, 235)", "rgb(255, 205, 86)"]
                }]
            }
        });
    },
}
</script>