import Vue from 'vue'
import VueRouter from 'vue-router'
import login from "@/view/login/login";
import main from "@/view/main/main";
import register from "@/view/register/register";
import change_detection from "@/view/change_detection/change_detection";
import target_detection from "@/view/target_detection/target_detection";
import target_extraction from "@/view/target_extraction/target_extraction";
import terrain_classification from "@/view/terrain_classification/terrain_classification";

// 1.通过Vue.use(插件)，安装插件
Vue.use(VueRouter)

// 2.创建VueRouter对象
const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/main',
        component: main
    },
    {
        path: '/login',
        component: login
    },
    {
        path: '/register',
        component: register
    },
    {
        path: '/change_detection',
        component: change_detection
    },
    {
        path: '/target_detection',
        component: target_detection
    },
    {
        path: '/target_extraction',
        component: target_extraction
    },
    {
        path: '/terrain_classification',
        component: terrain_classification
    },

]

const router = new VueRouter({
    // 配置路由和组件之间的应用关系
    routes,
    mode: 'history'
})

export default router
