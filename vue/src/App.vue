<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "App",

};
</script>
<style>
@import "./assets/css/normalize.css";
* {
  margin: 0;
  padding: 0;

}

#app {
  width: 100%;
  height: 100vh;

}


</style>
