<template>
  <div id="head">
    <div id="box">
      <div id="background1" style="clear: both"><img src="@/assets/Images/1.png" alt="无法显示"></div>
    </div>
    <div id="login">
      <p class="top">
        <span style="font-size: 36px; color: #2be1f1; font-weight: 200;"><b>欢迎注册</b></span><br>
        <span style="font-size: 14px; color: gray;">已有账号？</span>
        <a @click="hrefclick" style="width: 400px; height: 40px">立即登录</a>
      </p>
      <form action="http://127.0.0.1:5001/register" method="post">
        <div id="username">
          <div class="user">
            <label class="label">&nbsp;&nbsp;用户名&nbsp;&nbsp;</label>
            <input @blur="judgeusername" name="username" type="text" placeholder="请输入用户名" v-model="username">
          </div>
          <div class="temp">
            <div class="tips1"><span style="color: red">用户名不能为空</span></div>
          </div>
        </div>
        <div id="email">
          <div class="user"><label class="label">&nbsp;邮&nbsp;&nbsp;&nbsp;&nbsp;箱&nbsp;&nbsp;</label>
            <input @blur="judgeemail" name="email" type="text" placeholder="请输入邮箱" v-model="email"></div>
          <div class="temp">
            <div class="tips2"><span style="color: red;font-size: 12px">{{ emailtips }}</span></div>
          </div>
        </div>
        <div id="password">
          <div class="user"><label class="label">&nbsp;密&nbsp;&nbsp;&nbsp;&nbsp;码&nbsp;&nbsp;</label>
            <input @blur="judgepassword" name="password" type="password" placeholder="请输入密码" v-model="password"></div>
          <div class="temp">
            <div class="tips3"><span style="color: red">{{ passwordtips }}</span></div>
          </div>
        </div>
        <div id="repassword">
          <div class="user">
            <label class="label">确认密码</label>
            <input @blur="judgerepassword" name="repassword" type="password" placeholder="请输入确认密码" v-model="repassword">
            <div class="temp">
              <div class="tips4"><span style="color: red">{{ repasswordtips }}</span></div>
            </div>
          </div>
        </div>
        <div id="register">
          <input type="submit" value="注册" id="login_but" @click="register">
        </div>
      </form>

    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import axios from "axios";

export default {
  name: "register",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      repassword: "",
      emailtips: '',
      passwordtips: '',
      repasswordtips: ''
    }
  },
  created: function () {
    document.title = "遥感科技平台";
  },
  methods: {
    hrefclick() {
      this.$router.push('/login')
    },
    judgeusername() {
      if (this.username === "") {
        $('.tips1').css("display", 'block')
      } else {
        $('.tips1').css("display", 'none')
      }
    },
    judgeemail() {
      if (this.email === "") {
        this.emailtips = "邮箱不能为空"
        $('.tips2').css("display", 'block')
      } else if (this.email.indexOf("@") === -1) {
        this.emailtips = "请输入正确的邮箱地址"
        $('.tips2').css("display", 'block')
      } else {
        $('.tips2').css("display", 'none')
      }
    },
    judgepassword() {
      if (this.password === "") {
        this.passwordtips = "密码不能为空"
        $('.tips3').css("display", 'block')
      } else if (this.password.length < 8 || this.password.length > 15) {
        this.passwordtips = "密码长度为8~15个字符"
        $('.tips3').css("display", 'block')
      } else {
        $('.tips3').css("display", 'none')
      }
    },
    judgerepassword() {
      if (this.repassword === "") {
        this.repasswordtips = "请再次输入密码"
        $('.tips4').css("display", 'block')
      } else if (this.password !== this.repassword) {
        this.repasswordtips = "两次输入密码不一致！"
        $('.tips4').css("display", 'block')
      } else {
        $('.tips4').css("display", 'none')
      }
    },
    register() {
      if (this.password !== this.repassword) {
        alert('两次密码不一致，请重新输入')
        return false
      } else {
        // alert('注册成功')
        let that = this;
        axios({
          method: "post",
          url: "http://localhost:5001/register",
        }).then(function (response) {
          console.log(response)
        });
        return true
      }
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

#login {
  width: 600px;
  height: 455px;
  background: rgba(22, 48, 76, .56);
  /*指定了一个元素的透明度*/
  opacity: 0.9;
  position: relative;
  padding: 20px;
  left: calc(50% - 300px);
  overflow: hidden;
  top: calc(50% - 225px);
  text-align: center;
  float: left;
}

.temp {
  width: 200px;
  height: 20px;
  position: relative;
  left: 130px;
  background-color: #14294C;
  border: #14294C;
}

.tips1, .tips2, .tips3, .tips4 {
  width: 200px;
  height: 20px;
  border: #14294C;
  position: relative;
  text-align: left;
  display: none;
}

input {
  width: 400px;
  height: 40px;
  outline: 1px solid #fff;
  border: 0;
  border-radius: 10px;
  background-color: rgba(22, 48, 76, .56);
  color: white;
  font-size: 17px;
}

#login_but {
  outline: none;
  background-color: #2be1f1;
  border-radius: 10px;

}

.label {
  color: white;
  font-size: 16px;
  letter-spacing: 0;
  text-align: right;
  width: 80px;
  height: 40px;
  line-height: 60px;
  margin-right: 15px;
  font-weight: 200;
  border: 1px red;
}

#login form {
  text-align: center;
}

#username {
  padding-top: 20px;
  margin-left: 40px;
}

#email, #password, #repassword {
  margin-left: 40px;
}

#register {
  margin: 7px auto 0;
  position: relative;
  left: 23px;
}

.top a {
  color: #2d8cf0;
  font-size: 16px;
  text-decoration: none;
  cursor: pointer;
}
</style>