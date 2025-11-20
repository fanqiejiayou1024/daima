<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 15:48:47
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 11:58:46
 * @FilePath: \router-demo\src\components\zi\yonghu.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>
        <h2 class="text-header">订单管理</h2>
    </div>
    <table border="" class="user_table">
        <thead>
            <tr>
                <th>订单号</th>
                <th>商品名</th>
                <th>购买人</th>
                <th>单价（元）</th>
                <th>购买量（台）</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in userList" :key="item.id">
                <td>
                    {{item.id}}
                </td>
                <td>
                    {{item.name}}
                </td>
                <td>
                    {{item.goumairen}}
                </td>
                <td>
                    {{ item.danjia }}
                </td>
                <td>
                    {{ item.shuliang }}
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>


    //模拟mysql获取用户数据
    const userList = [
        {id:1,name:"Xiaomi 15 pro 16+1T 亮银版",goumairen:"张三",danjia:"6699",shuliang:"10"},
        {id:2,name:"Xiaomi 15 定制版",goumairen:"王五",danjia:"4999",shuliang:"19"},
        {id:3,name:"Xiaomi 14 Ultra 钛金属特别版",goumairen:"李四",danjia:"8299",shuliang:"51"},
        {id:4,name:"Xiaomi MIX Fold 4 16+1T 龙鳞纤维版",goumairen:"zhf",danjia:"10999",shuliang:"100"},
        {id:5,name:"Xiaomi SU7 Ultra",goumairen:"Xiaomi ev",danjia:"814900",shuliang:"1"},
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