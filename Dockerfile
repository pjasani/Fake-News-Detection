FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD ["user_control.py"]