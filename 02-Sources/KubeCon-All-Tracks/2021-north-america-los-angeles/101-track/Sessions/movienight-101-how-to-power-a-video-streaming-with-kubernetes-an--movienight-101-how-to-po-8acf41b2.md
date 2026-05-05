---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Rachel Sheikh", "Twitter"]
sched_url: https://kccncna2021.sched.com/event/lV0n/movienight-101-how-to-power-a-video-streaming-with-kubernetes-and-webrtc-rachel-sheikh-twitter
youtube_search_url: https://www.youtube.com/results?search_query=Movienight+101%3A+How+to+Power+a+Video+Streaming+with+Kubernetes+and+WebRTC+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Movienight 101: How to Power a Video Streaming with Kubernetes and WebRTC - Rachel Sheikh, Twitter

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Rachel Sheikh, Twitter
- Schedule: https://kccncna2021.sched.com/event/lV0n/movienight-101-how-to-power-a-video-streaming-with-kubernetes-and-webrtc-rachel-sheikh-twitter
- Busca YouTube: https://www.youtube.com/results?search_query=Movienight+101%3A+How+to+Power+a+Video+Streaming+with+Kubernetes+and+WebRTC+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Movienight 101: How to Power a Video Streaming with Kubernetes and WebRTC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0n/movienight-101-how-to-power-a-video-streaming-with-kubernetes-and-webrtc-rachel-sheikh-twitter
- YouTube search: https://www.youtube.com/results?search_query=Movienight+101%3A+How+to+Power+a+Video+Streaming+with+Kubernetes+and+WebRTC+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GrozSkmVHdw
- YouTube title: Movienight 101: How to Power a Video Streaming with Kubernetes and WebRTC - Rachel Sheikh, Twitter
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/movienight-101-how-to-power-a-video-streaming-with-kubernetes-and-webr/GrozSkmVHdw.txt
- Transcript chars: 14332
- Keywords: server, client, webrtc, everyone, wanted, session, explore, stream, connection, streaming, watching, clients, instance, having, candidates, connect, however, latency

### Resumo baseado na transcript

hello hello everyone how's everyone doing today um i am very excited this is my first time in la and my first time ever speaking at a conference so we're gonna hope for the best let's do it my name is rachel sheik i use she her pronouns i'm a software engineer at twitter where i work on all twitter's live audio and video services most notably our product twitter spaces which is sort of a conversational approach to social media where you can as a host invite some speakers

### Excerpt da transcript

hello hello everyone how's everyone doing today um i am very excited this is my first time in la and my first time ever speaking at a conference so we're gonna hope for the best let's do it my name is rachel sheik i use she her pronouns i'm a software engineer at twitter where i work on all twitter's live audio and video services most notably our product twitter spaces which is sort of a conversational approach to social media where you can as a host invite some speakers in and have a bunch of listeners as your audience and just talk about whatever you want you can find me on twitter at rachel chic and without further ado let's jump into how today's talk is going to work i'm going to keep things fairly high level and accessible to all all audiences so we're going to cover what movie night is what webrtc is how i used webrtc how i use kubernetes and some core learnings and takeaways that i learned throughout this project that you guys can take forward if you ever want to follow my footsteps so let's kick it off so what is movie night let me grab a drink of water real quick so i really like movies and tv shows as do most people and i really enjoy watching them with friends and family however when we were quarantining at the beginning of the pandemic it became really difficult to sync things up and get a watch party together and it's always a hassle trying to sync things up over the phone where you're trying to like start in the middle of a show and everyone is trying to get to the right time stamp and then it's just off by a millisecond so you're hearing an echo the entire time so i wanted to create something to solve this problem if you've ever used disney plus they have their new group watch feature or if you use the chrome extension netflix party it's very similar to this where it's a distributed approach to concurrently streaming video across multiple peers so yeah so it's just something you can start up as a host start a stream and then kick back and watch with your friends and they can join in whenever they want so let's go over the core technology i used to build this webrtc web being that it can go across web clients for the most part you have your chrome firefox opera pretty seamless rtc stands for real-time communication and this is an open source framework developed by google to enable peer-to-peer connections across different browsers there are a few key terms we want to go over before we jump into really explaining how i use this technology but
