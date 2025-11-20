<template>
    <div>
        <img :src = "img" style = "width: 400px;">
    </div>
</template>

<script setup>
    import { onMounted,ref } from 'vue'
    let img = ref("src/assets/s1.png")
    onMounted(()=>{
        setInterval(()=>{
            if(img.value == "src/assets/s1.png"){
                img.value = "src/assets/s2.png"
            }else if(img.value == "src/assets/s2.png"){
                img.value = "src/assets/s3.png"
            }else if(img.value == "src/assets/s3.png"){
                img.value = "src/assets/s4.png"
            }else{
                img.value = "src/assets/s1.png"
                //img.value = "src/assets/s4.png"
            }
        },2000)
    })
</script>

<style scoped>

</style>