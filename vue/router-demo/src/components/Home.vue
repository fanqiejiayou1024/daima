<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-17 22:47:34
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-18 16:15:36
 * @FilePath: \router-demo\src\components\Home.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <tou></tou>
    <div class="home-box">
        <zuowenzi></zuowenzi>
        <!-- 右侧内容 -->
        <div class="home-box-r">
            <!-- 路由出口 -->
            <router-view></router-view>
        </div>
        <!--<div class="home-content">{{content}}</div>
        -->
    </div>
    
</template>

<script setup>
    //头
    import tou from './zi/tou.vue';
    //左侧文字
    import zuowenzi from './zi/zuowenzi.vue';
</script>
    
<style scoped>
    .home-box {
    display: flex;
    }

    .home-box-r {
    padding: 15px;
    flex: 1;
    }
</style>