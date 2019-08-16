FROM alpine
Run apk add git
WORKDIR /repo
ENTRYPOINT [&quot;git&quot;, &quot;clone&quot;]
