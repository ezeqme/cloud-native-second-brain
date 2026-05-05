---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Terence Lee", "Heroku (Salesforce)", "Juan Bustamante", "VMware"]
sched_url: https://kccncna2023.sched.com/event/1R2uq/getting-buildpacks-ready-for-the-multi-architecture-future-terence-lee-heroku-salesforce-juan-bustamante-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Getting+Buildpacks+Ready+for+the+Multi-Architecture+Future+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Getting Buildpacks Ready for the Multi-Architecture Future - Terence Lee, Heroku (Salesforce) & Juan Bustamante, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Terence Lee, Heroku (Salesforce), Juan Bustamante, VMware
- Schedule: https://kccncna2023.sched.com/event/1R2uq/getting-buildpacks-ready-for-the-multi-architecture-future-terence-lee-heroku-salesforce-juan-bustamante-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Getting+Buildpacks+Ready+for+the+Multi-Architecture+Future+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Getting Buildpacks Ready for the Multi-Architecture Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uq/getting-buildpacks-ready-for-the-multi-architecture-future-terence-lee-heroku-salesforce-juan-bustamante-vmware
- YouTube search: https://www.youtube.com/results?search_query=Getting+Buildpacks+Ready+for+the+Multi-Architecture+Future+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v1R-5LMdDq8
- YouTube title: Getting Buildpacks Ready for the Multi-Architecture Future - Terence Lee & Juan Bustamante
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/getting-buildpacks-ready-for-the-multi-architecture-future/v1R-5LMdDq8.txt
- Transcript chars: 25077
- Keywords: actually, images, architecture, multi-architecture, architectures, docker, salesforce, developers, support, builds, started, produce, manifest, itself, buildpack, experience, essentially, running

### Resumo baseado na transcript

um so we're here to talk about how Bill packs we going to tackle basically handling mul architecture image builds um the QR code in the top right uh is for rating this talk um and it we'll have it also at the end so you don't need to scan it right now uh if you don't want to my name is Terence Lee I'm one of the I guess co-founders of the cloud Bill packs project uh work at Salesforce and Heroku um Juan was on kind of the

### Excerpt da transcript

um so we're here to talk about how Bill packs we going to tackle basically handling mul architecture image builds um the QR code in the top right uh is for rating this talk um and it we'll have it also at the end so you don't need to scan it right now uh if you don't want to my name is Terence Lee I'm one of the I guess co-founders of the cloud Bill packs project uh work at Salesforce and Heroku um Juan was on kind of the description if you looked at the talk and unfortunately he couldn't be here uh due to Visa issues but he's actually the one that has done the bulk of the work that we're going to be talking about here um and we're going to have a video kind of later on where he will be able to kind of say a little bit uh he'll say he's a contributor but we've actually elevated him to a maintainer so um we're super excited about that and the work he's done and then uh I've replaced him in your stuck with this guy Joe U who also works at Salesforce um and different part of the company uh and also co-founded the bill packs project with me so in this talk if you don't know anything about Bill packs we'll do a quick kind of intro on them um pretty brief um and then we'll talk about why you should care about multiarch um as a whole dig into how Bill paack can help you kind of deal with that and how we're approaching and solving it and then Juan's going to um we'll have a l video from him where he's going to talk about key takeaways from The Talk itself and yeah let's get started so if you're not familiar with build packs uh we take your app source code and transform them into production grade images focus on developer experience and things like security and the quickest way to get started is to use a tool called pack that is part of the project um it's a CLI that interfaces with the dock of demon and um this is an example of the output that you get when you run a pack build uh very similar to the docker build and what you're going to get is you're going get these uh images that are kind of fine-tuned um uh for your application itself uh where we can split out basically like build and launch um concerns uh Bill packs have the option to provide a software build materials that can be um done at build time so the actual things that are ending up in your image are the things that can get documented um given the same inputs the builds are going to be reproducible um we care about security things like doing things as non-root as we do that um I mentioned kind of the a
