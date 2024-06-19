<template>
    <form method="POST" @submit.prevent="addCategory">
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="name" v-model="name" class="form-control" placeholder="name" required /><label>Email
                    address</label>
            </div>
        </div>

        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="desc" v-model="desc" class="form-control" placeholder="desc" required /><label>Email
                    address</label>
            </div>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4"> Creer </button>
    </form>

    <div class="container-fluid">
        <form action="fetchCategories" method="GET">
            <ul class="list-group">
                <li class="list-group-item list-group-item-action list-group-item-numbered" :v-for="category in categories">
                    <div class="card">
                        <div class="card-header">
                            <a class="btn" data-bs-toggle="collapse" href="#{{category.name}}">
                                {{ category.name }}
                            </a>
                        </div>
                        <div id="{{category.name}}" class="collapse show" data-bs-parent="#accordion">
                            <div class="card-body">
                                {{ category.desc }}
                                <p class="float-right"><u><i>{{ formatDateTime(category.time) }}</i></u></p>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </form>
    </div>
</template>

<script>
    import api from '@/api';
    import moment from 'moment';
    import $ from 'jquery';

    $(document).ready(function() {
        $('li').each(function() {
            $(this).fadeIn("slow");
        });
    });

    export default {
        name: 'CategoryView',
        data() {
            return { name: '', desc: '', categories: [], }
        },
        created() {
            this.fetchCategories();
        },
        methods: {
            fetchCategories() {
                api.get('/api/categories/')
                    .then(response => {
                        this.categories = response.data.map(cat => cat.name);
                    })
                    .catch(error => { console.error('Error fetching categories:', error); });
            },
            addCategory() {
                const data = { name: this.name, desc: this.desc, };

                api.post('/api/categories/', data)
                    .then(response => {
                        console.log('Quiz created:', response.data);
                    })
                    .catch(error => { console.error('Error creating category:', error); });
            },
            formatDateTime(dateTime) {
                return moment(dateTime).locale('fr').format('ddd DD MMM, HH[h] mm[min]');
            },
        },
    }
