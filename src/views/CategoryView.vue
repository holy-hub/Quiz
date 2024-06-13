<template>
    <form method="POST" @submit.prevent="addCategory">
        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="name" v-model="name" class="form-control" placeholder="name" required /><label>Email address</label>
            </div>
        </div>

        <div class="form-group mb-4">
            <div class="form-floating">
                <input type="desc" v-model="desc" class="form-control" placeholder="desc" required /><label>Email address</label>
            </div>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4"> Creer </button>
    </form>

    <div class="container-fluid">
        <form action="" method="GET">
            <ul class="list-group">
                <li class="list-group-item list-group-action" :v-for="category in categories">{{ category.name }}</li>
            </ul>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
import $ from 'jquery';

$(document).ready(() => {
    $('li').each(() => {
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
            axios.get('api/categories/')
                .then(response => {
                    this.categories = response.data.map(cat => cat.name);
                })
                .catch(error => {
                    console.error('Error fetching categories:', error);
                });
        },
        addCategory() {
            const data = { name: this.name, desc: this.desc, };

            axios.post('api/category/', data)
                .then(response => {
                    console.log('Quiz created:', response.data);
                })
                .catch(error => { console.error('Error creating category:', error); });
        },
    },
}
</script>