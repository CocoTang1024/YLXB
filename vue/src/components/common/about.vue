<template>
  <div>
    <div class="about">
      <div class="help" @click="handleClose" @mouseover="about"><img src="@/assets/Images/about.png"></div>
      <div class="text"><span style="color: white;font-size: 14px">关于软件</span></div>
      <el-dialog
          title="关于软件"
          :visible.sync="textVisible"
          width="50%"
          top="10vh">
      <span>1.1编写目的 <br>
      本需求说明书目的在于：将用户提供的需求描述系统化、精确化、全面化。从而实现：
      1．便于用户、分析人员和设计人员进行理解和交流。<br>
      2．支持目标软件系统的确认。<br>
      3．控制系统进化过程。<br>
      预期读者：软件设计者和测试者。<br>
      1.2背景 <br>
      说明：<br>
      1．待开发软件系统的名称：基于百度飞桨的遥感图像智能解译平台；<br>
      2．项目来源：《软件杯》命题组；<br>
      3．项目开发者：一路向北队；<br>
      4．依赖实验室：创新实验室。<br>
      1.3文档约定 <br>
      计算方法：是指对收集到数据进行合理计算得到真实需要数据所采取的方法；<br>
      数据清洗：指对数据进行校验，去重等；<br>
      目标提取器：指DeepLab V3+算法；<br>
      变化检测器：指BIT算法；<br>
      目标检测器：指PP-YOLO算法；<br>
      服务端：指后端程序；<br>
      客户：指本产品的使用者，一般为企业管理人员或安全部门等，本文档中的用户与客户概念相同；<br>
      Web界面：指在Vue框架下完成的UI界面。</span>
        <span slot="footer" class="dialog-footer">
    <el-button @click="textVisible = false">取 消</el-button>
    <el-button type="primary" @click="textVisible = false">确 定</el-button>
  </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: "about",
  data() {
    return {
      textVisible: false,
    }
  },
  methods: {
    handleClose() {
      this.textVisible = true
    },
    about() {
      $('.help')[0].onmouseover = function () {
        $('.text').css('opacity', '1')
      }
      $('.help')[0].onmouseout = function () {
        $('.text').css('opacity', '0')
      }
    }
  }
}
</script>

<style scoped>
.about {
  width: 200px;
  height: 50px;
  position: absolute;
  margin: 0;
  right: 0;
  bottom: 0;
}

.text {
  width: 58px;
  height: 30px;
  margin: 0;
  right: 2px;
  bottom: 67px;
  position: absolute;
  opacity: 0;
}

.help {
  width: 30px;
  height: 30px;
  margin: 0;
  background-color: #14294C;
  right: 15px;
  bottom: 43px;
  position: absolute;
  cursor: pointer;
}

.help img {
  width: 30px;
  height: 30px;
}
</style>