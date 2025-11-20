// pages/user/user.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  },
  handleEditUserInfo(){
    wx.showToast({
      title:'跳转修改',
      icon:"success",
      duration:1500,
      mask:true
    })
  },
  goToOrderList(){
    wx.showModal({
      title: '跳转提示',
      content: '123456678',
      complete: (res) => {
        if (res.cancel) {
          console.log("取消跳转") 
        }
        if (res.confirm) {
          console.log("跳转成功") 
        }
      }
    })
  },
  goToOrderList(){
    wx.showModal({
      title: '跳转提示',
      content: '123456678',
      complete: (res) => {
        if (res.cancel) {
          console.log("取消跳转") 
        }
        if (res.confirm) {
          console.log("跳转成功") 
        }
      }
    })
  },
  goToOrderList(){
    wx.showModal({
      title: '跳转提示',
      content: '123456678',
      complete: (res) => {
        if (res.cancel) {
          console.log("取消跳转") 
        }
        if (res.confirm) {
          console.log("跳转成功") 
        }
      }
    })
  },

})