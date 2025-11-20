<template>
    <div class="main">
        <h2>用户详情</h2>
        <div class="showDetails">
            <div class="show_img">
                <img :src="'/src/assets/yh/'+id+'.jpg'" alt="wu">
            </div>
            <div class="details">
                <div class="contnet">编号：{{ obj.id }}</div>
                <div class="contnet">姓名：{{ obj.name }}</div>
                <div class="contnet">职业：{{ obj.job }}</div>
                <div class="contnet">描述：{{ obj.instruction }}</div>
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
        {id: 1, name: '尤雨溪', job: '前端工程师', instruction: "用户累计消费80000.00元"},
        {id: 2, name: '吉多·范罗苏姆', job: '后端工程师', instruction: "python创始人"},
        {id: 3, name: '李腾', job: '化学博士生', instruction: "南昌大学杨维冉课题组成员"},
        {id: 4, name: '王思聪', job: '董事长', instruction: "万北京普思投资有限公司董事长"},
        {id: 5, name: '李维腾', job: '废物一枚', instruction: "真不知道怎么写，他没有可写的"},
        {id: 6, name: '雷军', job: '程序员',instruction:'小米科技创始人，程序员'}
    ]
    const obj = reactive({
        id: "",
        name: "",
        job: "",
        instruction: "",
    })
    onMounted(() => {
        obj.id = userList[parseInt(props.id) - 1].id
        obj.name = userList[parseInt(props.id) - 1].name
        obj.job = userList[parseInt(props.id) - 1].job
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
                width: 80%;
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