<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-09-25 16:01:41
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-09-25 16:23:33
 * @FilePath: \vue-demo\src\components\demo4-1.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>{{ num }}</div>
    <button @click = "add">"点击增加"</button>
</template>

<script setup>
    import { ref } from 'vue';
    const num = ref(1)
    const add = () =>{

        num.value++
        console.log(num.value);
    }
</script>