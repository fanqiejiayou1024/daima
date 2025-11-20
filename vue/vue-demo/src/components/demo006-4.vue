<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-10-16 16:31:42
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-10-16 16:44:24
 * @FilePath: \vue-demo\src\components\demo006-4.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <button @click = "change">切换图片</button><hr/>
    <div>
        <img :src="img" style="width: 400px;"/>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    let img = ref('E:/daima/vue/vue-demo/src/assets/img/1.jpg')
    const change = () => {
        if (img.value == 'E:/daima/vue/vue-demo/src/assets/img/1.jpg') {
            img.value = 'E:/daima/vue/vue-demo/src/assets/img/2.jpg'
        }else if(img.value == 'E:/daima/vue/vue-demo/src/assets/img/2.jpg'){
            img.value = 'E:/daima/vue/vue-demo/src/assets/img/3.jpg'
        }else if(img.value == 'E:/daima/vue/vue-demo/src/assets/img/3.jpg'){
            img.value = 'E:/daima/vue/vue-demo/src/assets/img/4.jpg'
        }else{
            img.value = 'E:/daima/vue/vue-demo/src/assets/img/1.jpg'
        }
    }
</script>