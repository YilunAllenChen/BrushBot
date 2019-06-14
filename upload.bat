for /r %%i in (.\Upload\*) do (
    echo Uploading: %%i
    ampy --port COM6 put %%i
)
