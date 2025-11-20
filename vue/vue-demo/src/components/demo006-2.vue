<!--
 * @Author: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @Date: 2024-10-16 15:26:14
 * @LastEditors: 'fanqie' '12553846+fanqiejiayou1024@user.noreply.gitee.com'
 * @LastEditTime: 2024-10-16 15:29:30
 * @FilePath: \vue-demo\src\components\demo006-2.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <a href="./demo01.vue">dianji1</a>
    <a href="./demo01.vue" @click.prevent>dianji2</a>

    <button @click = "console.log('click')">click1</button>
    <button @click.once = "console.log('click')">click2</button>

    <button @click.left = "console.log('click')">click3</button>

    <input autofocus
        @keyup.enter = "console.log('enter')"
        @keyup.esc = "console.log('esc')"
        @keyup.tab = "console.log('tab')"
        @keyup.delete = "console.log('delete')"
        @keyup.backspace = "console.log('backspace')"
        @keyup.space = "console.log('space')"
        @keyup.up = "console.log('up')"
        @keyup.down = "console.log('down')"
        @keyup.left = "console.log('left')"
        @keyup.right ="console.log('right')"
    >
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>