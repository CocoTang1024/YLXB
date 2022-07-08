<template>
  <div id="head">
    <layout></layout>
    <div id="content">
      <div class="judge">
        <img src="@/assets/Images/success.png"><span
          style="color: #67C23A">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上传成功</span>
      </div>
      <div class="image">
        <div class="label"><span>Pred</span></div>
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
        <div class="label"><span>Result</span></div>
        <div id="pic3" @mousewheel.prevent="rollImg(index[2])">
          <input class="file" type="file" accept="image/gif, image/jpg, image/png">
          <div class="tip"><span style="color: white">等待识别</span></div>
          <img :src="pic_url" alt="" ref="imgDiv3" class="resimg" @mousedown="move($event,index[2])">
        </div>
      </div>
      <el-progress type="line" :percentage="percentage"></el-progress>
      <button class="test" @click="target()" @mouseover='highlight'>目标提取</button>
    </div>
    <div id="tishi">
      <div id="set">
        <span style="color: white">目标提取，<br>是指单幅或序列图像中感兴趣的目标与背景分割开来，从图像中识别
      和解译有意义的物体实体面提取不同的图像特征的操作</span>
      </div>
    </div>
    <about></about>
  </div>
</template>
<script>
import $ from 'jquery'
import layout from "@/components/common/layout";
import axios from "axios";
import about from "@/components/common/about";

export default {
  name: "target_extraction",
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
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      // console.log(file.url);
      this.dialogVisible = true;
    },
    async uploadFile1(params) {
      const file = params.file;
      let form = new FormData();
      form.append("file", file);
      form.append("target", '3');
      var reader = new FileReader();
      reader.readAsDataURL(file)
      reader.onload = function (e) {
        var base = e.target.result
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
      this.imageUrl = res.data;
    },
    turnToBase64(buffer) {
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
          that.percentage = that.percentage + 10
        }
      }, 1000)
      axios({
        method: "get",
        url: "http://localhost:5000/target_extraction",
        responseType: "arraybuffer", // 最为关键
        params: {"chose": '3'}//我设置的1是目标检测，234分别剩下三个
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
          message: '目标提取成功！',
          type: 'success'
        })
        $('.el-progress').css('opacity', '0')
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
}

.back {
  height: 330px;
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
  /*设置opactity为0，使input变透明*/
  opacity: 0;
  left: 0;
}

.test {
  width: 16%;
  height: 30px;
  outline: none;
  background-color: #2BE1F1;
  cursor: pointer;
  margin-left: 84%;

}

.el-progress {
  width: 32%;
  height: 40px;
  float: left;
  margin-left: 58%;
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