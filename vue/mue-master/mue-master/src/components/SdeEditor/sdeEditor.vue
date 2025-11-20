<template>
  <div>
    <script id="editor" type="text/plain" ></script>
  </div>
</template>
<script>
export default {
    name: 'ueditor',
    data () {
        return {
            editor: null
        }
    },
    props: {
        id: {
            type: String
        },
        config: {
            type: Object
        }
    },
    mounted () {
        const that = this
        that.editor = window.MUE = window.UE.getEditor('editor', that.config)
    },
    destroyed () {
        this.editor.destroy()
    },
    methods: {
        getUEContent: function () {
            return this.editor.getContent()
        }
    }
}
</script>
