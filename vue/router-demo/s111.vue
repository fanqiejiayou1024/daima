<template>
    <div class="login-container">
        <div>
            <div class="logo-box">
                <img class="top-logo" src="../assets/logo.png" alt="">
            </div>
            <h2>login</h2>
            <form >
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" v-model.trim="username" required>   
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" v-model.trim="password" required>   
                </div>
                <div class="form-group">
                    <button type="button" class="btn" @click="login">login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    const router = useRouter()
    const username = ref("")
    const password = ref("")
    const login = ()=>{
        if (username.value ==='admin' && password.value === "admin"){
            router.push("/home/users")
            return localStorage.setItem('token','this is a token')
        } else{
            alert("用户名或密码错误")
            localStorage.removeItem("token")
        }
    }

</script>

<style  scoped>
    
    .login-container{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #E6E6FA;
        .logo-box{
            text-align: center;
        }
        .top-logo{
            width: 100px;
            border-radius: 50%;
        }
        h2{
            text-align: center;
            margin-bottom: 20px;
        }
        form{
            width: 400px;
            border: 1px solid #7B68EE;
            padding: 40px;
            border-radius: 20px;
            .form-group{
                margin-bottom: 15px;
            }
            label{
                display: block;
                margin-bottom: 5PX;
            }
            input{
                width: 100%;
                padding: 10px;
                border: 1px solid #7B68EE;
                border-radius: 4px;
                box-sizing: border-box;

            }
            .btn{
                width: 100%;
                padding: 10px;
                border: none;
                background-color: #7B68EE;
                color: #fff;
                cursor: pointer;
                font-size: 16px;
            }
            .bth:hover{
                background-color: rgb(105, 36, 151);
                color: wheat;
            }
        }
    }
</style>