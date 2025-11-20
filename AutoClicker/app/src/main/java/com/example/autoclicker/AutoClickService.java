package com.example.autoclicker;
import android.accessibilityservice.AccessibilityService;
import android.accessibilityservice.GestureDescription;
import android.graphics.Path;
import android.os.Handler;
import android.view.accessibility.AccessibilityEvent;
import android.view.accessibility.AccessibilityNodeInfo;
import android.graphics.Rect;

public class AutoClickService extends AccessibilityService {
    private Handler handler = new Handler();
    private Runnable clickRunnable;
    private static final int CLICK_INTERVAL = 1000; // 点击间隔1秒
    private int clickX = 500; // 默认点击坐标X
    private int clickY = 1000; // 默认点击坐标Y

    @Override
    public void onAccessibilityEvent(AccessibilityEvent event) {
        // 此处可扩展为根据控件ID点击（示例代码见后续步骤）
    }

    @Override
    public void onInterrupt() {}

    @Override
    protected void onServiceConnected() {
        super.onServiceConnected();
        startAutoClick();
    }

    // 启动定时点击
    private void startAutoClick() {
        clickRunnable = new Runnable() {
            @Override
            public void run() {
                performClick(clickX, clickY);
                handler.postDelayed(this, CLICK_INTERVAL); // 循环执行
            }
        };
        handler.post(clickRunnable);
    }

    // 执行点击操作
    private void performClick(int x, int y) {
        Path path = new Path();
        path.moveTo(x, y);
        GestureDescription.Builder builder = new GestureDescription.Builder();
        GestureDescription.StrokeDescription stroke =
                new GestureDescription.StrokeDescription(path, 0, 50); // 点击持续50ms
        builder.addStroke(stroke);
        dispatchGesture(builder.build(), null, null);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        handler.removeCallbacks(clickRunnable); // 停止点击
    }
}
