<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-10-09 15:14:15
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-10-09 15:17:45
 * @FilePath: \vue-demo\src\components\demo005-2.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>年龄：{{ age }}</div>
    <div>分数：{{ score }}</div>
    <button v-on:click="add_age">年龄+1</button>
    <button @click="add_score">分数+1</button>
</template>

<script setup>
    import { ref } from 'vue'
    const age = ref(18)
    const add_age = () => {
        age.value++
    }
    const score = ref(90)
    const add_score = () => {
        score.value++
    }
</script>

<style lang="scss" scoped>

</style>