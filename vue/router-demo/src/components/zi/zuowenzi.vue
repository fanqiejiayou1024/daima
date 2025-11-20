<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 14:04:30
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 11:11:54
 * @FilePath: \router-demo\src\components\zi\zuowenzi.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <!-- 侧边栏 -->
    <div class="aside-container">
        <ul class="menu">
            <li class="menu-item">
                <router-link to="/home/users">用户管理</router-link>
            </li>
            <li class="menu-item">
                <router-link to="/home/rights">权限管理</router-link>
            </li>
            <li class="menu-item">
                <router-link to="/home/goods">商品管理</router-link>
            </li>
            <li class="menu-item">
                <router-link to="/home/orders">订单管理</router-link>
            </li>
            <!--<li class="menu-item">
                <router-link to="/home/setting">全局设置</router-link>
            </li>-->
        </ul>
    </div>
</template>

<script setup>


</script>

<style scoped>
    .aside-container{
        width: 280px;
        height: calc(100vh - 51px);
        border-right: 1px solid #000;
        .menu{
            list-style-type: none;
            padding: 0px;
            .menu-item{
                line-height: 50px;
                font-weight: bold;
            }
        }
        a{
            font-size: 18px;
            display: block;
            color: gray;
            padding-left: 100px;
            text-decoration: none;
        }
        a:hover{
            background-color: #ff6900;
            color: #fff;
            cursor: pointer;
        }
    }
</style>