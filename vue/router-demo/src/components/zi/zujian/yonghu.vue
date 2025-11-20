<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 15:48:47
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 17:08:43
 * @FilePath: \router-demo\src\components\zi\yonghu.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <!--标题-->
    <h2 class="text-header">用户管理</h2>
    <!--用户列表-->
    <table border="" class="user_table">
        <thead>
            <tr>
                <th>头像</th>
                <th>编号</th>
                <th>姓名</th>
                <th>职业</th>
                <th>描述</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in userList" :key="item.id">
                <td class="img_box">
                    <img :src="'/src/assets/yh/'+item.id+'.jpg'" alt="">
                </td>
                <td>
                    {{item.id}}
                </td>
                <td>
                    {{item.name}}
                </td>
                <td>
                    {{item.job}}
                </td>
                <td>
                    <router-link :to="'/home/users_details/'+item.id">详情</router-link>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>


    //模拟mysql获取用户数据
    const userList = [
        {id:1,name:'尤雨溪',job:'前端工程师'},
        {id:2,name:'吉多·范罗苏姆',job:'后端工程师'},
        {id:3,name:'李腾',job:'化学博士生'},
        {id:4,name:'王思聪',job:'董事长'},
        {id:5,name:'李维腾',job:'废物一枚'},
        {id:6,name:'雷军',job:'小米科技创始人'}
    ]

</script>

<style scoped>
    .user_table{
        width: 100%;
        text-align: center;
        .img_box{
            width: 100px;
        }
        img{
            height: 50px;
        }
    }
    .text-header{
        text-align: center; 
    }
</style>