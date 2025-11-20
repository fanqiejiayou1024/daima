UE.registerUI('dialog',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/text/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"这是个测试浮层",

        //指定dialog的外围样式
        cssRules:"width:600px;height:300px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name:'dialogbutton' + uiName,
        title:'dialogbutton' + uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background-position: -500px 0;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrllabel',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/label/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"标签",

        //指定dialog的外围样式
        cssRules:"width:600px;height:350px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAACX0lEQVR42mL8//8/AzUBQAAxMVAZAAQQ1Q0ECCCqGwgQQCzZ2dnKnz59EgSG5X9GRkYGEMYVriA5bGL//v0D03x8fF8AAohFTU1tjba2thZQ4B/IIGQFMIBsAUwcJIYmznjjxo0HAAHEIisrq+vi4sKMywswjb9//4YbCGODaJDlf//+ZeDh4WH48uWLMkAACsjQBoAQCGBN/kEj2OHOwf4zwAjcBoScQ7x4EDU1Tfpef3jmnIwxUFVijLTWMDNCCOScKaVw1tB7Z61FSolaK3tv3B0RueHvF4DmObQBKAhhANr8/VdhB9xpJCgSzCkGIIgfSK6mrnn93gUzAxHB3Xewu6GquPeCmbfPORCR1UQEMhNVhcGMdPILIBaYgSDJr1+/MgDDgUFTU5NBVFQU7D2Qq0AWfP/+HWwZyDAbGxuGly9fMrCwsIAtBgUJzECAAGICArBtMMUgF7x69QrsFZCclJQUOIxAhoPkQQaDXATyEXIYwxwGEEBMMK9xc3MzmJubgzWfO3eO4fXr12CFnz9/BsuBgJWVFQMvLy/D/v37wS789u0b2JWgcIa5ECCAQJHCYGhoyCAtLQ3WqKqqCvYGiA3yNsilIC+DIoGLi4vBw8MD7AN2dnawi0Fy4uLi8FQBEEAgA1mFhYUZQBgZgGyEeQfkalASAdH8/PwMioqKYEtBGKROUFAQ7HKQeQABxPLkyZPLe/bsASdsmLNxAfQEj5zoQZHx9OnT2wABxAIM3BBgmhOEyP2HK4JlQ0IAOasCXfkZIIAYqV0eAgQQ1UsbgACiuoEAAUR1AwECDADFEjSqwkL2PQAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrltext',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/text/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"文本框",

        //指定dialog的外围样式
        cssRules:"width:600px;height:480px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: 'text' + uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAACX0lEQVR42mL8//8/AzUBQAAxMVAZAAQQ1Q0ECCCqGwgQQCzZ2dnKnz59EgSG5X9GRkYGEMYVriA5bGL//v0D03x8fF8AAohFTU1tjba2thZQ4B/IIGQFMIBsAUwcJIYmznjjxo0HAAHEIisrq+vi4sKMywswjb9//4YbCGODaJDlf//+ZeDh4WH48uWLMkAACsjQBoAQCGBN/kEj2OHOwf4zwAjcBoScQ7x4EDU1Tfpef3jmnIwxUFVijLTWMDNCCOScKaVw1tB7Z61FSolaK3tv3B0RueHvF4DmObQBKAhhANr8/VdhB9xpJCgSzCkGIIgfSK6mrnn93gUzAxHB3Xewu6GquPeCmbfPORCR1UQEMhNVhcGMdPILIBaYgSDJr1+/MgDDgUFTU5NBVFQU7D2Qq0AWfP/+HWwZyDAbGxuGly9fMrCwsIAtBgUJzECAAGICArBtMMUgF7x69QrsFZCclJQUOIxAhoPkQQaDXATyEXIYwxwGEEBMMK9xc3MzmJubgzWfO3eO4fXr12CFnz9/BsuBgJWVFQMvLy/D/v37wS789u0b2JWgcIa5ECCAQJHCYGhoyCAtLQ3WqKqqCvYGiA3yNsilIC+DIoGLi4vBw8MD7AN2dnawi0Fy4uLi8FQBEEAgA1mFhYUZQBgZgGyEeQfkalASAdH8/PwMioqKYEtBGKROUFAQ7HKQeQABxPLkyZPLe/bsASdsmLNxAfQEj5zoQZHx9OnT2wABxAIM3BBgmhOEyP2HK4JlQ0IAOasCXfkZIIAYqV0eAgQQ1UsbgACiuoEAAUR1AwECDADFEjSqwkL2PQAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrlselect',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/select/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"下拉选项",

        //指定dialog的外围样式
        cssRules:"width:600px;height:594px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: 'text' + uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAD00lEQVR42mL8//8/AzUBQACxNDU1TRQSEtJmZGT8DzIcSDOg0yAA44MAiGZiYmL4+/cvw4cPHxiYmZlBfMZv3749AAggFhUVlXR/f392kCBMM0Tjf4Z//xAGgPDv37/Bhvz79w9iIJDev28fw5s3bxjExMQYnj179gsgAIdjsAMgDMLQZpEwx3X7/2/jrN7VMSLYpLe+tltrO0QE73PjvA7YTGD9YQ84CyycGr2jVsY0j5UFJkKJE6oKZgYR+SeAWP7+/ff/L1D++cvXDKdOnWH48eM7A8iBIIP+gwwDGQy0gJmFhcHC1IxBQlKc4efP32A1LKwMYMv4BQTAPvjy5QsDQACx3H/8nmHB2rMM795/Znj37j/QhSzAAAP5k4UB6mGwZmZmJoY3h58wsDI/Z/j7H+RCRgYOTmAwff/BICstBTRUkOH79+8MAAHE8vrdZ4ZTd28wCPNzMBjqyDKwADWCwogRCP+DIwMSIUCfMJy+9Ijh6YsPDKxA14Js5eJkYjBQ+MegrSbLIComyfDp0ycGgABiAbmGjYWJ4TfQ6e/efwEGNgPDP0icQCIJgsARBAoGVhZmoGsZwQaCLIdF1q9fv8DyAAHEIi7Cx6BrqMHw6fNXsMtA3vv/H0aDvPwPEsvMDAx6aqJgF4MMB4lxcLAwMP96wvAXFEnQpAUQQCzyUoIMfj76DPfu3WU4ffosMAZ/w0IOrOkfyEAg/w/QFSKiIgxmJsbACGJm+PcHElFnz35g+PX7DzxpAQQQCzA9Ar3BxCArI8XACHTZD2DyATntL0jBP4jr/gHxn1+/GTiBSYyNjQXiGqC3QV5HhDUjGAMEEAss9f8CamDn4GRgZWMHexkUCRBb/4GTBrsAGzi9/vmDcA3jP4hlyIkfIIBYYHnw5ctXDMdOnAAm8N8MIFcDnQeNnP/gZKKkoMCgr68H1wg3FOgqUNjDwhAggOAGysvLMQgJCwIN/AWODFBiBrkaFHsgV3JycoJjEZanYRgEQNmWBRieoOwIEEBwA1+9eg3MQo8gMc3wHxwJ0sAEKyUlCWb/BnoV2bsw14GSzOvXr8H63r9/zwAQQHAD//79AzT0FTBb/YTGMQODADBLgQwBGQbOiqAIAmfFfwyIsP/F8OLFC7A6UE4BCCAWRmgRIy4uzuDk5ABWwACNWZBXYAahA5gLQfjz589g/Tw8PAwAAcTy48cPsADIVpABnJwc8GILVlTBijVkl8EASE5ZWRlcfD158oQJIIBY7ty5M3PhwoVYC1h0jTDDkC0AFbCgyACWNIxfv369DRBAjNSuAgACDABaZEYT+6oQbgAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrldate',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/date/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"日期控件",

        //指定dialog的外围样式
        cssRules:"width:600px;height:352px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAD00lEQVR42mL8//8/AzUBQACxNDU1TRQSEtJmZGT8DzIcSDOg0yAA44MAiGZiYmL4+/cvw4cPHxiYmZlBfMZv3749AAggFhUVlXR/f392kCBMM0Tjf4Z//xAGgPDv37/Bhvz79w9iIJDev28fw5s3bxjExMQYnj179gsgAIdjsAMgDMLQZpEwx3X7/2/jrN7VMSLYpLe+tltrO0QE73PjvA7YTGD9YQ84CyycGr2jVsY0j5UFJkKJE6oKZgYR+SeAWP7+/ff/L1D++cvXDKdOnWH48eM7A8iBIIP+gwwDGQy0gJmFhcHC1IxBQlKc4efP32A1LKwMYMv4BQTAPvjy5QsDQACx3H/8nmHB2rMM795/Znj37j/QhSzAAAP5k4UB6mGwZmZmJoY3h58wsDI/Z/j7H+RCRgYOTmAwff/BICstBTRUkOH79+8MAAHE8vrdZ4ZTd28wCPNzMBjqyDKwADWCwogRCP+DIwMSIUCfMJy+9Ijh6YsPDKxA14Js5eJkYjBQ+MegrSbLIComyfDp0ycGgABiAbmGjYWJ4TfQ6e/efwEGNgPDP0icQCIJgsARBAoGVhZmoGsZwQaCLIdF1q9fv8DyAAHEIi7Cx6BrqMHw6fNXsMtA3vv/H0aDvPwPEsvMDAx6aqJgF4MMB4lxcLAwMP96wvAXFEnQpAUQQCzyUoIMfj76DPfu3WU4ffosMAZ/w0IOrOkfyEAg/w/QFSKiIgxmJsbACGJm+PcHElFnz35g+PX7DzxpAQQQCzA9Ar3BxCArI8XACHTZD2DyATntL0jBP4jr/gHxn1+/GTiBSYyNjQXiGqC3QV5HhDUjGAMEEAss9f8CamDn4GRgZWMHexkUCRBb/4GTBrsAGzi9/vmDcA3jP4hlyIkfIIBYYHnw5ctXDMdOnAAm8N8MIFcDnQeNnP/gZKKkoMCgr68H1wg3FOgqUNjDwhAggOAGysvLMQgJCwIN/AWODFBiBrkaFHsgV3JycoJjEZanYRgEQNmWBRieoOwIEEBwA1+9eg3MQo8gMc3wHxwJ0sAEKyUlCWb/BnoV2bsw14GSzOvXr8H63r9/zwAQQHAD//79AzT0FTBb/YTGMQODADBLgQwBGQbOiqAIAmfFfwyIsP/F8OLFC7A6UE4BCCAWRmgRIy4uzuDk5ABWwACNWZBXYAahA5gLQfjz589g/Tw8PAwAAcTy48cPsADIVpABnJwc8GILVlTBijVkl8EASE5ZWRlcfD158oQJIIBY7ty5M3PhwoVYC1h0jTDDkC0AFbCgyACWNIxfv369DRBAjNSuAgACDABaZEYT+6oQbgAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrlradio',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/radio/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"单选框",

        //指定dialog的外围样式
        cssRules:"width:600px;height:594px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAD00lEQVR42mL8//8/AzUBQACxNDU1TRQSEtJmZGT8DzIcSDOg0yAA44MAiGZiYmL4+/cvw4cPHxiYmZlBfMZv3749AAggFhUVlXR/f392kCBMM0Tjf4Z//xAGgPDv37/Bhvz79w9iIJDev28fw5s3bxjExMQYnj179gsgAIdjsAMgDMLQZpEwx3X7/2/jrN7VMSLYpLe+tltrO0QE73PjvA7YTGD9YQ84CyycGr2jVsY0j5UFJkKJE6oKZgYR+SeAWP7+/ff/L1D++cvXDKdOnWH48eM7A8iBIIP+gwwDGQy0gJmFhcHC1IxBQlKc4efP32A1LKwMYMv4BQTAPvjy5QsDQACx3H/8nmHB2rMM795/Znj37j/QhSzAAAP5k4UB6mGwZmZmJoY3h58wsDI/Z/j7H+RCRgYOTmAwff/BICstBTRUkOH79+8MAAHE8vrdZ4ZTd28wCPNzMBjqyDKwADWCwogRCP+DIwMSIUCfMJy+9Ijh6YsPDKxA14Js5eJkYjBQ+MegrSbLIComyfDp0ycGgABiAbmGjYWJ4TfQ6e/efwEGNgPDP0icQCIJgsARBAoGVhZmoGsZwQaCLIdF1q9fv8DyAAHEIi7Cx6BrqMHw6fNXsMtA3vv/H0aDvPwPEsvMDAx6aqJgF4MMB4lxcLAwMP96wvAXFEnQpAUQQCzyUoIMfj76DPfu3WU4ffosMAZ/w0IOrOkfyEAg/w/QFSKiIgxmJsbACGJm+PcHElFnz35g+PX7DzxpAQQQCzA9Ar3BxCArI8XACHTZD2DyATntL0jBP4jr/gHxn1+/GTiBSYyNjQXiGqC3QV5HhDUjGAMEEAss9f8CamDn4GRgZWMHexkUCRBb/4GTBrsAGzi9/vmDcA3jP4hlyIkfIIBYYHnw5ctXDMdOnAAm8N8MIFcDnQeNnP/gZKKkoMCgr68H1wg3FOgqUNjDwhAggOAGysvLMQgJCwIN/AWODFBiBrkaFHsgV3JycoJjEZanYRgEQNmWBRieoOwIEEBwA1+9eg3MQo8gMc3wHxwJ0sAEKyUlCWb/BnoV2bsw14GSzOvXr8H63r9/zwAQQHAD//79AzT0FTBb/YTGMQODADBLgQwBGQbOiqAIAmfFfwyIsP/F8OLFC7A6UE4BCCAWRmgRIy4uzuDk5ABWwACNWZBXYAahA5gLQfjz589g/Tw8PAwAAcTy48cPsADIVpABnJwc8GILVlTBijVkl8EASE5ZWRlcfD158oQJIIBY7ty5M3PhwoVYC1h0jTDDkC0AFbCgyACWNIxfv369DRBAjNSuAgACDABaZEYT+6oQbgAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('mcctrlcbx',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/checkbox/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"复选框",

        //指定dialog的外围样式
        cssRules:"width:600px;height:594px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAD00lEQVR42mL8//8/AzUBQACxNDU1TRQSEtJmZGT8DzIcSDOg0yAA44MAiGZiYmL4+/cvw4cPHxiYmZlBfMZv3749AAggFhUVlXR/f392kCBMM0Tjf4Z//xAGgPDv37/Bhvz79w9iIJDev28fw5s3bxjExMQYnj179gsgAIdjsAMgDMLQZpEwx3X7/2/jrN7VMSLYpLe+tltrO0QE73PjvA7YTGD9YQ84CyycGr2jVsY0j5UFJkKJE6oKZgYR+SeAWP7+/ff/L1D++cvXDKdOnWH48eM7A8iBIIP+gwwDGQy0gJmFhcHC1IxBQlKc4efP32A1LKwMYMv4BQTAPvjy5QsDQACx3H/8nmHB2rMM795/Znj37j/QhSzAAAP5k4UB6mGwZmZmJoY3h58wsDI/Z/j7H+RCRgYOTmAwff/BICstBTRUkOH79+8MAAHE8vrdZ4ZTd28wCPNzMBjqyDKwADWCwogRCP+DIwMSIUCfMJy+9Ijh6YsPDKxA14Js5eJkYjBQ+MegrSbLIComyfDp0ycGgABiAbmGjYWJ4TfQ6e/efwEGNgPDP0icQCIJgsARBAoGVhZmoGsZwQaCLIdF1q9fv8DyAAHEIi7Cx6BrqMHw6fNXsMtA3vv/H0aDvPwPEsvMDAx6aqJgF4MMB4lxcLAwMP96wvAXFEnQpAUQQCzyUoIMfj76DPfu3WU4ffosMAZ/w0IOrOkfyEAg/w/QFSKiIgxmJsbACGJm+PcHElFnz35g+PX7DzxpAQQQCzA9Ar3BxCArI8XACHTZD2DyATntL0jBP4jr/gHxn1+/GTiBSYyNjQXiGqC3QV5HhDUjGAMEEAss9f8CamDn4GRgZWMHexkUCRBb/4GTBrsAGzi9/vmDcA3jP4hlyIkfIIBYYHnw5ctXDMdOnAAm8N8MIFcDnQeNnP/gZKKkoMCgr68H1wg3FOgqUNjDwhAggOAGysvLMQgJCwIN/AWODFBiBrkaFHsgV3JycoJjEZanYRgEQNmWBRieoOwIEEBwA1+9eg3MQo8gMc3wHxwJ0sAEKyUlCWb/BnoV2bsw14GSzOvXr8H63r9/zwAQQHAD//79AzT0FTBb/YTGMQODADBLgQwBGQbOiqAIAmfFfwyIsP/F8OLFC7A6UE4BCCAWRmgRIy4uzuDk5ABWwACNWZBXYAahA5gLQfjz589g/Tw8PAwAAcTy48cPsADIVpABnJwc8GILVlTBijVkl8EASE5ZWRlcfD158oQJIIBY7ty5M3PhwoVYC1h0jTDDkC0AFbCgyACWNIxfv369DRBAjNSuAgACDABaZEYT+6oQbgAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('kityformula',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/kityformula/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"公式",

        //指定dialog的外围样式
        cssRules:"width:783px;height:386px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAABMpJREFUeNrEV11MW3UUP/2kMEIYo3TQTQLC1qKMr5EwNPjqg8rL1G0vE6evixM2Gds0fkw+KnFox+bY3BYZYPTBgW8mJkJMdNJJtjG11oK0vaX0AhUKpdAPz7ne3iD2du2AeJLDpfd/7zm///n4/c+VhMNh+D9FHu2mRCKRvXu2uQuvdQRwPSClUim9f/XMqZOv4s/gWltykfeSyfmBAy/CysoyKJVJD+k+jABkcONGTx3+OIrqjSsCKCr6Mz8/D3fu3MWISFHRXBi4a1yu+chVV1evthk3ACmFjlQul1NKBKP0PymtxZJQKIwa5ADz70vjrgFeZs3m37cSgMhuMjMz0WgIRkdHQSaTCcDEIpCamso9FwusGIDlpsYTTxvaz/2o1eZgDSg5xzMzM6DX62FiYgJu3zb1XOw8f402K2a7/nhjU1paWg2BEC1SkfsLqEz3Z9f3MwwjVDOp2WyGqqoq0OmKDtW9/EoWLo2i3o2i99sNLfUjIyM/UCGKiSRai/GhpdLPPvxS3ZGKvZWntVotn9sQpKSkgFqthqGhIRizWnXGjzvMXMn/W8jrVlQtv2ajtMbbhlwaUKeuX7vanaXZvicpSfWcRpPFLSwuLsLSkg+Ki/dgm658i7fy+OdXSxDVg+rnI+1LJAXAo15CdRlam99k2Snr3Nwc1xWkbjcL6enpUFBQkNPSZvhGZDMB6mbUv6IAfCAA4AuMDDCnTjYedLmm/D6fj6tsUqeTgcLCQsjK0tS8897ZY3HYSxjA6lDa+3q7D7lcLgp7hGLB4XBAWVkZbNuW2XaisamKSmijAZCsoE6bhodNQ4NDDRgJgaQCgQDMzs5CeXk5aLU7v9///AsZmwEgUpTuL7/o6//1l/uXbTa7wIoLCwvctahIB088WUMdodwMAGG+kt2q5ORFlSoJMjIyBFomkqIWxccoBSmbAYCT02feeio/P+9oRUUFLC8vc8UYSYXFYoHWlvdr1z0PiJHWsfqGwu3ZOV+Vl1eAx+Ph+CBSjDbbBAx+N9gw6XSOE1VsRgSUubl5I0VFem7X5DyyezobxsbGuz/v6+nH51ixnl8PAMWHHUbT7t27kinvLMtyOycADOMEJCjrB20tbURaPHltaBfIDO0dF3Jysh/D3KPzaWHnxIwez6y/4fXXDuJzTv4QC28kAGlzq+GwRqM+UlpSAna7gxswCACREcNMAp4V5NzO021wI5lQUn/8jUcx5FeI6dwsKxzL1HqYczCZbr09/NOtn4mkeLL6T5EbOy8OfNJ1JSzGDbEAKPPz883V+/aB1+vldhwJvcViBcbhuPnp5a5eOjFFik527iNjL9p4hj+CtyTShorzFy7ZS0tLIBgKgN/vF1hvctKFHbAAao2m1th5qVaMs8hpbm4uVFbuhfHxPzmbiQDYgqHOfGTHDvhjfEyY/XC8Ar1uF542kpjjMa0EgkEE6uNG6VifFWIAlJF8c8Mnf8AR5/9mtvxjMMaZJxHGcoDix/VoR5I4E9Icp1AqQCFXRJl+H9xp5JxA0ED7MFNxaGaGHbjZ//WziXyMRBvN790bxYNqekBsehYbSlPxshNVLVY8CQi1p5sfSr1r/YkBoIk2mf+ckq4TQIinZ1+0j9NYY/mmyFp/fwswAMAtBGxliyxfAAAAAElFTkSuQmCC) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);

UE.registerUI('textbox',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/textbox/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"文本框",

        //指定dialog的外围样式
        cssRules:"width:800px;height:500px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAD00lEQVR42mL8//8/AzUBQACxNDU1TRQSEtJmZGT8DzIcSDOg0yAA44MAiGZiYmL4+/cvw4cPHxiYmZlBfMZv3749AAggFhUVlXR/f392kCBMM0Tjf4Z//xAGgPDv37/Bhvz79w9iIJDev28fw5s3bxjExMQYnj179gsgAIdjsAMgDMLQZpEwx3X7/2/jrN7VMSLYpLe+tltrO0QE73PjvA7YTGD9YQ84CyycGr2jVsY0j5UFJkKJE6oKZgYR+SeAWP7+/ff/L1D++cvXDKdOnWH48eM7A8iBIIP+gwwDGQy0gJmFhcHC1IxBQlKc4efP32A1LKwMYMv4BQTAPvjy5QsDQACx3H/8nmHB2rMM795/Znj37j/QhSzAAAP5k4UB6mGwZmZmJoY3h58wsDI/Z/j7H+RCRgYOTmAwff/BICstBTRUkOH79+8MAAHE8vrdZ4ZTd28wCPNzMBjqyDKwADWCwogRCP+DIwMSIUCfMJy+9Ijh6YsPDKxA14Js5eJkYjBQ+MegrSbLIComyfDp0ycGgABiAbmGjYWJ4TfQ6e/efwEGNgPDP0icQCIJgsARBAoGVhZmoGsZwQaCLIdF1q9fv8DyAAHEIi7Cx6BrqMHw6fNXsMtA3vv/H0aDvPwPEsvMDAx6aqJgF4MMB4lxcLAwMP96wvAXFEnQpAUQQCzyUoIMfj76DPfu3WU4ffosMAZ/w0IOrOkfyEAg/w/QFSKiIgxmJsbACGJm+PcHElFnz35g+PX7DzxpAQQQCzA9Ar3BxCArI8XACHTZD2DyATntL0jBP4jr/gHxn1+/GTiBSYyNjQXiGqC3QV5HhDUjGAMEEAss9f8CamDn4GRgZWMHexkUCRBb/4GTBrsAGzi9/vmDcA3jP4hlyIkfIIBYYHnw5ctXDMdOnAAm8N8MIFcDnQeNnP/gZKKkoMCgr68H1wg3FOgqUNjDwhAggOAGysvLMQgJCwIN/AWODFBiBrkaFHsgV3JycoJjEZanYRgEQNmWBRieoOwIEEBwA1+9eg3MQo8gMc3wHxwJ0sAEKyUlCWb/BnoV2bsw14GSzOvXr8H63r9/zwAQQHAD//79AzT0FTBb/YTGMQODADBLgQwBGQbOiqAIAmfFfwyIsP/F8OLFC7A6UE4BCCAWRmgRIy4uzuDk5ABWwACNWZBXYAahA5gLQfjz589g/Tw8PAwAAcTy48cPsADIVpABnJwc8GILVlTBijVkl8EASE5ZWRlcfD158oQJIIBY7ty5M3PhwoVYC1h0jTDDkC0AFbCgyACWNIxfv369DRBAjNSuAgACDABaZEYT+6oQbgAAAABJRU5ErkJggg==) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);


UE.registerUI('wordcount',function(editor,uiName){

    //创建dialog
    var dialog = new UE.ui.Dialog({
        //指定弹出层中页面的路径，这里只能支持页面,因为跟addCustomizeDialog.js相同目录，所以无需加路径
        iframeUrl:'/ue/plugins/wordcount/index.html',
        //需要指定当前的编辑器实例
        editor:editor,
        //指定dialog的名字
        name:uiName,
        //dialog的标题
        title:"文本框",

        //指定dialog的外围样式
        cssRules:"width:250px;height:150px;",

        //如果给出了buttons就代表dialog有确定和取消
        buttons:[
            {
                className:'edui-okbutton',
                label:'确定',
                onclick:function () {
                    dialog.close(true);
                }
            },
            {
                className:'edui-cancelbutton',
                label:'取消',
                onclick:function () {
                    dialog.close(false);
                }
            }
        ]});

    //参考addCustomizeButton.js
    var btn = new UE.ui.Button({
        name: 'button' + uiName,
        title: uiName,
        theme: editor.options.theme,
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background: url(data:image/png;base64,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) !important;',
        onclick:function () {
            //渲染dialog
            dialog.render();
            dialog.open();
        }
    });

    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);