<template>
  <div id="head">
    <layout></layout>
    <div id="content">
      <div class="judge">
        <img src="@/assets/Images/success.png"><span
          style="color: #67C23A">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上传成功</span>
      </div>
      <div class="image">
        <div class="label"><span>Image 1</span></div>
        <el-upload
            id="pic1"
            action=""
            list-type="none"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :auto-upload="true"
            :http-request="uploadFile1"
        >
          <img src="@/assets/Images/add.png" class="back" ref="imgDiv1">
        </el-upload>
        <img src="" alt="" class="img" >
      </div>
      <div class="image">
        <div class="label"><span>Detection</span></div>
        <div id="pic3" @mousewheel.prevent="rollImg(index[2])">
          <input class="file" type="file" accept="image/gif, image/jpg, image/png" >
          <div class="tip">
            <span style="color: white">等待识别...</span>
          </div>
          <img :src="pic_url" alt="" ref="imgDiv3" class="resimg" @mousedown="move($event,index[2])">
        </div>
      </div>

      <el-progress type="line" :percentage="percentage"></el-progress>
      <div class="coorbtn" @click="btn">
        <button>获取坐标</button>
      </div>
        <div class="funbtn">
          <button class="test" @click="target()" @mouseover='highlight'>目标检测</button>
        </div>
    </div>
    <div id="tishi">
      <div id="set">
        <span style="color:white">目标检测，<br>是一种基于目标几何和统计特征的图像分割。他将目标的分割与识别合二为一。</span>
        <div class="bar">
          <progressbar :min='0' :max='100' v-model="per" @inputchange="printit"></progressbar>
          <span style="color:white">左上角坐标:({{ a }},{{ b }})<br>右下角坐标:({{ c }},{{ d }})</span>
        </div>
      </div>
    </div>
    <about></about>
  </div>
</template>
<script>
import $ from 'jquery'
import layout from "@/components/common/layout";
import progressbar from "@/components/common/progressbar";
import axios from "axios";
import about from "@/components/common/about";

export default {
  name: "target_detection",
  data() {
    return {
      index: [1, 2, 3],
      msg: "",
      dialogImageUrl: '',
      dialogVisible: false,
      imageUrl: "",
      pic_url: '',
      it: '50',
      percentage:0,
      a:"",
      b:'',
      c:'',
      d:''
    }
  },
  methods: {
    printit(it) {
      this.it = it
      console.log('this.it=', this.it)
    },
    //显示paddlers的函数，可以当作请求模版
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    //element组件的相关函数
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      // console.log(file.url);
      this.dialogVisible = true;
    },
    async uploadFile1(params) {
      const file = params.file;
      let form = new FormData();
      form.append("file", file);
      form.append("target", '2');
      var reader = new FileReader();
      reader.readAsDataURL(file)
      reader.onload = function (e) {
        var base = e.target.result
        console.log(2222, e)
        let img = document.getElementsByClassName('img')[0]
        img.setAttribute('style', 'z-index:1')
        img.src = base
        form.append("src", img.src);
        console.log('pic1')
        document.getElementById('pic1').appendChild(img)
        $('.el-upload-list').remove()
        this.msg = "上传成功"
        setTimeout(function () {
          $('.judge').slideDown()
        })
        setTimeout(function () {
          $('.judge').slideUp()
        }, 2000)
      }
      const res = await axios.post("http://127.0.0.1:5000/pic_3", form);
      console.log("res1=", res);
      this.imageUrl = res.data;//这里解决了一个跨域问题
    },
    turnToBase64(buffer) {
      //第一步，将ArrayBuffer转为二进制字符串
      let binary = "";
      let bytes = new Uint8Array(buffer);
      let len = bytes.byteLength;
      for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
      }
      return window.btoa(binary);
    },
    target() {
      let that = this;
      $('.el-progress').css('opacity','1')
      setInterval( ()=> {
        if(that.percentage!==100){
          that.percentage=that.percentage+10
        }
      },1000)
      axios({
        method: "get",
        url: "http://localhost:5000/target_detection",
        responseType: "arraybuffer", // 最为关键
        params: {"chose": '2', 'per': that.it}//我设置的1是目标检测，234分别剩下三个
      }).then(function (response) {
        if ($('.tip').css('opacity') === 1) {
          $('.tip').css('opacity', '0')
        }
        let img = document.getElementsByClassName('resimg')[0]
        img.setAttribute('style', 'z-index:1')
        that.pic_url =
            "data:image/jpeg;base64," + that.turnToBase64(response.data);
        that.percentage=100
        console.log(response)
        that.$message({
          showClose: true,
          message: '目标检测成功！',
          type: 'success'
        })
        $('.el-progress').css('opacity','0')
      });
    },
    highlight() {
      $('.test')[0].onmouseover = function () {
        $('.test')[0].style.backgroundColor = '#05B2ED'
      }
      $('.test')[0].onmouseout = function () {
        $('.test')[0].style.backgroundColor = '#2BE1F1'
      }
    },
    async btn() {
      let that=this
      const res = await axios.post("http://127.0.0.1:5000/coor");
      let list =  (res.data).split(',')
      that.a = list[0].slice(0,5)
      that.b = list[1].slice(0,5)
      that.c = list[2].slice(0,5)
      that.d = list[3].slice(0,5)
      console.log(res);
    },
    move(e, index) {
      e.preventDefault();
      // 获取元素
      console.log("#pic" + index);
      console.log(e)
      let left = document.querySelector("#pic" + index);
      let img = document.querySelectorAll(".resimg")[0];
      // console.log(img);
      let x = e.pageX - img.offsetLeft;
      let y = e.pageY - img.offsetTop;
      // 添加鼠标移动事件
      left.addEventListener("mousemove", move);

      function move(e) {
        img.style.left = e.pageX - x + "px";
        img.style.top = e.pageY - y + "px";
      }

      // 添加鼠标抬起事件，鼠标抬起，将事件移除
      img.addEventListener("mouseup", function () {
        left.removeEventListener("mousemove", move);
      });
      // 鼠标离开父级元素，把事件移除
      left.addEventListener("mouseout", function () {
        left.removeEventListener("mousemove", move);
      });
    },
    rollImg(index) {
      /* 获取当前页面的缩放比 若未设置zoom缩放比，则为默认100%，即1，原图大小 */
      let tref = 'this.$refs.imgDiv' + index
      tref = eval(tref)
      var zoom = parseInt(tref.style.zoom) || 100;
      // var zoom = parseInt(this.$refs.imgDiv1.style.zoom) || 100;
      /* event.wheelDelta 获取滚轮滚动值并将滚动值叠加给缩放比zoom wheelDelta统一为±120，其中正数表示为向上滚动，负数表示向下滚动 */

      zoom += event.wheelDelta / 12;
      /* 最小范围 和 最大范围 的图片缩放尺度 */

      if (zoom >= 80 && zoom < 500) {
        // this.$refs.imgDiv1.style.zoom = zoom + "%";
        tref.style.zoom = zoom + "%";
      }
      return false;
    }
  },
  created: function () {
    document.title = "遥感科技平台";

  },
  mounted() {

  },
  computed: {
    per: {
      get() {
        return 0;
      },
      set(val) {
        console.log(val);
      },
    },
  },
  components: {
    layout,
    progressbar,
    about
  }
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

#content {
  border: 1px #2be1f1 solid;
  width: calc(100% - 600px);
  margin: auto;
  height: 400px;
  position: absolute;
  float: left;
  left: 318px;
  top: calc(50vh - 200px);
}


.judge {
  width: 33%;
  height: 43px;
  left: 34%;
  margin: auto;
  position: absolute;
  float: left;
  background-color: #F0F9EB;
  font-size: 15px;
  border-radius: 5px;
  display: none;
}

.judge img {
  width: 15px;
  height: 15px;
  margin-top: 13px;
  margin-left: 13px;
}

.image {
  border: 1px deepskyblue solid;
  width: 42%;
  height: 370px;
  margin: 15px 0 15px 5%;
  float: left;
  text-align: center;
}

.label {
  border-bottom: 1px white solid;
  width: 100%;
  height: 30px;
}

.label span {
  font-size: 20px;
  color: white;
}

#pic1, #pic3 {
  height: 340px;
  width: 100%;
  position: relative;
  float: left;
  overflow: hidden;
  text-align: center;
}


#pic3 div {
  height: 50px;
  width: 50%;
  margin: 135px auto;
  text-align: center;

}

.back {
  height: 340px;
  width: 100%;

}

.img {
  width: 100%;
  height: 100%;
  float: left;
  z-index: -2;
  position: absolute;
  left: 0;
  top: 0;
}

.resimg {
  width: 340px;
  height: 340px;
  float: left;
  z-index: -2;
  position: absolute;
  left: calc(50% - 170px);
  top: 0;
}

.image input {
  position: absolute;
  height: 340px;
  width: 100%;
  opacity: 0;
  left: 0;
}

.test {
  cursor: pointer;
}
.coorbtn {
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 9%;
  /*margin-top: 442px;*/
  text-align: center;
  /*position: absolute;*/
}
.funbtn {
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 17%;
  text-align: center;
}
.coorbtn button {
  width: 50%;
  height: 30px;
  outline: none;
  background-color: #05B2ED;
  cursor: pointer;

}
.funbtn button {
  width: 50%;
  height: 30px;
  outline: none;
  background-color: #2BE1F1;

}
.el-progress{
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 58%;
  text-align: center;
  opacity:0;
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

#set {
  width: 80%;
  margin-top: 35%;
  margin-left: 10%;
  text-align: center;
  font-size: 20px;
}


</style>