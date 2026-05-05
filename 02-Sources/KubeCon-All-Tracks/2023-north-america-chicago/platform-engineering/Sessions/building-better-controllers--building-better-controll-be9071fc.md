---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["John Howard", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2oY/building-better-controllers-john-howard-google
youtube_search_url: https://www.youtube.com/results?search_query=Building+Better+Controllers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building Better Controllers - John Howard, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: John Howard, Google
- Schedule: https://kccncna2023.sched.com/event/1R2oY/building-better-controllers-john-howard-google
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Better+Controllers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building Better Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oY/building-better-controllers-john-howard-google
- YouTube search: https://www.youtube.com/results?search_query=Building+Better+Controllers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GKPBQDJ2Hjk
- YouTube title: Building Better Controllers - John Howard, Google
- Match score: 0.82
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-better-controllers/GKPBQDJ2Hjk.txt
- Transcript chars: 32988
- Keywords: controller, controllers, actually, writing, config, useful, library, testing, output, probably, write, outputs, inputs, object, simple, saying, reading, update

### Resumo baseado na transcript

all right hello everyone welcome I'm John Howard I am a software engineer at Google and I'm really excited to be here talking with you guys about some ideas for how we can build kubernetes controllers uh in some better patterns I'm especially excited to be here on a Tuesday talking about something other than service mesh which always is on Friday night so just a quick overview what we're going to be talking about first I'm going to go over what are controllers how many people here know what

### Excerpt da transcript

all right hello everyone welcome I'm John Howard I am a software engineer at Google and I'm really excited to be here talking with you guys about some ideas for how we can build kubernetes controllers uh in some better patterns I'm especially excited to be here on a Tuesday talking about something other than service mesh which always is on Friday night so just a quick overview what we're going to be talking about first I'm going to go over what are controllers how many people here know what a kubernetes controller is all right quite a few kind of what I expected how many of you are involved in the development of controllers in in some way like you write the code or even you just read the code wow that's actually more than I expected so that's good um so I'm glad everyone knows what controllers are you might have some different ideas of what a controller is than me so I'm still going to go over it next I'm going to try and convince you that writing controllers is pretty hard to do correctly you might already have this opinion in which case it won't be a hard uh argument but if not uh you know we're going to go over this and specifically I'm going to talk about a lot of the challenges we faced in EO uh I've been working at EO for about five years now uh mostly on you know the control plane which is basically a big controller and we've had a lot of challenges that are somewhat unique to EO compared to other controller projects and so we'll give kind of a deep dive into that and then talk about some ways that we can solve these problems and kind of introduce a different approach to writing controllers so if we if we look at what are controllers kubernetes has this this big blurb it's very useful but quite long I like to think of controller as something that takes in some input and has some output it's a very broad generic thing uh so for an example in kubernetes a user creates a deployment there is a controller that reads the deployment and outputs a replica set right that is a controller some input and some output and kubernetes is not just one controller it consists of a ton of different controllers that all operate together to give us the kubernetes experience that we know and maybe love uh so there's another controller that takes a replica set and outputs a pod there's another one that takes pods and services and outputs endpoints and kubernetes is extremely extensible as I'm sure you you've noticed right you can have custom controllers that are thirdparty
