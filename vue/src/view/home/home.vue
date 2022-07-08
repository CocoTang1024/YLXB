<template>
  <div class="course-image">
    <el-progress :percentage="50"></el-progress>
    <el-progress :percentage="100" :format="format"></el-progress>
    <el-progress :percentage="100" status="success"></el-progress>
    <el-progress :percentage="100" status="warning"></el-progress>
    <el-progress :percentage="50" status="exception"></el-progress>
  </div>

</template>
<script>
import progressbar from "@/components/common/progressbar";
import $ from "jquery";
import axios from "axios";

export default {
  name: "home",
  data() {
    return {};
  },
  methods: {
    format(percentage) {
      return percentage === 100 ? '满' : `${percentage}%`;
    }
  }

};
</script>

<style>
.temp {
  width: 200px;
  height: 200px;
  border: 1px solid red;
  background-color: #2be1f1;
}

.temp img {
  width: 80px;
  height: 80px;
}

i {
  width: 80px;
  height: 80px;
}

.el-icon-plus::before {
  width: 80px;
  height: 80px;
}

.temp div {
  width: 180px;
  height: 180px;
  border: 1px solid blue;
}

/*.el-upload{*/
/*  width: 180px;*/
/*  height: 180px;*/
/*  border: 1px solid green;*/
/*}*/
.el-icon-plus {
  width: 80px;
  height: 80px;
}

.img {
  position: absolute;
  width: 90px;
  height: 90px;
  float: left;
  left: 0;
  top: 0;
  z-index: -1;
}
</style>

