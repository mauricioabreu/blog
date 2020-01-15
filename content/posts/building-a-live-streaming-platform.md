---
title: Building a live streaming platform, part I
date: 2019-12-22
tags: ["live-streaming"]
slug: building-a-live-streaming-platform-part-i
---

Have you ever got yourself thinking how live streaming works?

This post is a guide to build your own live streaming platform. After reading and following the examples
included on this post, you will be able to publish your content live.

## How live streaming works

If you consume videos on Youtube, you probably already had contact with a live video transmited over the web.

Most of Youtube content is on demand (VoD) but today we see a lot of people streaming games, news, shows and all kinds of stuff with their smartphones or notebooks.

But how does this happen? How our recording goes through the internet and gets views around the world?

### Ingest

The first part is popularly known as **ingest** and it is the step where we publish our video.

We can publish a video using well known and open source tools like [ffmpeg](https://ffmpeg.org/) and [OBS Studio](https://obsproject.com/). With **ffmpeg** you can publish a video file and loop it, pretending to be a live video. Or use **OBS Studio** to stream a video directly from your webcam.

But where does it go? A server.

There is a variety of protocols used to ingest video. You can use HTTP or the new SRT protocol. For this series of posts we will
use **RTMP** (Real-Time Messaging Protocol), solid, widely used and based on TCP. Developed by Macromedia, it was used in the old Flash player.

#### A bit about RTMP

RTMP is an L7 (application layer) protocol. It has some variations like **RTMPS** (Security) and **RTMPE** (Encrypted). They are not the same thing. Although both have the same goals, RTMPS uses SSL certificates while RTMPE uses standard cryptographic algorithms to generate a pair of keys so the client and the server can encrypt and decrypt the data being transmitted.

RTMP works over TCP, which means it guarantees packet delivery and missed packets will be retransmitted. It can also be a bad thing for live streaming because problems like network congestion will cause a delay in your streaming.

Since RTMP is old and it does not receive any specification updates, it does not support modern audio and video codecs.

It is not a big deal, though. With RTMP you can stream videos with **H.264** (video) and **AAC** (audio). These codecs are widely used.

In the past, RTMP was also used for playback. And it is almost impossible now given the high number of people simultaneously watching a streaming. A good strategy is to use RTMP to receive the streaming (ingest) and serve the playlists and chunks using [HLS](https://en.wikipedia.org/wiki/HTTP_Live_Streaming) or [DASH](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP) so you can have a CDN on top of it. 

### Bulding a server

*Before moving on, I recommend you to [clone the repository](https://github.com/mauricioabreu/building-a-live-streaming-platform) containing all assets to run the following commands. Use the 0.1.0 tag (git checkout 0.1.0)*

Now we already know the protocol we will use, we need a server to receive our video. If you ever heard about nginx, you need to know **NGINX-RTMP**, a RTMP streaming server based on NGINX. With this server you can:

* Ingest video over RTMP protocol;
* Generate HLS and DASH playlists;
* Transcode videos with ffmpeg.

And some other features that can be checked [here](https://github.com/arut/nginx-rtmp-module#features)

To ease our job, we can use a Docker image to have a RTMP server up and running.

```
make runserver
```

These commands will download the Docker image and start a NGINX-RTMP server ready to receive our live content.

Now we have to publish some live content. Let's generate a video using ffmpeg, sending it to our RTMP server.

```
make ingest
```

Executing this command will ingest a colored video to test our server.

There is a lot going on there but the most important part is the very end: rtmp://localhost:1935/stream/colors

This is the RTMP address of our server. Let's break it into pieces so we can understand it better:

* **1935** - default RTMP port;
* **stream** - application name described in our NGINX configuration;
* **colors** - streaming name. It identifies each stream your server is handling.

NGINX-RTMP is not a simple receiver. It also *segments* incoming data, generating HLS and DASH ready to be consumed.

Now it is time to test our stream by watching it. You can use [VLC](https://www.videolan.org/) to watch it. **VLC** is an open source software to reproduce a wide variety of media, compatible with most of existent codecs.

Open your VLC, go to "Open media", choose "Network" and paste http://localhost:8080/live/colors.m3u8 there.

If everything is ok, you will see something like this:

{{< figure src="/img/colors.jpg" width="50%" >}}

### Resources

Here is a list of links to improve your knowledge of video streaming:

* [Streaming onboarding](https://github.com/Eyevinn/streaming-onboarding)
* [Intro video concepts and ffmpeg (until Bonus Round: Adaptive Streaming)](https://github.com/leandromoreira/ffmpeg-libav-tutorial)
* [Coursera: Fundamentals of Digital Image and Video Processing](https://www.coursera.org/learn/digital)
* [Digital video introduction](https://github.com/leandromoreira/digital_video_introduction)

Thank you for reading. Wait you in the next episode.