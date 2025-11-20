<template>
    <button @click="add">{{ "切换" }}</button>
</template>

<script setup>
    import { ref } from 'vue'
    let sum = ref(1)
    const add = () => {
        sum.value++
    }
    
</script>

<style scoped>

</style>