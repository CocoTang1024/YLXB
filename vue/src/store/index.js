import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        name: JSON.parse(sessionStorage.getItem("COMPANY_AUTH_INFO")) || {}
    },
    getters: {
        getName(state) {
            return state.name //返回目 前城市名称
        }
    },
    mutations: {
        setName(state, data) {
            state.name = data;
            sessionStorage.setItem("COMPANY_AUTH_INFO", JSON.stringify(data))
        }
    },
})

