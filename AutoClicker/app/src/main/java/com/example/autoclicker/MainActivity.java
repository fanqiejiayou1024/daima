package com.example.autoclicker;
import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import android.content.SharedPreferences;
import android.widget.EditText;
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnStart = findViewById(R.id.btn_start);
        Button btnStop = findViewById(R.id.btn_stop);

        // 跳转到无障碍设置页面
        btnStart.setOnClickListener(v -> {
            Intent intent = new Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS);
            startActivity(intent);
        });

        // 停止服务
        btnStop.setOnClickListener(v -> {
            Intent intent = new Intent(this, AutoClickService.class);
            stopService(intent);
        });
    }
    
}
