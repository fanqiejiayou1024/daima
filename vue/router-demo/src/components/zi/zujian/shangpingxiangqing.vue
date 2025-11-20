<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-19 12:26:08
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 16:54:22
 * @FilePath: \router-demo\src\components\zi\zujian\shangpingxiangqing.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div class="main">
        <h2>商品详情</h2>
        <div class="showDetails">
            <div class="show_img">
                <img :src="'/src/assets/cp/'+id+'.jpg'" alt="wu">
            </div>
            <div class="details">
                <div class="contnet">商品编号：{{ obj.id }}</div>
                <div class="contnet">商品名：{{ obj.name }}</div>
                <div class="contnet">价格：{{ obj.danjia }}</div>
                <div class="contnet">描述：{{ obj.instruction }}</div>
                <div></div>
                <div>
                    <button class="btn_back" @click="goBack">返回</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted, reactive } from 'vue';
    import { useRouter } from 'vue-router'
    const router = useRouter();
    const props = defineProps({
        id: String
    })
    const userList = [
        {id:1,name:"Xiaomi 15 pro 16+1T 亮银版",danjia:"6699",instruction:"骁龙8至尊版移动平台小米翼型环形冷泵散热系统6100mAh 小米金沙江电池90W 小米澎湃有线秒充｜50W 小米澎湃无线秒充2K 低功耗超级阳光屏全等深微曲屏｜小米龙晶玻璃 2.0超声波指纹徕卡光学 Summilux 高速镜头  光影猎人900 高动态主摄｜120mm 徕卡潜望长焦Xiaomi AISP 大模型计算摄影平台 2.0小米星辰通信系统立体声双扬声器｜高动态 4-MIC 阵列"},
        {id:2,name:"Xiaomi 15 定制版",danjia:"4999",instruction:"骁龙8至尊版移动平台徕卡光学Summilux高速镜头  光影猎人900高动态主摄｜60mm徕卡浮动长焦Xiaomi AISP大模型计算摄影平台 2.01.5K 低功耗超级阳光屏｜超窄四等边小米龙晶玻璃3D超声波指纹5400mAh 小米金沙江电池90W 小米澎湃有线秒充｜50W 小米澎湃无线秒充翼型环形冷泵散热系统小米星辰通信系统IP68级防尘防水小米澎湃OS 2"},
        {id:3,name:"Xiaomi 14 Ultra 钛金属特别版",danjia:"8299",instruction:"徕卡全明星四摄徕卡光学 Summilux 镜头小米龙铠架构｜小米龙晶玻璃专业 2K 超视感屏｜全等深微曲屏第三代骁龙®8移动平台｜动态性能调度 4.0LPDDR5X + UFS 4.0 + FBO 焕新存储5300mAh 小米金沙江电池双路环形冷泵散热系统90W 小米澎湃有线秒充80W 小米澎湃无线秒充双向卫星通信立体声双扬声器IP68级防尘防水*"},
        {id:4,name:"Xiaomi MIX Fold 4 16+1T 龙鳞纤维版",danjia:"10999",instruction:"超轻薄四曲机身小米龙骨转轴2.0全碳纤维支撑架构徕卡光学全明星四摄徕卡光学 Summilux 镜头内外一致超清视感屏第三代骁龙®8移动平台5100mAh小米金沙江电池｜DOU1.47天小米澎湃67W有线秒充｜小米澎湃50W无线秒充双向卫星通信IPX8防水"},
        {id:5,name:"Xiaomi SU7 Ultra",danjia:"814900",instruction:"巅峰性能源自对极速的不断追求源自对每个弯道的极限突破更源自对胜利的渴望Xiaomi SU7 Ultra踩下电门，赛道见！"},
        {id:6,name:"Xiaomi MIX Alpha",danjia:"19999",instruction:"探索，让未来多一种可能MIX Alpha 是小米站在 5G时代的起点，设计的一款面向未来的概念手机。这部很未来的手机，承载了小米对于 5G时代很多个方向的探索，实现在一部手机之上。这些不可能的探索，并不是因为它们一定能成为确定的未来，而是希望用探索，让未来多一种可能。"},
    ]
    const obj = reactive({
        id: "",
        name: "",
        danjia: "",
        instruction: "",
    })
    onMounted(() => {
        obj.id = userList[parseInt(props.id) - 1].id
        obj.name = userList[parseInt(props.id) - 1].name
        obj.danjia = userList[parseInt(props.id) - 1].danjia
        obj.instruction = userList[parseInt(props.id) - 1].instruction
    })
    
    const goBack = () => {
        router.go(-1)
    }
</script>

<style scoped>
    .main {
        border: 2px solid #ccc;
        border-radius: 10px;
        height: 500px;
        width: 100%;
        h2 {
            text-align: center; 
        }
        .showDetails {
            display: flex;
            flex-direction: row;
            padding: 20px;
            .show_img {
                flex: 0 1 25%;
            }
            img {
                width: 100%;
                border-radius: 10px;
                outline: 2px solid #ccc;
                outline-offset: 5px;
            }
            .details {
                flex: 0 1 65%;
                margin-left: 10%;
                .contnet {
                    margin: 30px;
                    font-size: 18px;
                }
                .btn_back {
                    width: 100px;
                    height: 40px;
                    font-size: 20px;
                    border-radius: 5px;
                    border: none;
                    background-color: #000;
                    color: #ccc;
                }
                .btn_back:hover {
                    cursor: pointer;
                    background-color: #ccc;
                    color: #111;
                }
            }
        }
    }
</style>