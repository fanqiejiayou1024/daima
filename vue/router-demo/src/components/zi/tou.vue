<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-18 13:09:44
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 17:25:44
 * @FilePath: \router-demo\src\components\zi\tou.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div class="header-container">
    <!--左侧logo和标题区-->
        <div class="header-left">
        <!--logo-->
            <img class="header-logo" src="../../assets/logo.png" alt="">
        
        <!--标题-->
            <h3 class="header-title">test----1</h3>
        </div>
        <!--右侧按钮-->
        <div class="header-right">
            <button type="button" class="btn" @click="logout">quit</button>
        </div>
    </div>
</template>

<script setup>
    import { useRouter } from 'vue-router';
    const route = useRouter()
    const logout = () => {
        localStorage.removeItem('token')
        route.push('/login')
    }
</script>

<style scoped>
    .header-container{
        height: 50px;
        border-bottom: 1px solid rebeccapurple;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 0.5rem;
        background-color: #FFEBCD;
        .header-left{
            display: flex;
            align-items: center;
            color: azure;
            .header-logo{
                width: 40px;
                margin-right: 10px;
                border-radius: 10px;
            }
        }
    }
    .header-right{
        display: flex;
        .btn{
            width: 50px;
            height: 30px;
            line-height: 32%;
            font-size: 20px;
            background-color: #ffff;
            border: 2px solid #FFEBCD;
            border-radius: 5px;
            color: #FFEBCD;
        }
        .btn:hover{
            color:#fff;
            background-color: #FFEBCD;
        }
        .header-title{
            color: #fff;
            
        }
    }
</style>