<template>
  <div id="subject">
    <div id="box">
      <div id="background1" style="clear: both"><img src="@/assets/Images/3.jpg" alt="无法显示"></div>
    </div>
    <div id="title">
      <div id="time"><span style="color: white">{{ nowDate }}</span></div>
      <div class="font"><span style="font-size: 28px; color: white"><b>遥感科技书写星空理想</b></span></div>
      <div class="user">
        <div id="userimg" @click="homepage" @mouseover="hide"><img src="@/assets/Images/donghua.gif"></div>
        <div class="userinfo">
          <span style="color: white" v-if="name !==''">
            <p>用户：{{ Name }}</p><br>
            <button id="btn" style="color: white" @mouseover='border' @click="logout">注销</button>
          </span>
        </div>
      </div>
      <div id="website"><a href="https://www.paddlepaddle.org.cn/">飞浆官网</a></div>
      <br>
    </div>
    <div id="Function">
      <div id="meau"><span>功能菜单</span></div>
      <div class="arrowsup"><img src="@/assets/Images/up.png" alt="无法显示" @click="btnup"></div>
      <div class="arrowsdown"><img src="@/assets/Images/down.png" alt="无法显示" @click="btndown"></div>
      <div class="function" @mouseover='highlight' @click="change_detection">
        <img src="@/assets/Images/build.png" alt="" class="icons"><span>变化检测</span>
      </div>
      <div class="function" @mouseover='highlight' @click="target_detection">
        <img src="@/assets/Images/detect.png" alt="" class="icons"><span>目标检测</span>
      </div>
      <div class="function" @mouseover='highlight' @click="target_extraction">
        <img src="@/assets/Images/extract.png" alt="" class="icons"><span>目标提取</span>
      </div>
      <div class="function" @mouseover='highlight' @click="terrain_classification">
        <img src="@/assets/Images/classify.png" alt="" class="icons"><span>地物分类</span>
      </div>
    </div>
  </div>

</template>

<script>
import $ from "jquery";
import store from '@/store/index.js'

export default {
  name: "layout",
  data() {
    return {
      name: "1",
      nowDate: "", // 当前日期
    };
  },
  store: store,
  methods: {
    currentTime() {
      setInterval(this.formatDate, 500);
    },
    formatDate() {
      let date = new Date();
      let year = date.getFullYear(); // 年
      let month = date.getMonth() + 1; // 月
      let day = date.getDate(); // 日
      let week = date.getDay(); // 星期
      let weekArr = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
      let hour = date.getHours(); // 时
      hour = hour < 10 ? "0" + hour : hour; // 如果只有一位，则前面补零
      let minute = date.getMinutes(); // 分
      minute = minute < 10 ? "0" + minute : minute; // 如果只有一位，则前面补零
      let second = date.getSeconds(); // 秒
      second = second < 10 ? "0" + second : second; // 如果只有一位，则前面补零
      this.nowDate = `${year}/${month}/${day} ${hour}:${minute}:${second} ${weekArr[week]}`;
    },
    homepage() {
      this.$router.replace('/main')
    },
    btnup() {
      $(`.arrowsup`).click(function (event) {
        $(`.function`).slideUp()
        $(`.arrowsdown`).show()
        $(`.arrowsup`).hide()
        event.stopPropagation();
      })
    },
    btndown() {
      $(`.arrowsdown`).click(function (event) {
        $(`.function`).slideDown()
        $(".arrowsdown").hide()
        $(`.arrowsup`).show()
        event.stopPropagation();
      })
    },
    border() {
      $('#btn')[0].onmouseover = function () {
        $('#btn')[0].style.border = '1px solid #48AFDC'
      }
      $('#btn')[0].onmouseout = function () {
        $('#btn')[0].style.border = '1px solid #5A636B'
      }
    },
    logout() {
      this.$router.replace('/login')
    },
    highlight() {
      for (let i = 0; i < 4; i++) {
        $('.function')[i].onmouseover = function () {
          $('.function')[i].style.backgroundColor = '#015C74'
        }
        $('.function')[i].onmouseout = function () {
          $('.function')[i].style.backgroundColor = ''
        }
      }
    },
    hide() {
      $('.user')[0].onmouseover = function () {
        $('.userinfo')[0].style.display = 'block'
      }
      $('.user')[0].onmouseout = function () {
        $('.userinfo')[0].style.display = 'none'
      }
    },
    change_detection() {
      this.$router.replace('/change_detection')
    },
    target_detection() {
      // $('#content').empty()
      this.$router.replace('/target_detection')
    },
    target_extraction() {
      // $('#content').empty()
      this.$router.replace('/target_extraction')
    },
    terrain_classification() {
      // $('#content').empty()
      this.$router.replace('/terrain_classification')
    },
  },
  computed: {
    Name() {
      return this.$store.state.name
    }
  },
  mounted() {
    this.name = this.$store.getters.getName

    this.currentTime();
  },
  // 销毁定时器
  beforeDestroy() {
    if (this.formatDate) {
      clearInterval(this.formatDate); // 在Vue实例销毁前，清除时间定时器
    }
  },


}
</script>

<style scoped>
#box {
  width: 100%;
  height: 100vh;
  position: absolute;
  z-index: -1;
}

#subject {
  width: 100%;
  height: 100%;
}

#background1 {
  width: 100%;
  height: inherit;
  margin: 0 auto;
  top: 0;
  left: 0;
  background-size: cover;
  background: no-repeat 50%;
}

#background1 img {
  width: 100%;
  height: 100%;
  position: fixed;
}

#title {
  margin: 0 auto;
  text-align: center;
  padding-top: 10px;
  height: 50px;
  position: relative;
}

#time {
  float: left;
  margin: 0 10px;
}

.font {
  width: 500px;
  height: 40px;
  left: calc(50% - 260px);
  margin: 0;
  position: absolute;
}

#title img {
  width: 40px;
  height: 40px;
}

.user {
  /*border: 1px red solid;*/
  width: 152px;
  height: 40px;
  margin: 0;
  position: absolute;
  right: 5px;
}

#userimg {
  float: right;
  margin: 0px 5px;
  cursor: pointer;
}

.userinfo {
  float: right;
  overflow: hidden;
  width: 100px;
  height: 85px;
  border: 1px solid #2A314A;
  border-radius: 10px;
  display: none;
  background-color: #041220;
}

.userinfo button {
  background-color: #041220;
  border: 1px solid #5A636B;
  width: 60px;
  height: 30px;
  border-radius: 5px;
  cursor: pointer;
}

#website {
  float: right;
  margin-right: 30px;
  margin-top: 8px;
  position: absolute;
  top: 10px;
  /*margin-top: 10px;*/
  right: 140px;
}

#website a {
  text-decoration: none;
  color: white;
  font-size: 15px;
}

#Function {
  width: 250px;
  height: calc(100vh - 170px);
  border: 5px #05B2ED solid;
  padding: 20px;
  position: relative;
}

#meau {
  border: 1px solid #2be1f1;
  width: 200px;
  height: 30px;
  text-align: center;
  border-radius: 10px;
  margin: auto;
  padding: 2px 5px;
  float: left;
}

.arrowsup {
  width: 30px;
  height: 30px;
  position: absolute;
  top: 20px;
  left: 250px;
  display: block;
}

.arrowsdown {
  width: 30px;
  height: 30px;
  position: absolute;
  top: 20px;
  left: 250px;
  display: none;
}

#Function img {
  width: 30px;
  height: 30px;
  cursor: pointer;
}

#Function span {
  color: #fff;
  font-size: 20px;
}

.function {
  border: 1px solid #2be1f1;
  width: 150px;
  height: 30px;
  text-align: center;
  padding: 2px 5px;
  margin: calc(20vh - 63px) auto 0px;
  display: block;
  cursor: pointer;
}

.icons {
  position: absolute;
  left: 65px;
}

.function span {
  color: #2be1f1;
}
</style>