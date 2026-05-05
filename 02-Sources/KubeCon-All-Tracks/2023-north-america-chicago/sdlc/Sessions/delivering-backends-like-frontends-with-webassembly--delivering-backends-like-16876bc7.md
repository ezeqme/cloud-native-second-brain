---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["Runtime Containers"]
speakers: ["Brooks Townsend", "Cosmonic"]
sched_url: https://kccncna2023.sched.com/event/1R2r8/delivering-backends-like-frontends-with-webassembly-brooks-townsend-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Delivering+Backends+Like+Frontends+with+WebAssembly+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Delivering Backends Like Frontends with WebAssembly - Brooks Townsend, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Runtime Containers]]
- País/cidade: United States / Chicago
- Speakers: Brooks Townsend, Cosmonic
- Schedule: https://kccncna2023.sched.com/event/1R2r8/delivering-backends-like-frontends-with-webassembly-brooks-townsend-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Delivering+Backends+Like+Frontends+with+WebAssembly+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Delivering Backends Like Frontends with WebAssembly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2r8/delivering-backends-like-frontends-with-webassembly-brooks-townsend-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Delivering+Backends+Like+Frontends+with+WebAssembly+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9SEjNqKVinc
- YouTube title: Delivering Backends Like Frontends with WebAssembly - Brooks Townsend, Cosmonic
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/delivering-backends-like-frontends-with-webassembly/9SEjNqKVinc.txt
- Transcript chars: 32187
- Keywords: application, running, assembly, branch, little, actually, wasm, network, server, platform, central, request, runtime, working, essentially, everything, inventory, branches

### Resumo baseado na transcript

all right hello everyone uh welcome to delivering backends like front ends with web assembly my name is Brooks Townsen I'm a lead software engineer at Cosmic and I've been a cncf wasm cloud maintainer since 2019 um even before it was called wasm Cloud so I've been doing web assembly stuff on the back end for quite a few years now serial open source contributor I love working with web assembly especially anything that has to do with rust and I'm a demo Enthusiast of course as you'll get

### Excerpt da transcript

all right hello everyone uh welcome to delivering backends like front ends with web assembly my name is Brooks Townsen I'm a lead software engineer at Cosmic and I've been a cncf wasm cloud maintainer since 2019 um even before it was called wasm Cloud so I've been doing web assembly stuff on the back end for quite a few years now serial open source contributor I love working with web assembly especially anything that has to do with rust and I'm a demo Enthusiast of course as you'll get to see today so taking a look at what we're going to talk about I want to go a little bit in the back into like what is a CDN like why people use them at all transfer that knowledge into Network optimization for backend applications diagrams do some demos do some more demos look at some more diagrams all that all that good good stuff try not to bore you too much in the post lunch hour and then really get into like what is all of this really good for and where are we going to go next with some kind of Technology like this so to start I found this really awesome blog to Define what is a Content delivery Network which I trust cloudflare with this kind of stuff at its core a CDN is a network of servers linked together with the goal of delivering content as quickly cheaply reliably and securely as possible in this blog it talks about how a CDN is a distributed network of edge nodes that's caching static front-end content as close to user as possible but it does specifically call out that this isn't a replacement for web hosting in general you still have to have some server somewhere that your assets are coming from that you're running your backend ultimately the data for your application has to live somewhere now why do people use cdns first of all they want their application to be quick and they don't want to spend a lot of money on egress cost these are two of the biggest things that people use CDN for and if you haven't used them explicitly on your own you can compile your static assets and then package them in a CDN and essentially what it looks like sorry for all the people who want to see the memes there's more there's more I promise this is kind of like a high level architecture diagram of what happens when you're using a CDN you've got your backend somewhere well we'll call it Like Us West where it's you know your go your node.js your rust whatever your your backend and the hosting platform for your application is running in Some central place when a user makes a request
