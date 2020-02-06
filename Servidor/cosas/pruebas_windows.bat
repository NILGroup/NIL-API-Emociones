rd /s /q resultados
mkdir resultados
for /F %%x in ('dir /B/D .') do (
	if %%x neq resultados if %%x neq pruebas.sh if %%x neq pruebas_windows.bat python ../traductor.py %%x > resultados/%%x
) 