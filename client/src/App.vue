<template>
  <div class="w-screen h-screen relative">
    <Video :ros="ros" class="w-full h-full" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { createRos } from "./api/ros.ts"
import Video from "./components/video.vue"
import { useLocalStorage } from "./utils/useLocalStorage.ts";

const { ros } = createRos()

onMounted(() => {
  const params = new URLSearchParams(location.search)
  const newWebSocketURL = params.get("websocket_url")
  if (newWebSocketURL) {
    const webSocketURL = useLocalStorage("WebSocketURL")
    if (webSocketURL.value === newWebSocketURL) return
    webSocketURL.value = newWebSocketURL
    location.reload()
  }
})
</script>

