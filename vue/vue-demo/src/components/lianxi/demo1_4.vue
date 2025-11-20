<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-09-25 20:16:56
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-09-25 20:17:15
 * @FilePath: \vue-demo\src\components\lianxi\demo1_4.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>{{ a1 }}</div>
    <button @click="a">点我</button>
</template>

<script setup>
    import { ref } from 'vue';
    const a1 = ref(0);
    const a = () => {
        a1.value++;
    };
</script>

<style lang="scss" scoped>

</style>