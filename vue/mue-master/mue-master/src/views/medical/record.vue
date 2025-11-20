<template>
  <div>
    <UEditor :config=config ref="ueditor"></UEditor>
    <!-- <button @click="getContent()"></button> -->
  </div>
</template>
<script>
import UEditor from '../../components/SdeEditor/sdeEditor'
export default {
  name: 'hello',
  components: { UEditor },
  data () {
    return {
      config: {
        theme: 'left',
        autoHeightEnabled: false,
        autoFloatEnabled: true,
        initialContent: '请输入内容',
        autoClearinitialContent: true,
        initialFrameWidth: null,
        initialFrameHeight: 580,
        BaseUrl: '',
        UEDITOR_HOME_URL: '/ue/',
        wordCount: false,
        elementPathEnabled: false,
        default_open_toolbar: 'sde-toolbar-editor',
        iframeCssUrl: '/ue/themes/iframe.css',
        page: 'page',
        toolbars: [{
        name: 'sde-toolbar-file',
        title: '文件',
          items: [{
            name: 'sde-toolbar-file-file',
            title: '文件管理',
            items: [{
              name: 'openxml',
              title: '打开XML'
            }, {
              name: 'importxml',
              title: '下载XML'
            }]
          }]
        }, {
          name: 'sde-toolbar-editor',
          title: '编辑',
          items: [{
            name: 'sde-toolbar-editor-history',
            title: '历史记录',
            items: [{
              name: 'drafts',
              title: '草稿箱'
            }, {
              name: 'undo',
              title: '撤销'
            }, {
              name: 'redo',
              title: '恢复'
            }, {
              name: 'fullscreen',
              title: '全屏'
            }, {
              name: 'insertframe',
              title: '插入Iframe'
            }, {
              name: 'template',
              title: '模板'
            }, {
              name: 'background',
              title: '背景'
            }, {
              name: 'wordimage',
              title: '图片转存'
            }, {
              name: 'date',
              title: '日期'
            }, {
              name: 'time',
              title: '时间'
            }, {
              name: 'horizontal',
              title: '分隔线'
            }]
          }, {
            name: 'sde-toolbar-editor-clipboard',
            title: '样式',
            items: [{
              name: 'fontfamily',
              title: '字体'
            }, {
              name: 'autotypeset',
              title: '自动格式化'
            }, {
              name: 'customstyle',
              title: '自定义标题'
            }, {
              name: 'forecolor',
              title: '文字颜色'
            }, {
              name: 'paragraph',
              title: '段落格式'
            }, {
              name: 'backcolor',
              title: '背景颜色'
            }, {
              name: 'fontsize',
              title: '字号'
            }]
          }, {
            name: 'sde-toolbar-editor-fonts',
            title: '字体',
            items: [{
              name: 'upsize',
              title: '增大字体'
            }, {
              name: 'downsize',
              title: '缩小字体'
            }, {
              name: 'subscript',
              title: '上标'
            }, {
              name: 'superscript',
              title: '下标'
            }, {
              name: 'bold',
              title: '加粗'
            }, {
              name: 'italic',
              title: '倾斜'
            }, {
              name: 'underline',
              title: '下划线'
            }, {
              name: 'fontborder',
              title: '字符边框'
            }, {
              name: 'strikethrough',
              title: '删除线'
            }, {
              name: 'blockquote',
              title: '引用'
            }, {
              name: 'selectall',
              title: '全选'
            }, {
              name: 'cleardoc',
              title: '清空文档'
            }, {
              name: 'formatmatch',
              title: '格式刷'
            }, {
              name: 'removeformat',
              title: '清除格式'
            }]
          }, {
            name: 'sde-toolbar-editor-paragraphs',
            title: '段落',
            items: [{
              name: 'justifyleft',
              title: '向左对齐'
            }, {
              name: 'justifycenter',
              title: '居中对齐'
            }, {
              name: 'justifyright',
              title: '向右对齐'
            }, {
              name: 'justifyjustify',
              title: '两端对齐'
            }, {
              name: 'blockindent',
              title: '增加缩进'
            }, {
              name: 'blockoutdent',
              title: '减小缩进'
            }, {
              name: 'unorderedlist',
              title: '无序编号'
            }, {
              name: 'orderedlist',
              title: '有序编号'
            }, {
              name: 'rowspacingtop',
              title: '段前距'
            }, {
              name: 'rowspacingbottom',
              title: '段后距'
            }, {
              name: 'lineheight',
              title: '行高'
            }, {
              name: 'imagenone',
              title: ''
            }, {
              name: 'imageleft',
              title: ''
            }, {
              name: 'imageright',
              title: ''
            }, {
              name: 'imagecenter',
              title: ''
            }, {
              name: 'DirectionalityLtr',
              title: ''
            }, {
              name: 'DirectionalityRtl',
              title: ''
            }, {
              name: 'touppercase',
              title: ''
            }, {
              name: 'tolowercase',
              title: ''
            }]
          }]
        }, {
          name: 'sde-toolbar-insert',
          title: '插入',
          items: [{
            name: 'sde-toolbar-insert-pagebreak',
            title: '分页符',
            items: [{
              name: 'pagebreak',
              title: '分页符'
            }]
          }, {
            name: 'sde-toolbar-insert-spechars',
            title: '字符',
            items: [{
              name: 'spechars',
              title: '字符'
            }]
          }, {
            name: 'sde-toolbar-insert-links',
            title: '链接',
            items: [{
              name: 'link',
              title: '添加链接'
            }, '|', {
              name: 'unlink',
              title: '取消链接'
            }, {
              name: 'anchor',
              title: '锚点'
            }]
          }, {
            name: 'sde-toolbar-insert-images',
            title: '图片',
            items: [{
              name: 'insertimage',
              title: '图片管理'
            }, {
              name: 'simpleupload',
              title: '插入'
            }, {
              name: 'emotion',
              title: '表情'
            }, {
              name: 'vectordiagram',
              title: '矢量图'
            }, {
              name: 'snapscreen',
              title: '截屏'
            }, {
              name: 'scrawl',
              title: '涂鸦'
            }, {
              name: 'insertvideo',
              title: '视频'
            }, {
              name: 'music',
              title: '音乐'
            }, {
              name: 'attachment',
              title: '附件'
            }]
          }, {
            name: 'sde-toolbar-insert-map',
            title: '地图',
            items: [{
              name: 'map',
              title: '地图'
            }, {
              name: 'gmap',
              title: 'Google地图'
            }]
          }, {
            name: 'sde-toolbar-insert-insertcode',
            title: '代码',
            items: [{
              name: 'insertcode',
              title: '代码'
            }]
          }, {
            name: 'sde-toolbar-insert-kityformula',
            title: '公式',
            items: [{
              name: 'kityformula',
              title: '公式'
            }]
          }]
        }, {
          name: 'sde-toolbar-table',
          title: '表格',
          items: [{
            name: 'sde-toolbar-table-table',
            title: '表格',
            items: [{
              name: 'inserttable',
              title: '插入表格'
            }, {
              name: 'deletetable',
              title: '删除表格'
            }, {
              name: 'insertrow',
              title: '插入行'
            }, {
              name: 'insertcol',
              title: '插入列'
            }, {
              name: 'deleterow',
              title: '删除行'
            }, {
              name: 'deletecol',
              title: '删除列'
            }]
          }, {
            name: 'sde-toolbar-table-merge',
            title: '合并单元格',
            items: [{
              name: 'mergecells',
              title: '合并单元格'
            }, {
              name: 'mergedown',
              title: '向下合并单元格'
            }, {
              name: 'mergeright',
              title: '向右合并单元格'
            }, {
              name: 'splittocells',
              title: '拆分单元格'
            }, {
              name: 'splittocols',
              title: '单元格拆分成列'
            }, {
              name: 'splittorows',
              title: '单元格拆分成行'
            }]
          }]
        }, {
          name: 'sde-toolbar-views',
          title: '视图',
          items: [{
            name: 'sde-toolbar-views-preview',
            title: '预览文档',
            items: [{
              name: 'preview',
              title: '预览文档'
            }]
          }]
        }, {
          name: 'sde-toolbar-tools',
          title: '工具',
          items: [{
            name: 'sde-toolbar-tools-drafts',
            title: '草稿箱',
            items: [{
              name: 'drafts',
              title: '草稿箱'
            }]
          }, {
            name: 'sde-toolbar-tools-print',
            title: '打印',
            items: [{
              name: 'print',
              title: '普通打印'
            }, {
              name: 'seniorprint',
              title: '高级打印'
            }]
          }, {
            name: 'sde-toolbar-tools-search',
            title: '搜索',
            items: [{
              name: 'searchreplace',
              title: '查找替换'
            }]
          }, {
            name: 'sde-toolbar-tools-wordcount',
            title: '字数统计',
            items: [{
              name: 'wordcount',
              title: '字数统计'
            }]
          }]
        }, {
          name: 'sde-toolbar-controls',
          title: '控件',
          items: [{
            name: 'sde-toolbar-controls-controls',
            title: '新增控件',
            items: [{
              name: 'mcctrllabel',
              title: '标签控件'
            }, {
              name: 'mcctrltext',
              title: '单行文本'
            }, {
              name: 'mcctrlsection',
              title: '文档段'
            }, {
              name: 'textbox',
              title: '文档节'
            }, {
              name: 'mcctrlselect',
              title: '下拉选择'
            }, {
              name: 'mcctrldate',
              title: '日期控件'
            }, {
              name: 'mcctrlradio',
              title: '单选框'
            }, {
              name: 'mcctrlcbx',
              title: '复选框'
            }]
          }]
        }],
        toolbars1: [[
            'fullscreen', 'source', '|', 'undo', 'redo', '|'
            ], ['combox', 'bold', 'button', 'myblockquote', 'dialog'], ['bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc', '|',
            'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
            'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
            'directionalityltr', 'directionalityrtl', 'indent', '|',
            'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
            'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
            'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment', 'map', 'gmap', 'insertframe', 'insertcode', 'webapp', 'pagebreak', 'template', 'background', '|',
            'horizontal', 'date', 'time', 'spechars', 'snapscreen', 'wordimage', '|',
            'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts', '|',
            'print', 'preview', 'searchreplace', 'drafts', 'help'
        ]]
      },
      addFormVisible: false
    }
  },
  methods: {
    openWindow: function () {
        this.addFormVisible = true
    },
    getContent: function () {
      const content = this.$refs.ueditor.getUEContent()
      console.log(content)
      alert(content)
      console.log(window.MUE.getContent())
      window.MUE.execCommand('insertHtml', '​<span class="sde-ctrl" LL="S" contenteditable="false" id="w" sde-type="text" sde-right="." sde-model="%7B%22desc%22%3A%22%E8%AF%B7%E9%80%89%E6%8B%A9%22%2C%22required%22%3A0%2C%22strictverify%22%3A0%2C%22notdel%22%3A0%2C%22verify%22%3A%22%22%2C%22mode%22%3A%22EDITOR%22%7D"><span class="sde-value" contenteditable="true" sde-left="[" sde-right="]" title="请选择" style="color: rgb(51, 126, 255); background-color: rgb(255, 103, 15);">请选择</span></span>​')
    }
  }
}
</script>
<style scoped>
</style>
