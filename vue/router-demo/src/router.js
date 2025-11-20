/*
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-12-17 22:47:34
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-12-19 12:50:59
 * @FilePath: \router-demo\src\router.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
// 1、引入路由、设置路由模式
import { createRouter,createWebHistory } from "vue-router";

// 2、创建路由对象
const router = createRouter({
    // 配置路由模式
    history:createWebHistory(),

    // 设置路由对象的路径
    routes:[
        {
            path:"/",
            redirect:"/home",
        },
        {
            path:"/login",
            component:()=>import('./components/Login.vue'),
         },
        {
            path:"/home",
            component:()=>import('./components/Home.vue'),
            redirect:"/home/users",
            //redirect:"/home",
            children:[
            {
                path:"users",
                component:()=>import('./components/zi/zujian/yonghu.vue'),
            },
            {
                path:"rights",
                component:()=>import('./components/zi/zujian/quanxian.vue'),
            },
            {
                path:"goods",
                component:()=>import('./components/zi/zujian/shangping.vue'),
            },
            {
                path:"orders",
                component:()=>import('./components/zi/zujian/dingdan.vue'),
            },
            /*{
                path:"setting",
                component:()=>import('./components/zi/zujian/shezhi.vue'),
            },*/
            {
                path:"users_details/:id",
                component:()=>import('./components/zi/zujian/yonghushuji.vue'),props:true
            },
            {
                path:"goods_details/:id",
                component:()=>import('./components/zi/zujian/shangpingxiangqing.vue'),props:true
            },
        ]
        }
    ]
})

// 3、导出路由对象
export default router