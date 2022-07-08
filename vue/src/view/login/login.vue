<template>
  <div id="head">
    <div id="box">
      <div id="background1" style="clear: both"><img src="@/assets/Images/login_background.jpg" alt="无法显示"></div>
    </div>
    <div id="title">
      <div style="text-align: center"><span style="font-size: 28px; color: white"><b>一路向北</b></span><br></div>
      <div style="text-align: right"><br><span style="font-size: 20px; color: white">——遥感系统</span></div>
    </div>
    <div id="login">
      <form action="http://127.0.0.1:5001/login" method="post" ref="loginForm" :model="loginForm">
        <div id="username">
          <div class="user">
            <div class="user_img"><img src="@/assets/Images/user1.png" alt=""></div>
            <div style="border-radius: 0 10px 10px 0;"><input type="text" placeholder="用户名" name="username" ref="username" v-model="loginForm.username"></div></div>
        </div>
        <div id="password">
          <div class="user">
            <div class="password_img"><img src="@/assets/Images/password.png" alt="无法显示"></div>
            <input type="password" placeholder="密码" name="password" ref="password" v-model="loginForm.password"></div>
          <div id="forget"><a href=""><span>忘记密码?</span></a></div>
        </div>
        <div>
          <div><input type="submit" value="登录" id="login_but" @click="login"></div>
        </div>
        <p class="bottom">
          <span>还没有账号？</span>
          <a style="width: 400px; height: 40px" @click="hrefclick">立即注册</a>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import $ from "jquery";
import store from '@/store/index.js'


export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
        flag: 1
      }
    }
  },
  created: function () {
    document.title = "遥感科技平台登录";

  },
  store: store,
  methods: {
    hrefclick() {
      this.$router.push('/register')
    },
    login() { //已实现，无报错，目标识别功能
      let that = this
      this.$store.commit('setName', that.loginForm.username)
      that.flag = this.$store.state.name
      axios({
        method: "post",
        url: "http://localhost:5001/login",
      }).then(function (response) {
        console.log(response)
        that.$router.push('/login')
        console.log(response.data);
      }).catch((error) => {
        console.log(error)
        alert("请求出现异常")
        that.$message({
          showClose: true,
          message: '请求出现异常！',
          type: 'error'
        })
      })
    },
  },
}
</script>

<style scoped>


* {
  margin: 0;
  padding: 0;

}

#head {
  width: 100%;
  height: 100vh;
  position: absolute;
  /*z-index: -1;*/
}

#box {
  width: 100%;
  height: 100vh;
  position: absolute;
  z-index: -1;
}

#background1 img {
  width: 100%;
  height: 100%;
  position: fixed;
}

#title {
  width: 450px;
  height: 200px;
  margin: 0 auto;
  text-align: center;
  padding: 10%;

}

#login {
  width: 600px;
  height: 300px;
  background: rgba(22, 48, 76, .56);
  /*指定了一个元素的透明度*/
  opacity: 0.9;
  position: absolute;
  padding: 20px;
  left: calc(50% - 300px);
  overflow: hidden;
  top: calc(50% - 80px);
  text-align: center;
  float: left;

}

input {
  width: 400px;
  height: 40px;
  outline: 1px solid #fff;
  border: 0;
  border-radius: 0 10px 10px 0;
  background-color: rgba(22, 48, 76, .56);
  color: white;
  font-size: 17px;

}

#login_but {
  outline: none;
  background-color: #2be1f1;
  border-radius: 10px;

}

.user span {
  width: 40px;
  height: 40px;
  color: white;

}

#login form {
  text-align: center;

}

#username {
  padding-top: 20px;
  padding-bottom: 20px;
  margin-left: 40px;

}

#password {
  padding-bottom: 20px;
  margin-left: 40px;

}

img {
  width: 40px;
  height: 40px;

}

.user_img {
  width: 40px;
  height: 40px;
  border: 1px solid #fff;
  border-radius: 10px 0 0 10px;
  display: block;
  position: absolute;
  top: 39px;
  left: 98px;

}

.password_img {
  width: 40px;
  height: 40px;
  border: 1px solid #fff;
  border-radius: 10px 0 0 10px;
  display: block;
  position: absolute;
  top: 99px;
  left: 98px;

}

#forget {
  width: 80px;
  height: 20px;
  margin-left: 405px;
  margin-top: 5px;
  padding: 0;

}

#forget a {
  color: #adadad;
  font-size: 14px;
  text-decoration: none;

}

.bottom {
  text-align: left;
  margin-left: 100px;
  margin-top: 10px;

}

.bottom span {
  color: #adadad;
  font-size: 16px;

}

.bottom a {
  color: #2be1f1;
  font-size: 16px;
  text-decoration: none;
  cursor: pointer;

}
</style>