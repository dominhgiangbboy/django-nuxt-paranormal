<template>
  <div>
    <video ref="videoPlayer" class="video-js vjs-default-skin vjs-16-9"></video>
  </div>
</template>
<style>
@import "video.js/dist/video-js.css";
</style>
<script>
import videojs from "video.js";

export default {
  name: "VideoPlayer",
  props: {
    options: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  data() {
    return {
      player: null
    };
  },
  mounted() {
    this.player = videojs(
      this.$refs.videoPlayer,
      this.options,
      function onPlayerReady() {}
    );
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose();
    }
  }
};
</script>
