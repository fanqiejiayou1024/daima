<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-11-07 17:46:43
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-11-07 18:14:39
 * @FilePath: \vue-zy-2\src\components\Fufg.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <button @click="content = tiyu" >体育</button>
    <button @click="content = junshi">军事</button>
    <button @click="content = guoji">国际</button>
    <button @click="content = yuli">娱乐</button>
    <div>
        <KeepAlive>
            <component :is="content"></component>
        </KeepAlive>
    </div>
</template>

<script setup>
    
    import tiyu from './Tiyu.vue'
    import junshi from './JunShi.vue'
    import guoji from './GuoJi.vue'
    import yuli from './Yuli.vue'

    // 引入shallowRef方法，设置默认页面
    import { shallowRef,KeepAlive } from "vue";
    const content = shallowRef(tiyu)  
</script>

<style scoped>
    button{
        margin-right: 40px;
        height: 100px;
        width: 150px;
        font-size: 30px;
        color: rgb(255,255,255);
        background-color: rgb(223, 13, 160);
    }
</style>