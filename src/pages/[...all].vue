<template>
    <h1 class="text-center">Not Good</h1>
    <NotFoundComponent error="4 0 4" />
</template>

<script>
import NotFoundComponent from './../components/NotFound.vue'

export default {
    name: 'NotFound',
    components: { NotFoundComponent, },
}
</script>