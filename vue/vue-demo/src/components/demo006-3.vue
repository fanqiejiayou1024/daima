<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-10-16 15:50:14
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-10-16 16:06:20
 * @FilePath: \vue-demo\src\components\demo006-3.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <button @click = "change">change</button>
    <div :class = "divCss">hall</div>
</template>

<script setup>
    import { ref } from 'vue';
    let divCss = ref('a')
    const change = () => {
        if (divCss.value == 'a'){
            divCss.value = 'b'
        }else {
            divCss.value = 'a'
        }
    }
</script>

<style scoped>
    .a{
        width: 300px;
        height: 200px;
        background-color: purple;
        color: white;
        font-size: 25px;
    }
    .b{
        width: 500px;
        height: 300px;
        background-color: blue;
        color: gold;
        font-size: 40px;
    }
</style>