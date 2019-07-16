for /r %%i in (.\Software\*) do (
    echo Uploading: %%i
    ampy --port COM5 put %%i
)
