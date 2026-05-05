---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Konstantin Ostrovsky", "Torq.io"]
sched_url: https://kccnceu2025.sched.com/event/1txEj/grpc-5-years-later-is-it-still-worth-it-konstantin-ostrovsky-torqio
youtube_search_url: https://www.youtube.com/results?search_query=gRPC%3A+5+Years+Later%2C+Is+It+Still+Worth+It%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# gRPC: 5 Years Later, Is It Still Worth It? - Konstantin Ostrovsky, Torq.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United Kingdom / London
- Speakers: Konstantin Ostrovsky, Torq.io
- Schedule: https://kccnceu2025.sched.com/event/1txEj/grpc-5-years-later-is-it-still-worth-it-konstantin-ostrovsky-torqio
- Busca YouTube: https://www.youtube.com/results?search_query=gRPC%3A+5+Years+Later%2C+Is+It+Still+Worth+It%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre gRPC: 5 Years Later, Is It Still Worth It?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEj/grpc-5-years-later-is-it-still-worth-it-konstantin-ostrovsky-torqio
- YouTube search: https://www.youtube.com/results?search_query=gRPC%3A+5+Years+Later%2C+Is+It+Still+Worth+It%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q44WBAGzKhk
- YouTube title: gRPC: 5 Years Later, Is It Still Worth It? - Konstantin Ostrovsky, Torq.io
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/grpc-5-years-later-is-it-still-worth-it/q44WBAGzKhk.txt
- Transcript chars: 18521
- Keywords: engineers, everything, clients, another, messages, basically, company, google, generated, servers, protocol, support, middleware, backward, design, called, security, define

### Resumo baseado na transcript

So excited so many people are interested in gRPC and to hear about my journey of using gRPC for the past five maybe six years. Um so a quick question who here uses gRPC in production raise your hands. And another really cool feature about it is that it's backward compatible by design. However, the problem with HTTP2 is that it has some challenges on Kubernetes with load balancing which we will address in a bit. So we said binary protocol over HTTP for performance, backward compatibility by design which was a really important aspect for our product. uh with wide support for almost all programming languages you you care about, nice Go support, TypeScript support, and it has built-in extensibility by design, which is really cool for annotating your proto l proto messages with some extra uh attributes for achieving stuff like

### Excerpt da transcript

So excited so many people are interested in gRPC and to hear about my journey of using gRPC for the past five maybe six years. Um so a quick question who here uses gRPC in production raise your hands. Nice. So we have quite a few people who are not using gRPC and this talk will be excellent for you and obviously for those who already do. Um so a quick introduction my name is Constantine. I'm the chief architect at Torque a cyber security no code automation startup. I love working at cyber security startups and for the past 12 15 years I've been a member of several of them. I have a guilty pleasure. I love optimizing CI build times. Who here loves optimizing CI build times? Raise your hand. Yeah, it's a rabbit hole you go down into and you you can spend days on it shaving those seconds. Just so you know what to talk is about and our what basically set the stage for using gRPC few words about what we do and our tech stack. So think of us as Zapier for security automation ex sorry for security analysts people who have to build automation but they don't like writing code they like graphical user interface building automations in the UI uh we are a team of about 50 engineers now uh we do microservices we use go we use gRPC for everything which is a bit unusual because in the front end world front end engineers don't really like using gRPC and it's quite not ordinary for them to do it.

Uh we use Postgress radius and all that stuff. Um we run millions of automations every day and we run on top of GCP. So why did we pick JRPC? The team who started building this company was originally working together at a pre at another company. In that company, we were like, "Yeah, REST API, Swagger, Open API files and stuff, but we didn't like the code generation tools that were available at the time for REST, specifically in in the Go ecosystem. They weren't that great. So what ended up happening is that our engineers didn't like the generated code and they would go and implement clients and servers themselves which meant you had like five different implementations for handlers and for clients and it was a pain to maintain it. So our primary goal with gRPC was this looks like a framework that is backed by a large company, a large ecosystem opensource community. We believe that the code generation tools available for this tool will be great and this will reduce the workload that our engineers have to deal with and not have to think too much about how to implement this layer for
