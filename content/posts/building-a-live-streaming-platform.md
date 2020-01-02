---
title: Building a live streaming platform, part I
date: 2019-10-22
tags: ["live-streaming"]
slug: building-a-live-streaming-platform-part-i
---

Have you ever got yourself thinking how live streaming technology works?

This post is a guide to build your own live streaming platform. After reading and following the examples
included on this post, you will be able to publish your content live.

## How live streaming works

If you use or know Youtube, you probably had contact with a live video transmited over the web.

Most of Youtube content is on demand (VoD) but today we see a lot of people streaming games, news, shows and all other stuff with their smartphones or notebooks.

But how does this happen? How our recording goes through the internet and get views around the world?

### Ingest

The first part is popularly known as **ingest** and it is the step where we publish our video.

We can publish a video using well known and open source tools like [ffmpeg](https://ffmpeg.org/) and [OBS Studio](https://obsproject.com/). With **ffmpeg** you can publish a video file and loop it, pretending to be a live video. Or use **OBS Studio** to stream a video directly from your webcam.

But where does it go? A server.

There is a variety of protocols used to ingest video. You can use HTTP or the new SRT protocol. For this series of posts we will
use **RTMP** (Real-Time Messaging Protocol), solid, widely used and based on TCP. Developed by Macromedia, it was used in the old Flash player.

#### Bulding a server

*Before moving on, I recommend you to [clone the repository](https://github.com/mauricioabreu/building-a-live-streaming-platform) containing all assets to run the following commands.*

Now we already know the protocol we will use, we need a server to receive our video. If you ever heard about nginx, you need to know **NGINX-RTMP**, a RTMP streaming server based on NGINX. With this server you can:

* Ingest video over RTMP protocol;
* Generate HLS and DASH playlists;
* Transcode videos with ffmpeg.

And some other features that can be checked [here](https://github.com/arut/nginx-rtmp-module#features)

To ease our job, we can use a Docker image to have a RTMP server up and running.

```
docker pull alfg/nginx-rtmp
docker run --net="host" -it -p 1935:1935 -p 8080:80 --rm alfg/nginx-rtmp
```

These commands will download the Docker image and start a NGINX-RTMP server ready to receive our live content.

Now we have to publish some live content. Let's generate a video using ffmpeg, sending it to our RTMP server.

```
docker run --net="host" --rm -v $(pwd):/files jrottenberg/ffmpeg -hide_banner \
    -re -f lavfi -i "testsrc2=size=1280x720:rate=30" -pix_fmt yuv420p \
    -c:v libx264 -x264opts keyint=30:min-keyint=30:scenecut=-1 \
    -tune zerolatency -profile:v high -preset veryfast -bf 0 -refs 3 \
    -b:v 1400k -bufsize 1400k \
    -vf "drawtext=fontfile='/files/fonts/OpenSans-Bold.ttf':text='%{localtime}:box=1:fontcolor=black:boxcolor=white:fontsize=100':x=40:y=400'" \
    -utc_timing_url "https://time.akamai.com/?iso" -use_timeline 0 -media_seg_name 'chunk-stream-$RepresentationID$-$Number%05d$.m4s' \
    -init_seg_name 'init-stream1-$RepresentationID$.m4s' \
    -window_size 5  -extra_window_size 10 -remove_at_exit 1 -adaptation_sets "id=0,streams=v id=1,streams=a" -f flv rtmp://localhost:1935/stream/colors
```

Executing this command will ingest a colored video to test our server.

There is a lot going on there but the most important part is the very end: rtmp://localhost:1935/stream/colors

This is the RTMP address of our server. Let's break it into pieces so we can understand it better:

* **1935** - default RTMP port;
* **stream** - application name described in our NGINX configuration;
* **colors** - streaming name.

Now it is time to test our stream by watching it. You can use [VLC](https://www.videolan.org/) to watch it. **VLC** is an open source software to reproduce a wide variety of media, compatible with most of existent codecs.

Open your VLC, go to "Open media", choose "Network" and paste http://localhost:8080/live/colors.m3u8 there.

If everything is ok, you will see something like this:

{{< figure src="/img/colors.jpg" width="50%" >}}

Thank you for reading. Wait you in the next episode.