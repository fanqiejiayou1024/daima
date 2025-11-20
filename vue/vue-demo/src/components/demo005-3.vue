<template>
    <button @click="show_1">v-if</button><br/>
    <img v-if="flag_1" src="../assets/img/1.png" style="width: 300px;"/>
    <hr />
    <button @click="show_2">v-show</button><br />
    <img v-show="flag_2" src="../assets/img/2.png" style="width: 300px;"/>
</template>

<script setup>
    import { ref } from 'vue';
    //v-if
    let flag_1 = ref(true);
    const show_1 = () => {
        flag_1.value = !flag_1.value;
    }
    //v-show
    let flag_2 = ref(true);
    const show_2 = () => {
        flag_2.value = !flag_2.value;
    }
</script>