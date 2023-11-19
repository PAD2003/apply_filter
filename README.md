<div align="center">

# Apply Filter

</div>

## Description

Apply filter to the face based on landmark points.

## Pipeline

Download weights for YOLO5face at https://github.com/deepcam-cn/yolov5-face

Apply filter

```
python -m apply_filter.app
```

## Docker

Pull docker image

```
docker pull pad2003/apply_filter_web_application:latest
```

Run docker container

```
docker run -p 7000:7000 pad2003/apply_filter_web_application:latest
```