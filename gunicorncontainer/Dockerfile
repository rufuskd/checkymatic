FROM alpine
RUN apk --update add py-gunicorn python py-pip curl
RUN mkdir -p /usr/local/connectorApp
ADD connectorApp /usr/local/connectorApp/
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
EXPOSE 8000
ENTRYPOINT /usr/bin/entrypoint.sh
