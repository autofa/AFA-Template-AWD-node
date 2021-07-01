```
# dockerfile构建
docker build –t awd:1 .
# dockerfile运行
docker run –d -p 80:80 --p 222:22 --name awd awd:1
```