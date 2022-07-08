import Vue from 'vue'
import App from './App.vue'
import router from './router'
import $ from 'jquery'
import 'element-ui/lib/theme-chalk/index.css'
import element from './element/index'
import store from './store/index'

Vue.use(element)

Vue.config.productionTip = false

new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
