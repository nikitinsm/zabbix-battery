FROM python:2.7

# Prepare libs
RUN pip install supervisor

# Prepare environment
ENV APP_ROOT=/opt/zabbix/battery
ENV APP_REPOSITORY=${APP_ROOT}/repository"

# Prepare repository
RUN mkdir -p ${APP_REPOSITORY}/
RUN mkdir -p /var/log/zabbix_battery
COPY . ${APP_REPOSITORY}/

# Prepare python libs
RUN pip install -r ${APP_REPOSITORY}/requirements.pip

# Prepare supervisord
COPY ./deploy/supervisord.conf /etc/supervisord.conf

# Prepare app
WORKDIR ${APP_REPOSITORY}/
RUN python setup.py install

EXPOSE 80

ENTRYPOINT ["supervisord"]