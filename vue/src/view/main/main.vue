<template>
  <div id="head">
    <layout></layout>
    <div id="content">
      <div class="wrap">
        <div class="slide">
          <img src="@/assets/Images/4.png" alt="无法显示" @mouseleave="changeInterval(false)"
               @mouseover="changeInterval(true)">
        </div>
        <div class="slide">
          <img src="@/assets/Images/5.png" alt="无法显示" @mouseleave="changeInterval(false)"
               @mouseover="changeInterval(true)">
        </div>
        <div class="slide">
          <img src="@/assets/Images/6.png" alt="无法显示" @mouseleave="changeInterval(false)"
               @mouseover="changeInterval(true)">
        </div>
        <div class="slide">
          <img src="@/assets/Images/7.png" alt="无法显示" @mouseleave="changeInterval(false)"
               @mouseover="changeInterval(true)">
        </div>
        <div class="slide">
          <img src="@/assets/Images/2.png" alt="无法显示" @mouseleave="changeInterval(false)"
               @mouseover="changeInterval(true)">
        </div>
      </div>
      <div class="prev" @click="prev('left')"><img src="@/assets/Images/icon-slides1.png" alt=""></div>
      <div class="next" @click="prev('right')"><img src="@/assets/Images/icon-slides2.png" alt=""></div>
    </div>
    <div id="tishi">
      <div><span style="color: white">欢迎来到遥感卫星解译平台，点击左侧功能菜单按钮开始体验吧！</span></div>
    </div>
    <about></about>
  </div>
</template>
<script>
import $ from 'jquery'
import layout from '@/components/common/layout'
import about from "@/components/common/about";

export default {
  name: "Main",
  data() {
    return {
      nowindex: 0,
      timer: null
    }
  },
  mounted() {
      this.startInterval()
      let arrowsup = document.getElementsByClassName('arrowsup')[0]
      arrowsup.style.display = 'none'
      let arrowsdown = document.getElementsByClassName('arrowsdown')[0]
      arrowsdown.style.display = 'block'
      let fun = document.getElementsByClassName('function')
      for (let i = 0; i < 4; i++)
      fun[i].style.display = 'none'
  },
  methods: {
    startInterval() {
      // 事件里定时器应该先清除在设置，防止多次点击直接生成多个定时器
      clearInterval(this.timer);
      this.timer = setInterval(() => {
        this.nowindex++;
        if (this.nowindex > 5) {
          this.nowindex = 1
        }
        function changeSlide(index) {
          //所有图片淡出
          $('.wrap .slide').fadeOut()
          $('.wrap .slide').eq(index - 1).fadeIn()
        }
        changeSlide(this.nowindex)
      }, 3000)
    },
    prev(val) {
      if (val === 'left') {
        this.nowindex--
        if (this.nowindex < 1) {
          this.nowindex = 5;
        }
      } else {
        this.nowindex++
        if (this.nowindex > 5) {
          this.nowindex = 1;
        }
      }
      function changeSlide(index) {
        //所有图片淡出
        $('.wrap .slide').fadeOut()
        $('.wrap .slide').eq(index - 1).fadeIn()
      }

      changeSlide(this.nowindex)
    },
    //鼠标移入移出控制
    changeInterval(val) {
      if (val) {
        clearInterval(this.timer)
      } else {
        this.startInterval()
      }
    },
  },
  created: function () {
    document.title = "遥感科技平台";
  },
  components: {
    layout,
    about
  }
}


</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.wrap {
  position: relative;
}

.wrap .slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 400px;
}

.wrap .slide img {
  width: 100%;
  height: 400px;
}

.prev {
  position: absolute;
  top: 50%;
  transform: translateY(-35px);
  height: 69px;
  width: 40px;
  left: -8px;
  opacity: 0.5;
}

.prev:hover {
  background-position: 0 0;
}

.next {
  position: absolute;
  top: 50%;
  /*便宜固定距离*/
  transform: translateY(-35px);
  height: 69px;
  width: 35px;
  right: 0;
  opacity: 0.5;
}

.next:hover {
  background-position: -42px 0;
}

#head {
  width: 100%;
  height: 100vh;
  position: absolute;
  /*z-index: -1;*/
}

#content {
  border: 1px red solid;
  width: calc(100% - 600px);
  text-align: center;
  margin: auto;
  height: 400px;
  position: absolute;
  float: left;
  left: 320px;
  top: calc(50vh - 200px);
  /*padding: 30px;*/
}

#content span {
  color: white;
  font-size: 30px;
}

#tishi {
  width: 250px;
  height: 400px;
  margin: auto;
  position: absolute;
  border: 2px #2be1f1 solid;
  top: calc(50vh - 200px);
  right: 10px;
}

#tishi div {
  width: 80%;
  margin-top: 50%;
  margin-left: 10%;
  text-align: center;
  font: 20px '微软雅黑 Light';
  letter-spacing: 2px;
  font-style: oblique;
}

</style>