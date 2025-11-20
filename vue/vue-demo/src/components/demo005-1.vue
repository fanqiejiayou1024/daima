<template>
    <div v-text="t1"></div>
    <div v-text="t2"></div>
    <div v-html="h1"></div>
    <div v-html="h2"></div>
</template>

<script setup>
    const t1 = "1-normal"
    const t2 = "<div>2-normal</div>"
    const h1 = "3-normal"
    const h2 = "<div>4-normal</div>"
</script>

<style scoped>
</style>