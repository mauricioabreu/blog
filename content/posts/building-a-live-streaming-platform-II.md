---
title: Building a live streaming platform, part II
date: 2020-01-06
tags: ["live-streaming"]
slug: building-a-live-streaming-platform-part-ii
---

* **[Building a live streaming platform, part I](https://www.maugzoide.com/posts/building-a-live-streaming-platform-part-i/)**
* **Building a live streaming platform, part II**

---

This post is the second in the *Building a live streaming platform* series.

We well cover more information about NGINX-RTMP, adding a way to authorize specific people to stream in our platform.

Youtube, Facebook and Twitch use a *stream key* to match your identity. Are you itself streaming this new video game?

## Authorizing streamings

From the point of view of a server, you are a **publisher** if you configured your software to stream your content, be it recorded (previously recorded media on live channels) or live (your notebook or smartphone camera).

To publish your content you must be authorized to do that. Big platforms have their own ways to accomplish it, like using a key. If you *gamer123* is yourself, we must check if that key you have is the same as ours.

What we need here is something to let only authorized people to use our service. Let's build a web application to get this done.

### The web application

*Before moving on, I recommend you to [clone the repository](https://github.com/mauricioabreu/building-a-live-streaming-platform) containing all assets to run the following commands. Use the 0.2.0 tag (git checkout 0.2.0)*

Our web application is simple. Not because it is easy - it is simple because it starts with one endpoint only: *auth*

To start the application execute:

```shell
make run-live
make create-db
```

It will start a webserver running on port 9090, NGINX-RTMP on 1935 and create a *SQLite* database.

To use */auth* we need to use POST method and pass two fields, name and psk. *name* is the streaming name and *psk* is the secret key:

```shell
curl -XPOST -H "Accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" http://localhost:9090/auth -d "name=foos&psk=bar"
```

It will fail because we don't have a user yet. Let's manually enter SQLite consolea and perform a SQL statement to create a new *account*:

```shell
sqlite live.db
```

Type the following statement on the console:

```sql
insert into publishers (name, key) values ('foo', 'bar');
```

Execute the HTTP POST again and you will see you are authorized. This request is very similar to the one NGINX-RTMP will do, except it will run on every new published streaming. To add authorization to our streaming platform we need to set and understand some NGINX-RTMP directives.

### Understanding NGINX-RTMP configuration

Our [RTMP configuration](https://github.com/mauricioabreu/docker-nginx-rtmp/blob/master/nginx.conf) is big and has some key points.

{{< highlight nginx "linenos=true" >}}
rtmp { # start a block to define RTMP settings inside nginx.conf
    server {
        listen 1935; # port to accept RTMP connections
        notify_method post; # HTTP method for callback notifications

        application stream { # "stream" in rtmp://localhost:1935/stream/colors
            live on;
            on_publish http://localhost:9090/auth; # authorization callback
        }
    }
}
{{< / highlight >}}

Our configuration is bigger but the snippet above focus on the authorization callback, the *on_publish* event.

*on_publish* is a server event generated every time a new streaming starts to be published. This event gives us the chance to deny the incoming streaming if we think it is malicious.

When we start to ingest a new streaming (using ffmpeg or OBS Studio) the server will hit the endpoint. If the response status is **2xx** it will accept the connection. Other errors like **4xx** will deny and close the connection.

### Streaming using OBS Studio

[OBS Studio](https://obsproject.com/) is a software designed for video recording and live streaming.

After downloading and opening it, go to *Settings -> Stream*. The next screen will come with fields to configure our streaming.

{{< figure src="/img/stream-settings.png" width="100%" >}}

If you typed everything right, you won't be receiving error messages. You can also analyze your containers applications logs.

Just like in the first time we used VLC to watch our stream at http://localhost:8080/live/foo.m3u8, we can use it again. This time you won't see a colored video with a tone in the background but your webcam's view from seconds ago - *it doesn't need to be now be live*.