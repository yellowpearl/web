chmod a+x init.sh
cp /etc/nginx/nginx.conf ~/web/etc
sudo ln -sf /home/box/web/etc/nginx.conf  /home/yellowpearl/PycharmProjects/untitled1/test
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start