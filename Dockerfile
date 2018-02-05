FROM alpine:3.7

ENV APPDIR /app

RUN mkdir -p $APPDIR

RUN apk add --no-cache mysql \
                       mysql-client \
                       python \
                       py-pip

RUN pip install virtualenv

EXPOSE 3306 5000

WORKDIR $APPDIR

CMD sh $APPDIR/scripts/init.sh
