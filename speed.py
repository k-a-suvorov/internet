try:
    import speedtest
except ImportError:
    print("Ошибка загрузки модулей, исправьте код программы!")


test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Speed: {round((download/1024)/1024,  2)} Mb/s \n Upload Speed : {round((upload/1024)/1024,  2)} Mb/s")
