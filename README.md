===================lesson 3============
docker ps -a\
docker status\
docker version\
docker run hello-world\
docker images -a\
docker ps\
docker run -d -p  8080:80 nginx\
lynx http://localhost:8080 \
docker run -it --rm alpine /bin/sh \
docker run -it --rm centos /bin/bash\
[root@4e7a3d7c3958 /]# echo $0\
/bin/bash\
==================lesson4 (CI/CD)===========


docker volume create --name nexus-data
chmod  644 nexus-data/
docker run -d -p 8081:8081 --name nexus3 -v nexus-data:/nexus-data sonatype/nexus3

docker run -it --name teamcity-server-instance  \
    -v /home/anton/devops/GitDevOps03/teamcity-server/data:/data/teamcity_server/datadir \
    -v /home/anton/devops/GitDevOps03/teamcity-server/logs:/opt/teamcity/logs  \
    -p 8111:8111 \
    jetbrains/teamcity-server

docker run  -d -it -e SERVER_URL="172.17.0.1:8111" -v /home/anton/devops/GitDevOps03/agent/conf:/data/teamcity_agent/conf -v /var/run/docker.sock:/var/run/docker.sock jetbrains/teamcity-agent



