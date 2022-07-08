<template>
  <div>
    <div class="slider" ref="slider">
      <div class="process" :style="{ width }"></div>
      <div class="thunk" ref="trunk" :style="{ left }">
        <div class="block"></div>
      </div>
    </div>
    <div class="adjust">
      <span style="color: white">置信度：{{ per / 100 }}</span>
    </div>
  </div>
</template>
<script>
/*
 * min 进度条最小值
 * max 进度条最大值
 * v-model 对当前值进行双向绑定实时显示拖拽进度
 * */
export default {
  name: 'progressbar',
  props: ["min", "max", "value"],
  data() {
    return {
      slider: null, //滚动条DOM元素
      thunk: null, //拖拽DOM元素
      per: 50, //当前值

    };
  },
  //渲染到页面的时候
  mounted() {
    this.slider = this.$refs.slider;
    this.thunk = this.$refs.trunk;
    var _this = this;
    console.log(_this);

    this.thunk.onmousedown = function (e) {
      var width = parseInt(_this.width);
      var disX = e.clientX;
      document.onmousemove = function (e) {
        // value, left, width
        // 当value变化的时候，会通过计算属性修改left，width
        // 拖拽的时候获取的新width
        var newWidth = e.clientX - disX + width;
        // 拖拽的时候得到新的百分比
        var scale = newWidth / _this.slider.offsetWidth;
        _this.per = Math.ceil((_this.max - _this.min) * scale + _this.min);
        _this.per = Math.max(_this.per, _this.min);
        _this.per = Math.min(_this.per, _this.max);
        _this.$emit("inputchange", _this.per);
      };
      document.onmouseup = function () {
        document.onmousemove = document.onmouseup = null;
      };
      return false;
    };
  },
  computed: {
    // 设置一个百分比，提供计算slider进度宽度和trunk的left值
    // 对应公式为  当前值-最小值/最大值-最小值 = slider进度width / slider总width
    // trunk left =  slider进度width + trunk宽度/2
    scale() {
      return (this.per - this.min) / (this.max - this.min);
    },
    width() {
      if (this.slider) {
        return this.slider.offsetWidth * this.scale + "px";
      } else {
        return 0 + "px";
      }
    },
    left() {
      if (this.slider) {
        return (
            this.slider.offsetWidth * this.scale -
            this.thunk.offsetWidth / 2 +
            "px"
        );
      } else {
        return 0 + "px";
      }
    },
  },
};
</script>
<style>

.slider {
  user-select: none;
  position: relative;
  margin: 20px 0;
  width: 200px;
  height: 5px;
  background: #e4e7ed;
  border-radius: 5px;
  cursor: pointer;
}

.slider .process {
  position: absolute;
  left: 0;
  top: 0;
  height: 5px;
  border-radius: 5px;
  background: #1A9BD3;
}

.slider .thunk {
  position: absolute;
  left: 100px;
  top: -5px;
  width: 10px;
  height: 10px;
}

.slider .block {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 2px solid #409eff;
  background: rgba(255, 255, 255, 1);
  transition: 0.2s all;
}

.slider .block:hover {
  transform: scale(1.1);
  opacity: 0.6;
}

.adjust {
  font: 20px '微软雅黑 Light';
  letter-spacing: 1px;
  font-style: oblique;
}
</style>
