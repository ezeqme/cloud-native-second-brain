---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "SRE Reliability", "Community Governance"]
speakers: ["Jesse Brown", "Terence Lee", "Heroku"]
sched_url: https://kccncna2024.sched.com/event/1howD/container-image-workflows-at-scale-with-buildpacks-jesse-brown-terence-lee-heroku
youtube_search_url: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Container Image Workflows at Scale with Buildpacks - Jesse Brown & Terence Lee, Heroku

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Jesse Brown, Terence Lee, Heroku
- Schedule: https://kccncna2024.sched.com/event/1howD/container-image-workflows-at-scale-with-buildpacks-jesse-brown-terence-lee-heroku
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Container Image Workflows at Scale with Buildpacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howD/container-image-workflows-at-scale-with-buildpacks-jesse-brown-terence-lee-heroku
- YouTube search: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lT4ULcmhVT8
- YouTube title: Container Image Workflows at Scale with Buildpacks - Jesse Brown & Terence Lee, Heroku
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/container-image-workflows-at-scale-with-buildpacks/lT4ULcmhVT8.txt
- Transcript chars: 28497
- Keywords: application, images, actually, basically, docker, source, layers, produce, heroku, software, specific, allows, platform, changes, started, talking, organization, container

### Resumo baseado na transcript

hello oh mic's on excellent uh welcome I think we are the last session for you all today before the food and festivities at the booth CW so we'll try to keep this short and concise uh I'm here to talk about containers workflows at scale with Bill packs um and when I talk about scale I mean companies like Heroku Salesforce Bloomberg uh who Google who need to build billions of container images I'm Terrence Lee I'm an architect at Heroku I'm also one of the founders of the

### Excerpt da transcript

hello oh mic's on excellent uh welcome I think we are the last session for you all today before the food and festivities at the booth CW so we'll try to keep this short and concise uh I'm here to talk about containers workflows at scale with Bill packs um and when I talk about scale I mean companies like Heroku Salesforce Bloomberg uh who Google who need to build billions of container images I'm Terrence Lee I'm an architect at Heroku I'm also one of the founders of the cloud Bill packs project yeah I'm Jesse Brown I'm also an architect at Heroku and I'm a maintainer on the bill packs project um so here's the agenda of what we're going to talk about we're going to give a brief overview of what Bill packs are if you don't know what Bill packs um uh talk about how um we can build things efficiently um go into kind of some dayto operation things with how it impacts the software supply chain and then uh kind of cover the bill pack ecosystem of how you can actually use this uh in your company so starting from the top what are Bill packs uh for those of you who aren't as familiar Bill packs basically take your application source code and transforms your application into an oci image uh without the use of Docker files and what you get at the other end is a um oci image that Maps logically to your application um and so this allows you to you know use it like any other Docker image uh that you have R image you can push it up to a registry uh you can you know inherent from it with a from in another Docker in an actual Docker file um and use it it's just an oci image uh and here's an example of us building a generic Ruby application uh using the Heroku Builder uh using the pxi that's part of the project so what it what you're seeing here is it actually automatically detects uh that it's Ruby application goes and installs the Ruby runtime for you and installs all the dependencies that are part of the application itself and then you get um all the layers exported into an image and so This Is Us looking to that image uh with a tool called Dive um and you can kind of see uh the layers that are mapped here and what you get is you get uh kind of an optimized image with the minimum amount of kind of layers and things that are part of it uh as well as metadata things associated with that image itself and so you know we've been kind of showing off things with pack uh kind of from an application developer perspective right like I have an application I need to containerize it u
