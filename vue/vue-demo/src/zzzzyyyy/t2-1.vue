<template>
    <button v-for="im"></button>
</template>

<script setup>
    import { ref } from 'vue'
    const im = ref(1) 
</script>

<style scoped>

</style>