---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Aidan Delaney", "Bloomberg"]
sched_url: https://kccncna2022.sched.com/event/182Mi/building-multi-architecture-images-with-buildpacks-aidan-delaney-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Building+Multi-Architecture+Images+With+Buildpacks+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building Multi-Architecture Images With Buildpacks - Aidan Delaney, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Aidan Delaney, Bloomberg
- Schedule: https://kccncna2022.sched.com/event/182Mi/building-multi-architecture-images-with-buildpacks-aidan-delaney-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Multi-Architecture+Images+With+Buildpacks+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building Multi-Architecture Images With Buildpacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Mi/building-multi-architecture-images-with-buildpacks-aidan-delaney-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Building+Multi-Architecture+Images+With+Buildpacks+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Sdr5axlOnDI
- YouTube title: Building Multi-Architecture Images With Buildpacks - Aidan Delaney, Bloomberg
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-multi-architecture-images-with-buildpacks/Sdr5axlOnDI.txt
- Transcript chars: 36276
- Keywords: platform, images, platforms, python, support, application, approach, multi-architecture, builder, question, dependencies, multiple, target, developers, output, provide, docker, manifest

### Resumo baseado na transcript

hi all uh I'm Aiden I'm one of the billpacks.io team leads and I want to talk today about multi-architecture images surprisingly or I don't know what I don't really have any answers in this talk but I would like to ask a lot of questions um but firstly as I said I kind of got to introduce myself and then I'd like to get a picture of your general knowledge of of build packs I've spoken to some people already just to see where things are so as I well as I said you know the platforms on K-POP are pack and kpac are released on multiple architectures however with this talk we're particularly interested in the output image and many of us are interested in deploying output applications on both AMD 64 and arm 64. have is an arm 64 machine and we'd like to make the development process experience as neat and efficient for developers using non-amd 64 Hardware so suppose I'm really scoping the questions around multi-architecture support at the moment to considering Linux and AMD 64 and so how do we go about supporting multi-architecture at buildpax is it simply the case that if we provide arm 64 build packs then the problem is solved well I kind of want to think about the problem from the perspective of each of our three user groups um from the perspective of an application developer an application developer as we figured out before just wants to build a production image and it seems...

### Excerpt da transcript

hi all uh I'm Aiden I'm one of the billpacks.io team leads and I want to talk today about multi-architecture images surprisingly or I don't know what I don't really have any answers in this talk but I would like to ask a lot of questions um but firstly as I said I kind of got to introduce myself and then I'd like to get a picture of your general knowledge of of build packs I've spoken to some people already just to see where things are so as I mentioned I'm Aiden I'm part of a team in Bloomberg that develops app or platforms on which are AI engineers at Bloomberg depend and for us Bill packs are a critical component because they allow the Bloomberg AI Engineers to achieve High Velocity when they iterate on experiments so I'm also a bill paxterio team lead where I mostly help with documentation so if you find any problems with the documentation you can just shout at me um in this talk I want to give a brief overview on the state of Bill Pax in I want to present some motivation around why we might want multi-architecture images and then I'm going to present kind of three high-level approaches to implementing multi-architecture images as I said it's important to note that we don't yet actually have a solution for this um but I'm trying to ask a lot of questions um and I'm not going to get down and deep into the code in this talk so it should be a high level the key Focus though is to accelerate the discussion around multi-architecture images and to encourage kind of uh design questions around it so I've spoken to some of you but um could I get maybe a hands up if you're kind of interested in build packs but haven't yet done very much with them oh wow interesting that's over half the talk so certainly I've got some stuff in this talk certainly early on that will hopefully uh wet your appetite and you can talk to me later about more details of the buildbacks.io booth um hands up here if you've got a reasonable amount of experience with Bill packs there's a couple of people here whose ways of amount of experience okay great I'm certainly going to be leaning on those of you uh to contribute to the this talk or the questions later on and then I do recognize some faces Stephen and Max you are the uh season build packs users but are there any kind of seasoned Bill packed veterans out there in the audience oh you're hiding in the back there fantastic Matt you just Matt's giving me kind of half yeah he's only a k-pak developer but hey so what are build packs is kind o
