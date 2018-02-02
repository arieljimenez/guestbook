FROM alpine:3.7

ENV APPDIR /app
ENV CONFIG mysql.config.sh

RUN mkdir -p $APPDIR

RUN apk add --no-cache mysql \
                       mysql-client

ADD $CONFIG $APPDIR

RUN chmod +x $APPDIR/$CONFIG

EXPOSE 3306

WORKDIR $APPDIR

CMD ["./mysql.config.sh"]
