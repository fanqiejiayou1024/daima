<template>
    <div>当前年龄：{{ stud.age }}</div>
    <button @click="addAge">增加年龄</button>
</template>

<script setup>
    import { reactive,toRef } from "vue";
    const stud = reactive({
        name:"fanqie",
        age:20,
        grade:1
    })
    let s_age = toRef(stud,"age")
    const addAge = () =>{
        s_age.value++
    }
</script>