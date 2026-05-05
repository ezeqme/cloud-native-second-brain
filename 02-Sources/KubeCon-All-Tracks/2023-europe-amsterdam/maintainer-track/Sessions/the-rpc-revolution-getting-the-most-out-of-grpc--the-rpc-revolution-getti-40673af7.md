---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Richard Belleville", "Kevin Nilson", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyTC/the-rpc-revolution-getting-the-most-out-of-grpc-richard-belleville-kevin-nilson-google
youtube_search_url: https://www.youtube.com/results?search_query=The+RPC+Revolution%3A+Getting+the+Most+Out+of+gRPC+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The RPC Revolution: Getting the Most Out of gRPC - Richard Belleville & Kevin Nilson, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Richard Belleville, Kevin Nilson, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyTC/the-rpc-revolution-getting-the-most-out-of-grpc-richard-belleville-kevin-nilson-google
- Busca YouTube: https://www.youtube.com/results?search_query=The+RPC+Revolution%3A+Getting+the+Most+Out+of+gRPC+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The RPC Revolution: Getting the Most Out of gRPC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTC/the-rpc-revolution-getting-the-most-out-of-grpc-richard-belleville-kevin-nilson-google
- YouTube search: https://www.youtube.com/results?search_query=The+RPC+Revolution%3A+Getting+the+Most+Out+of+gRPC+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9dBMPrwtGAQ
- YouTube title: The RPC Revolution: Getting the Most Out of gRPC - Richard Belleville & Kevin Nilson, Google
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-rpc-revolution-getting-the-most-out-of-grpc/9dBMPrwtGAQ.txt
- Transcript chars: 34355
- Keywords: protobuf, resource, account, method, client, actually, update, within, message, gateway, little, orientation, methods, protocol, fields, volume, server, standard

### Resumo baseado na transcript

all right the crowd work has come to an end it's 11 A.M so we can actually talk about grpc the thing that you're here to hear about uh yes clapping for our terrible jokes to end uh all right so this talk is the RPC Revolution getting the most out of grpc I am Richard Belleville I'm a software engineer I'm the grpc team I work on the python bindings but also a ton of other stuff Within grpc thank you Richard uh yeah my name is Kevin Nelson to learn some more basic things too if you need that all right so this is going to be full life cycle covering every aspect of the process of running an RPC based system including API design developer velocity and even operating the system in

### Excerpt da transcript

all right the crowd work has come to an end it's 11 A.M so we can actually talk about grpc the thing that you're here to hear about uh yes clapping for our terrible jokes to end uh all right so this talk is the RPC Revolution getting the most out of grpc I am Richard Belleville I'm a software engineer I'm the grpc team I work on the python bindings but also a ton of other stuff Within grpc thank you Richard uh yeah my name is Kevin Nelson and I'm one of the leads on the on the grpc team uh I I you know we talked to folks before we got started and it seemed like about half of you were extremely familiar with grpc and frequent users um but for the rest of you kind of you know what is grpc um we are you know very very popular framework um that has adoption across many languages ability for servers to talk to each other in different languages and a lot of adoption and uh you know for us we really see ourselves if you are doing micro services or thinking about microservices we feel like grpc is is really a great framework for doing that and so if you're considering microservices or User it's a it's a great thing if you're not grpc is still amazing so cool so uh I'm gonna go over a quick kind of just you know adoption and some high level stuff and then I'll pass it off to Richard for more of the the technical details uh and I wanted to share kind of some of the numbers some of the things that we're proud of and the continued growth and Adoption of grpc uh as you can see here for node.js uh six million weekly downloads so in npm and uh python we're actually the the number 59 most downloaded package on Pipi so that's pretty impressive and Richard here he's our our Tech lead for python and then finally uh in Java uh you know for the for Maven Maven Central uh we have 12 and a half uh million downloads uh every month and uh Sanjay in the front row here he's uh he's on the on the Java team so here's a chart uh from Star history from GitHub and this is our main grpc kind of grpc grpc repo not one of the language repos but the main core repo and as you can see uh going way back 2016 to today continued kind of linear growth and adoption is is really really strong and healthy and we want to thank all of you for that we're really proud of it hope it continues to grow and you know just a reminder for those of you who are considering we're very active very vibrant and things are going well uh one of the the key products that uh we're launching and I had a discussion with th
