<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 15:48:47
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 16:46:12
 * @FilePath: \router-demo\src\components\zi\yonghu.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div>
        <h2 class="text-header">商品管理</h2>
    </div>
    <table border="" class="user_table">
        <thead>
            <tr>
                <th>商品图片</th>
                <th>商品编号</th>
                <th>商品名</th>
                <th>规格</th>
                <th>单价（元）</th>
                <th>库存（台）</th>
                <th>描述</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in userList" :key="item.id">
                <td class="img_box">
                    <img :src="'/src/assets/cp/'+item.id+'.jpg'" alt="">
                </td>
                <td>
                    {{item.id}}
                </td>
                <td>
                    {{item.name}}
                </td>
                <td>
                    {{item.guige}}
                </td>
                <td>
                    {{ item.danjia }}
                </td>
                <td>
                    {{ item.kucun }}
                </td>
                <td>
                    <router-link :to="'/home/goods_details/'+item.id">详情</router-link>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>


    //模拟mysql获取用户数据
    const userList = [
        {id:1,name:"Xiaomi 15 pro 16+1T 亮银版",guige:"台",danjia:"6699",kucun:"10000"},
        {id:2,name:"Xiaomi 15 定制版",guige:"台",danjia:"4999",kucun:"100"},
        {id:3,name:"Xiaomi 14 Ultra 钛金属特别版",guige:"台",danjia:"8299",kucun:"19999"},
        {id:4,name:"Xiaomi MIX Fold 4 16+1T 龙鳞纤维版",guige:"台",danjia:"10999",kucun:"1999"},
        {id:5,name:"Xiaomi SU7 Ultra",guige:"台",danjia:"814900",kucun:"0"},
        {id:6,name:"Xiaomi MIX Alpha",guige:"台",danjia:"19999",kucun:"0"},
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