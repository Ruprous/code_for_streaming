@echo off
rem OBSを起動
start "OBS" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"

rem わんコメを起動
start "わんコメ" "C:\Program Files\OneComme\わんコメ - OneComme.exe"

rem VOICEVOXを起動
start "VOICEVOX" "C:\Program Files\VOICEVOX\VOICEVOX.exe"

rem 棒読みちゃんを起動
start "棒読みちゃん" "C:\Program Files\BouyomiChan\BouyomiChan.exe"

:wait_for_input
echo 起動完了！終了するには「end」と入力してEnterを押してな！
set /p user_input=入力: 

if /i "%user_input%"=="end" (
    goto :exit_program
) else (
    echo 「end」と入力するまで終了せえへんで！
    goto :wait_for_input
)

:exit_program
rem OBS、わんコメ、VOICEVOX、棒読みちゃんを終了
taskkill /im obs64.exe /f
taskkill /im "わんコメ - OneComme.exe" /f
taskkill /im VOICEVOX.exe /f
taskkill /im BouyomiChan.exe /f

echo 全部終了したで！配信お疲れさん！
pause
