<template>
  <canvas
    ref="imageCanvas"
    class="w-full h-full object-contain" />
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import RosLib from "roslib";

const imageCanvas = ref<HTMLCanvasElement>();

interface Message {
  data: string;
  encoding: "rgb8";
  header: {
    frame_id: string;
    stamp: {
      sec: number;
      nanosec: number;
    };
  };
  height: number;
  width: number;
  step: number;
  is_bigendian: number;
}

const videoTopicName: string = "/face_image_base64"
const { ros } = defineProps<{
  ros: RosLib.Ros;
}>();

async function getTopic() {
  const messageType = await new Promise<string>((resolve) => ros.getTopicType(videoTopicName, resolve))
  return new RosLib.Topic({
    ros: ros,
    name: videoTopicName,
    messageType
  })
}

const imageTopic = ref<RosLib.Topic>()
watch(() => ros, async () => {
  imageTopic.value = await getTopic()
}, { immediate: true })

function drawCameraImage(_message: RosLib.Message) {
  console.log("draw!")
  const message = _message as Message;
  let image_data = message.data

  let _width = '';
  let _height = '';
  let colonCount = 0;
  let index = 0;

  while (index < image_data.length) {
    let char = image_data[index];
    if (char === ':') {
      colonCount++;
      if (colonCount === 1) {
        _width = image_data.substring(0, index);
      } else if (colonCount === 2) {
        _height = image_data.substring(_width.length + 1, index);
        break;
      }
    }
    index++;
  }

  const width = Number(_width)
  const height = Number(_height)
  const image_base64 = image_data.substring(_width.length + _height.length + 2);

  if (!imageCanvas.value) throw new Error("imageCanvas is undefined");
  imageCanvas.value.width = width;
  imageCanvas.value.height = height;

  const ctx = imageCanvas.value.getContext("2d");
  if (!ctx) throw new Error("ctx is null");

  const img = new Image();
  img.src = `data:image/jpeg;base64,${image_base64}`;
  img.onload = () => {
    ctx.drawImage(img, 0, 0, width, height);
  }
}

onMounted(() => {
  watch(imageTopic, (topic) => {
    if (!topic) return;
    topic.subscribe(drawCameraImage);
  })
});
</script>

