for /r %%i in (.\Upload\*) do (
    echo Uploading: %%i
    ampy --port COM5 put %%i
)
