<template>
    <button @click="reduce">-</button>
    &emsp;<span>{{ num }}</span>&emsp;
    <button @click="add">+</button>
</template>

<script setup>
    import { ref } from 'vue'
    const num = ref(0)
    const reduce = () => {
        if (num.value > 0) {
            num.value--
        }else {
            num.value = 0
        }
    }
    const add = () => {
        if (num.value < 10) {
            num.value++
        }else {
            num.value = 10
        }
    }
</script>

<style scoped>

</style>