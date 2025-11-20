<template>
    <h2>军事新闻</h2><hr/>
    <img :src = "img" style = "width: 400px;"><hr/>
    <h4>陆军直升机到了！直-20、直-10和直-8L抵达中国航展</h4>
    <div>
        11月7日，来自陆军的直-20、直-10和直-8L三架直升机陆续抵达珠海。
    </div>
    <img src=" ../assets/junshi1.jpg" style="width: 500px;"><br/>
    <img src=" ../assets/junshi2.jpg" style="width: 500px;">
    <div>
        直-20是我国自主研制的多用途直升机，2013年12月首飞，2022年首次亮相中国航展。
        直-10是我国自主研发的第一款专用武装直升机，2016年首次在中国航展上公开展示，它的列装大大提高了中国人民解放军陆军航空兵的突击与反装甲能力。
        直-8L是在直-8直升机的基础上改进研制的大型宽体运输直升机。
    </div>
    <img src=" ../assets/junshi3.jpg" style="width: 500px;"><br/>
    <img src=" ../assets/junshi4.jpg" style="width: 500px;">
</template>

<script setup>
    import { onMounted,ref } from 'vue'
    let img = ref("src/assets/d_js.jpg")
    onMounted(()=>{
        setInterval(()=>{
            if(img.value == "src/assets/d_js.jpg"){
                img.value = "src/assets/d_js1.jpg"
            }else if(img.value == "src/assets/d_js1.jpg"){
                img.value = "src/assets/d_js2.jpg"
            }else{
                img.value = "src/assets/d_js.jpg"
            }},2000)
    })
</script>

<style scoped></style>