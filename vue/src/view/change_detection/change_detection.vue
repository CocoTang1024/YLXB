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
        <img src="" alt="" class="img">
      </div>
      <div class="image">
        <div class="label"><span>Image 2</span></div>
        <el-upload
            id="pic2"
            action=""
            list-type="none"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :auto-upload="true"
            :http-request="uploadFile2"
        >
          <img src="@/assets/Images/add.png" class="back" ref="imgDiv2">
        </el-upload>
        <img src="" alt="" class="img">
      </div>
      <div class="image">
        <div class="label"><span>Ground truth</span></div>
        <div id="pic3" @mousewheel.prevent="rollImg(index[2])">
          <input class="file" type="file" accept="image/gif, image/jpg, image/png">
          <div class="tip" style="opacity: 1"><span style="color: white">等待识别...</span></div>
          <img :src="pic_url" alt="无法显示" ref="imgDiv3" class="resimg" @mousedown="move($event,index[2])">
        </div>
      </div>
      <!--      <div class="upfile" @click="clearimg('1')">-->
      <!--        <button>重新上传</button>-->
      <!--      </div>-->
      <!--      <div class="upfile" @click="clearimg('2')">-->
      <!--        <button>重新上传</button>-->
      <!--      </div>-->
      <el-progress type="line" :percentage="percentage"></el-progress>
      <button class="test" @click="target()" @mouseover='highlight'>开始检测</button>
    </div>
    <div id="tishi">
      <div id="set">
        <span style="color: white">变化检测，<br>是指利用已有两张不同时间拍摄的相同位置的遥感图像训练数据，实现对多时相图像中的建筑变化检测。</span>
      </div>
    </div>
    <about></about>
  </div>
</template>
<script>
import $ from 'jquery'
import layout from '@/components/common/layout'
import about from "@/components/common/about";
import axios from "axios";

export default {
  name: "change_detection",
  data() {
    return {
      index: [1, 2, 3],
      msg: "",
      dialogImageUrl: '',
      dialogVisible: false,
      imageUrl: "",
      pic_url: '',
      percentage: 0,
    }
  },
  created: function () {
    document.title = "遥感科技平台";
  },
  methods: {

    //显示paddlers的函数，可以当作请求模版
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    //element组件的相关函数
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    async uploadFile1(params) {
      const file = params.file;
      let form = new FormData();
      form.append("file", file);
      form.append("target", '1');
      console.log(params);
      var reader = new FileReader();
      reader.readAsDataURL(file)
      reader.onload = function (e) {
        var base = e.target.result
        let img = document.getElementsByClassName('img')[0]
        img.setAttribute('style', 'z-index:1')
        img.src = base
        form.append("src", img.src);
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
      const res = await axios.post("http://127.0.0.1:5000/pic", form);
      console.log("res1=", res);
      this.imageUrl = res.data;//这里解决了一个跨域问题
    },
    async uploadFile2(params) {
      const file = params.file;
      let form = new FormData();
      form.append("file", file);
      form.append("target", '1');
      console.log(params);
      var reader = new FileReader();
      reader.readAsDataURL(file)
      reader.onload = function (e) {
        var base = e.target.result
        let img = document.getElementsByClassName('img')[1]
        img.setAttribute('style', 'z-index:1')
        img.src = base
        document.getElementById('pic2').appendChild(img)
        $('.el-upload-list').remove()
        this.msg = "上传成功"
        setTimeout(function () {
          $('.judge').slideDown()
        })
        setTimeout(function () {
          $('.judge').slideUp()
        }, 2000)
      }
      const res = await axios.post("http://127.0.0.1:5000/pic", form);
      console.log('res2=', res);
      //解决一个跨域问题
      this.imageUrl = res.data;
    },
    turnToBase64(buffer) {
      //第一步，将ArrayBuffer转为二进制字符串
      let binary = "";
      let bytes = new Uint8Array(buffer);
      let len = bytes.byteLength;
      for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
      }
      //将二进制字符串转为base64字符串
      return window.btoa(binary);
    },
    target() {
      let that = this;
      $('.el-progress').css('opacity', '1')
      setInterval(() => {
        if (that.percentage !== 100) {
          that.percentage = that.percentage + 5
        }
      }, 1000)
      axios({
        method: "get",
        url: "http://localhost:5000/change_detection",
        responseType: "arraybuffer",
        params: {"chose": '1'}//设置1代表目标检测
      }).then(function (response) {
        if ($('.tip').css('opacity') === 1) {
          $('.tip').css('opacity', '0')
        }
        let img = document.getElementsByClassName('resimg')[0]
        img.setAttribute('style', 'z-index:1')
        that.pic_url =
            "data:image/jpeg;base64," + that.turnToBase64(response.data);
        that.percentage = 100
        console.log(response)
        that.$message({
          showClose: true,
          message: '图片检测成功！',
          type: 'success'
        })
        $('.el-progress').css('opacity', '0')
      });
    },
    // // 通过input上传图片
    // clearimg(index) {
    //   let img = document.getElementsByClassName('img')
    //   if (index === '1') {
    //     img[0].src = ""
    //     img[0].setAttribute('style', 'z-index:-2')
    //   } else {
    //     img[1].src = ""
    //     img[1].setAttribute('style', 'z-index:-2')
    //   }
    // },
    highlight() {
      $('.test')[0].onmouseover = function () {
        $('.test')[0].style.backgroundColor = '#05B2ED'
      }
      $('.test')[0].onmouseout = function () {
        $('.test')[0].style.backgroundColor = '#2BE1F1'
      }
    },
    move(e, index) {
      // 取消目标元素的默认行为，防止异常
      e.preventDefault();
      // 获取元素
      let left = document.querySelector("#pic" + index);
      let img = document.querySelectorAll(".resimg")[0];
      // console.log(img);
      // 鼠标在页面上的位置-距离父辈元素左边缘的距离
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
      /* event.wheelDelta 获取滚轮滚动值并将滚动值叠加给缩放比zoom wheelDelta统一为±120，其中正数表示为向上滚动，负数表示向下滚动 */

      zoom += event.wheelDelta / 12;
      /* 最小范围 和 最大范围 的图片缩放尺度 */

      if (zoom >= 80 && zoom < 500) {
        tref.style.zoom = zoom + "%";
      }
      return false;
    },

  },
  components: {
    layout,
    about
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
  height: 100%;
  position: absolute;
  /*z-index: -1;*/
}

#content {
  border: 1px #2be1f1 solid;
  width: calc(100% - 600px);
  margin: auto;
  height: 400px;
  position: absolute;
  /*float: left;*/
  left: 318px;
  top: calc(50vh - 200px);
}

.upfile {
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 1%;
  text-align: center;
}

.upfile button {
  width: 50%;
  height: 30px;
  outline: none;
  background-color: #05B2ED;

}

.test {
  width: 16%;
  height: 30px;
  outline: none;
  background-color: #2BE1F1;
  cursor: pointer;
  margin-left: 84%;

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
  width: 32%;
  height: 320px;
  margin: 45px 0 0px 0.8%;
  float: left;
  /*z-index: 1;*/
  position: relative;
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

#pic1, #pic2, #pic3 {
  height: 290px;
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
}

.back {
  height: 285px;
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
  width: 285px;
  height: 285px;
  float: left;
  z-index: -2;
  position: absolute;
  left: 0;
  top: 0;
}

.image input {
  position: absolute;
  height: 300px;
  width: 100%;
  opacity: 0;
  left: 0;
}

.el-progress {
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 68%;
  text-align: center;
  opacity: 0;
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