<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 15:48:47
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 11:44:10
 * @FilePath: \router-demo\src\components\zi\yonghu.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>
        <h2 class="text-header">权限管理</h2>
    </div>
    <table border="" class="user_table">
        <thead>
            <tr>
                <th>编号</th>
                <th>用户名</th>
                <th>用户类型</th>
                <th>是否为官方工作人员</th>
                <th>是否为管理员</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in userList" :key="item.id">
                <td>
                    {{ item.id }}
                </td>
                <td>
                    {{ item.name }}
                </td>
                <td>
                    {{ item.quanxian }}
                </td>
                <td>
                    {{ item.guangfang }}
                </td>
                <td>
                    {{ item.guanlian }}
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>


    //模拟mysql获取用户数据
    const userList = [
        {id:1,name:'admin',quanxian:'超级管理员',guangfang:'是',guanlian:'是'},
        {id:2,name:'xiaomi',quanxian:'工作人员',guangfang:'是',guanlian:'否'},
        {id:3,name:'zs',quanxian:'用户',guangfang:'否',guanlian:'否'},
        {id:4,name:'ls',quanxian:'用户',guangfang:'否',guanlian:'否'},
        {id:5,name:'xm_xx',quanxian:'xx小米之家',guangfang:'是',guanlian:'否'},
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