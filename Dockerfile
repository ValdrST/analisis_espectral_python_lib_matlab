FROM python:3.8
WORKDIR /runtime
COPY ./matlab/runtime/analisis_espectral/for_redistribution/ /runtime/
RUN ./MyAppInstaller_web.install -agreeToLicense yes -mode silent
RUN rm MyAppInstaller_web.install
WORKDIR /applib
COPY ./matlab/runtime/analisis_espectral/for_redistribution_files_only/ /applib/
RUN python setup.py install
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./
RUN pip3 install .
EXPOSE 3000
