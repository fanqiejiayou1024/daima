<template>
    <div>姓名：{{ stud.name }}</div>
    <div>当前年龄：{{ stud.age }}</div>
    <div>当前就读于：{{ stud.grade }}</div>
    <button @click="addAge">增加年龄</button>
    <button @click="addGrade">增加年级</button>
</template>

<script setup>
    import { reactive } from "vue";
    const stud = reactive({
        name:"fanqie",
        age:20,
        grade:1
    })
    const addAge = () =>{
        stud.age++
    }
    const addGrade = () =>{
        stud.grade++
    }
</script>