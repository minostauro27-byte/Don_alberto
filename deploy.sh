echo "Iniciando el despliegue automatico de Don Albert"

#Ingresar a la carpeta
cd /home/$USER/moto-api

#Traer los cambios desde git
echo "Trayendo la ultima version desde git"
git pull origin main

#Activar el entorno virtual
echo "Asegurando las dependencias"
source venv/bin/activate
pip install -r requirements.txt  --quiet

#Reiniciar el servidor de systemd
echo "Reiniciando el motor gunicorn"
sudo systemctl restart moto-api.service

#Verificar que este en vivo
echo "Despliegue completado con exito. El estado actual es:"
sudo systemctl status moto-api.service | grep "Active:"
