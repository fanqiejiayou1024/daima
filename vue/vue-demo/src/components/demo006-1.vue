<template>
    <button @click="show">点我</button>
</template>

<script setup>
    const show = (e) =>{
        //console.log(e)
        //console.log(e.target)
        //console.log(e.target.innerText)
        e.target.innerText = "我被点击了"
        e.target.style.color = "red"
        e.target.style.width = "300px"
        e.target.style.height = "300px"
        e.target.style.fontSize = "50px"
        e.target.style.fontWeight = "bold"
    }
</script>

<style lang="scss" scoped>

</style>