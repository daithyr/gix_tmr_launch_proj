package com.example.a5gsignaldetectionapp

import android.Manifest
import android.annotation.SuppressLint
import android.content.pm.PackageManager
import android.os.Bundle
import android.os.Environment
import android.os.Handler
import android.os.Looper
import android.telephony.CellInfo
import android.telephony.TelephonyManager
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import java.io.File
import java.io.FileWriter
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    private lateinit var telephonyManager: TelephonyManager
    private lateinit var signalStrengthTextView: TextView
    private lateinit var startButton: Button
    private lateinit var stopButton: Button

    private val handler = Handler(Looper.getMainLooper())
    private lateinit var signalStrengthRunnable: Runnable
    private var isCollecting = false
    private val signalData = mutableListOf<Triple<String, Long, Int>>() // 时间戳, 毫秒数, 信号强度值
    private var startTime: Long = 0

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        signalStrengthTextView = findViewById(R.id.signalStrengthTextView)
        startButton = findViewById(R.id.startButton)
        stopButton = findViewById(R.id.stopButton)

        telephonyManager = getSystemService(TELEPHONY_SERVICE) as TelephonyManager

        startButton.isEnabled = false
        stopButton.isEnabled = false

        startButton.setOnClickListener {
            if (!isCollecting) {
                signalStrengthTextView.text = "Starting signal collection..."
                startSignalStrengthUpdates()
                isCollecting = true
                startTime = System.currentTimeMillis()
                startButton.isEnabled = false
                stopButton.isEnabled = true
            }
        }

        stopButton.setOnClickListener {
            if (isCollecting) {
                signalStrengthTextView.text = "Stopping signal collection..."
                stopSignalStrengthUpdates()
                isCollecting = false
                saveSignalDataToCsv()
                startButton.isEnabled = true
                stopButton.isEnabled = false
            }
        }

        requestPermissions()
    }

    @SuppressLint("SetTextI18n")
    private fun requestPermissions() {
        val permissionLauncher = registerForActivityResult(
            ActivityResultContracts.RequestMultiplePermissions()
        ) { permissions ->
            val readPhoneStateGranted = permissions[Manifest.permission.READ_PHONE_STATE] ?: false
            val accessFineLocationGranted = permissions[Manifest.permission.ACCESS_FINE_LOCATION] ?: false

            if (readPhoneStateGranted && accessFineLocationGranted) {
                signalStrengthTextView.text = "Permissions Granted"
                startButton.isEnabled = true
            } else {
                signalStrengthTextView.text = "Permissions Denied"
            }
        }

        permissionLauncher.launch(
            arrayOf(
                Manifest.permission.READ_PHONE_STATE,
                Manifest.permission.ACCESS_FINE_LOCATION
            )
        )
    }

    private fun startSignalStrengthUpdates() {
        signalStrengthRunnable = object : Runnable {
            override fun run() {
                getSignalStrength()
                handler.postDelayed(this, 1000)
            }
        }
        handler.post(signalStrengthRunnable)
    }

    private fun stopSignalStrengthUpdates() {
        handler.removeCallbacks(signalStrengthRunnable)
    }

    @SuppressLint("MissingPermission", "SetTextI18n")
    private fun getSignalStrength() {
        if (ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) == PackageManager.PERMISSION_GRANTED &&
            ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.READ_PHONE_STATE
            ) == PackageManager.PERMISSION_GRANTED
        ) {
            val cellInfoList: List<CellInfo>? = telephonyManager.allCellInfo

            if (!cellInfoList.isNullOrEmpty()) {
                for (cellInfo in cellInfoList) {
                    if (cellInfo is android.telephony.CellInfoNr) {
                        val nrSignalStrength = cellInfo.cellSignalStrength
                        val strengthValue = nrSignalStrength.dbm
                        val currentTimeMillis = System.currentTimeMillis()
                        val timestamp = SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS", Locale.getDefault()).format(Date(currentTimeMillis))
                        signalData.add(Triple(timestamp, currentTimeMillis, strengthValue))

                        signalStrengthTextView.text = "5G Signal Strength: $strengthValue dBm"
                        Log.d("SignalStrength", "Signal Strength: $strengthValue dBm at $timestamp ($currentTimeMillis)")
                        return
                    }
                }
                signalStrengthTextView.text = "5G Signal Not Available"
            } else {
                signalStrengthTextView.text = "No Cell Info Available"
            }
        } else {
            signalStrengthTextView.text = "Permissions Not Granted"
        }
    }

    @SuppressLint("SetTextI18n")
    private fun saveSignalDataToCsv() {
        val dateFormat = SimpleDateFormat("yyyyMMdd_HHmm", Locale.getDefault())
        val startTimestamp = dateFormat.format(Date(startTime))
        val fileName = "5G_Signal_Data_$startTimestamp.csv"
        val documentsPath = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOCUMENTS)?.absolutePath
        if (documentsPath == null) {
            signalStrengthTextView.text = "Error: Cannot access Documents folder"
            return
        }
        val file = File(documentsPath + File.separator + fileName)

        try {
            val writer = FileWriter(file)
            writer.append("Timestamp,Milliseconds,Signal Strength (dBm)\n")
            for ((timestamp, milliseconds, strength) in signalData) {
                writer.append("$timestamp,$milliseconds,$strength\n")
            }
            writer.flush()
            writer.close()
            signalStrengthTextView.text = "Data saved to $file"
        } catch (e: IOException) {
            Log.e("SaveCSV", "Error saving data to CSV: ${e.message}")
            signalStrengthTextView.text = "Error saving data"
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        handler.removeCallbacks(signalStrengthRunnable)
    }
}
